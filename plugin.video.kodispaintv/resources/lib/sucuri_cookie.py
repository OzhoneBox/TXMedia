# copied from salt thanks
import sys
import traceback
import re
import base64
import cookielib
import urlparse


def _get_sucuri_cookie(html):
    if 'sucuri_cloudproxy_js' in html:
        match = re.search(r"S\s*=\s*'([^']+)", html)
        if match:
            s = base64.b64decode(match.group(1))
            s = s.replace(' ', '')
            s = re.sub(r'String\.fromCharCode\(([^)]+)\)', r'chr(\1)', s)
            s = re.sub(r'\.slice\((\d+),(\d+)\)', r'[\1:\2]', s)
            s = re.sub(r'\.charAt\(([^)]+)\)', r'[\1]', s)
            s = re.sub(r'\.substr\((\d+),(\d+)\)', r'[\1:\1+\2]', s)
            s = re.sub(r';location.reload\(\);', '', s)
            s = re.sub(r'\n', '', s)
            s = re.sub(r'document\.cookie', 'cookie', s)
            try:
                cookie = ''
                exec(s)
                match = re.match('([^=]+)=(.*)', cookie)
                if match:
                    return {match.group(1): match.group(2)}
            except Exception as e:
                print 'Exception during sucuri js: %s' % (e)


def _make_cookies(base_url, cookies, cj):
    domain = urlparse.urlsplit(base_url).hostname
    for key in cookies:
        c = cookielib.Cookie(0, key, str(cookies[key].split(';')[0]), port=None, port_specified=False, domain=domain, domain_specified=True,
                             domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=False, comment=None,
                             comment_url=None, rest={})
        cj.set_cookie(c)
    return cj


def createCookie(url, cj=None, agent='Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0'):
    urlData = ''
    try:
        if cj is None:
            cj = cookielib.CookieJar()
        import requests

        session = requests.session()
        session.cookies = cj

        headers = {"User-Agent": agent}

        urlData = session.get(url, headers=headers).text
        isCookie = _get_sucuri_cookie(urlData)

        if isCookie:
            session.cookies = _make_cookies(url, isCookie, cj)
            urlData = session.get(url, headers=headers).text
        return urlData
    except:
        traceback.print_exc(file=sys.stdout)
        return urlData
