# -*- coding: utf-8 -*-

import re

from platformcode import config, logger, platformtools
from core.item import Item
from core import httptools, scrapertools, tmdb, servertools


host = 'https://seriez.co/'


def mainlist(item):
    logger.info()
    itemlist = []

    itemlist.append(item.clone( title = 'Películas', action = 'mainlist_pelis' ))
    itemlist.append(item.clone( title = 'Series', action = 'mainlist_series' ))

    itemlist.append(item.clone( title = 'Buscar ...', action = 'search', search_type = 'all' ))

    return itemlist


def mainlist_pelis(item):
    logger.info()
    itemlist = []

    itemlist.append(item.clone( title = 'Catálogo', action = 'list_all', url = host + 'todas-las-peliculas', search_type = 'movie' ))

    itemlist.append(item.clone( title = 'Estrenos', action = 'list_all', url = host + 'estrenos-cine', search_type = 'movie' ))
    itemlist.append(item.clone( title = 'Más valoradas', action = 'list_all', url = host + 'peliculas-mas-valoradas', search_type = 'movie' ))

    itemlist.append(item.clone( title = 'Por género', action = 'generos', search_type = 'movie' ))
    itemlist.append(item.clone( title = 'Por año', action = 'anios', search_type = 'movie' ))

    itemlist.append(item.clone( title = 'Buscar película ...', action = 'search', search_type = 'movie' ))

    return itemlist


def mainlist_series(item):
    logger.info()
    itemlist = []

    itemlist.append(item.clone( title = 'Catálogo', action = 'list_all', url = host + 'todas-las-series', search_type = 'tvshow' ))

    itemlist.append(item.clone( title = 'Más valoradas', action = 'list_all', url = host + 'mas-valoradas', search_type = 'tvshow' ))

    itemlist.append(item.clone( title = 'Por género', action = 'generos', search_type = 'tvshow' ))
    itemlist.append(item.clone( title = 'Por año', action = 'anios', search_type = 'tvshow' ))

    itemlist.append(item.clone( title = 'Buscar serie ...', action = 'search', search_type = 'tvshow' ))

    return itemlist


def generos(item):
    logger.info()
    itemlist = []

    url = host + ('todas-las-series' if item.search_type == 'tvshow' else 'todas-las-peliculas')
    data = httptools.downloadpage(url).data

    matches = re.compile('onclick="cfilter\(this, \'([^\']+)\', 1\);"', re.DOTALL).findall(data)
    for title in matches:
        url = host + 'filtrar/%s/%s,/,' % ('series' if item.search_type == 'tvshow' else 'peliculas', title)

        itemlist.append(item.clone( title=title, url=url, action='list_all' ))

    return sorted(itemlist, key=lambda it: it.title)


def anios(item):
    logger.info()
    itemlist = []

    from datetime import datetime
    current_year = int(datetime.today().year)

    for x in range(current_year, 1970, -1):
        url = host + 'filtrar/%s/,/,%d' % ('series' if item.search_type == 'tvshow' else 'peliculas', x)

        itemlist.append(item.clone( title=str(x), url=url, action='list_all' ))

    return itemlist


def list_all(item):
    logger.info()
    itemlist = []

    es_busqueda = 'search?' in item.url

    data = httptools.downloadpage(item.url).data

    patron = '<article>\s*<a href="([^"]+)">\s*<div class="stp">(\d+)</div>'
    patron += '\s*<div class="Poster"><img src="[^"]+" data-echo="([^"]+)"></div>'
    patron += '\s*<h2>([^<]+)</h2>\s*<span>(.*?)</span>'

    matches = re.compile(patron, re.DOTALL).findall(data)
    for url, year, thumb, title, span in matches:
        if es_busqueda:
            tipo = 'tvshow' if 'Serie' in span else 'movie'
            if item.search_type not in ['all', tipo]: continue
        else:
            tipo = item.search_type

        sufijo = '' if item.search_type != 'all' else tipo

        if tipo == 'movie':
            itemlist.append(item.clone( action='findvideos', url=url, title=title, thumbnail=thumb, fmt_sufijo=sufijo,
                                        contentType='movie', contentTitle=title, infoLabels={'year': year} ))
        else:
            itemlist.append(item.clone( action='temporadas', url=url, title=title, thumbnail=thumb, fmt_sufijo=sufijo,
                                        contentType='tvshow', contentSerieName=title, infoLabels={'year': year} ))

    tmdb.set_infoLabels(itemlist)

    next_page_link = scrapertools.find_single_match(data, 'class="PageActiva">\d+</a><a href="([^"]+)')
    if next_page_link:
        itemlist.append(item.clone( title='>> Página siguiente', url=next_page_link, action='list_all', text_color='coral' ))

    return itemlist


def temporadas(item):
    logger.info()
    itemlist = []

    data = httptools.downloadpage(item.url).data

    matches = re.compile('onclick="activeSeason\(this,\'temporada-(\d+)', re.DOTALL).findall(data)

    for numtempo in matches:
        title = 'Temporada ' + numtempo

        if len(matches) == 1:
            platformtools.dialog_notification(item.contentSerieName.replace('&#038;', '&'), 'solo [COLOR tan]' + title + '[/COLOR]')
            item.page = 0
            item.contentType = 'season'
            item.contentSeason = numtempo
            itemlist = episodios(item)
            return itemlist

        itemlist.append(item.clone( action = 'episodios', title = title, contentType = 'season', contentSeason = numtempo, page = 0 ))

    tmdb.set_infoLabels(itemlist)

    return itemlist


def episodios(item):
    logger.info()
    itemlist = []

    if not item.page: item.page = 0
    perpage = 50

    data = httptools.downloadpage(item.url).data

    patron = '<a href="([^"]+)" onclick="return OpenEpisode\(this, (\d+), (\d+)\);"\s*>'
    patron += '<div class="wallEp"><img src="[^"]+" data-echo="([^"]+)"></div><h2>([^<]+)</h2>'

    matches1 = re.compile(patron, re.DOTALL).findall(data)

    tot_epis1 = 0

    for url, season, episode, thumb, title in matches1[item.page * perpage:]:
        if item.contentSeason:
            if not str(item.contentSeason) == str(season): continue

        tot_epis1 += 1

        titulo = '%sx%s %s' % (season, episode, title)
        itemlist.append(item.clone( action='findvideos', url=url, title=titulo, thumbnail=thumb, 
                                    contentType='episode', contentSeason=season, contentEpisodeNumber=episode ))

        if len(itemlist) >= perpage:
            break

    # Patron diferente si no hay thumbnails
    patron = '<a href="([^"]+)" onclick="return OpenEpisode\(this, (\d+), (\d+)\);"\s*>'
    patron += '<div class="wallEp" style="[^"]+"></div><h2>([^<]+)</h2>'

    matches2 = re.compile(patron, re.DOTALL).findall(data)

    tot_epis2 = 0

    for url, season, episode, title in matches2[item.page * perpage:]:
        if item.contentSeason:
            if not str(item.contentSeason) == str(season): continue

        tot_epis2 += 1

        titulo = '%sx%s %s' % (season, episode, title)
        itemlist.append(item.clone( action='findvideos', url=url, title=titulo, 
                                    contentType='episode', contentSeason=season, contentEpisodeNumber=episode ))

        if len(itemlist) >= perpage:
            break

    tmdb.set_infoLabels(itemlist)

    if (tot_epis1 + tot_epis2) > ((item.page + 1) * perpage):
        itemlist.append(item.clone( title=">> Página siguiente", action="episodios", page=item.page + 1, text_color='coral' ))

    if tot_epis2 == 0:
        return itemlist
    else:
        return sorted(itemlist, key=lambda it: (it.contentSeason, it.contentEpisodeNumber))


def puntuar_calidad(txt):
    orden = ['360p', '480p', '720p HD', '1080p HD']
    if txt not in orden: return 0
    else: return orden.index(txt) + 1


def findvideos(item):
    logger.info()
    itemlist = []

    IDIOMAS = {'1': 'Esp', '2': 'Lat', '3': 'Vose', '4': 'VO', 'Latino': 'Lat', 'Español': 'Esp', 'Subtitulado': 'Vose', 'VSO': 'VO'}

    data = httptools.downloadpage(item.url).data

    datos = scrapertools.find_multiple_matches(data, '<tr><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>')

    ses = 0

    for servidor, calidad, idioma, enlace in datos:
        ses += 1

        if servidor == 'Servidor': continue

        server = scrapertools.find_single_match(servidor, 'domain=(?:www.|dl.|)([a-z0-9]+)')
        server = servertools.corregir_servidor(server)

        url = scrapertools.find_single_match(enlace, " href='([^']+)'").strip()
        if not url.startswith('http'): url = host + url[1:]
        url = url.replace('.html.html', '.html')

        itemlist.append(Item( channel = item.channel, action = 'play', server = server, referer = item.url, title = '', url = url, 
                              language = IDIOMAS.get(idioma, idioma), quality = calidad, quality_num = puntuar_calidad(calidad) ))

    if not itemlist:
        if not ses == 0:
            platformtools.dialog_notification(config.__addon_name, '[COLOR tan][B]Sin enlaces Soportados[/B][/COLOR]')
            return

    return itemlist


def play(item):
    logger.info()
    itemlist = []

    if item.url.startswith(host):
        headers = { 'Referer': item.referer }
        data = httptools.downloadpage(item.url, headers=headers).data

        wopen = scrapertools.find_single_match(data, 'onclick="window\.open\(([^\)]+)\);"')
        if wopen:
            url = scrapertools.find_single_match(data, "%s\s*=\s*'([^']+)" % wopen)
        else:
            url = scrapertools.find_single_match(data, "enlaceeee\s*=\s*'([^']+)")
            if not url: url = scrapertools.find_multiple_matches(data, '<a id="link-redirect".*? href="([^"]+)')[-1]

        if url:
            servidor = servertools.get_server_from_url(url)
            servidor = servertools.corregir_servidor(servidor)

            if servidor and servidor != 'directo':
                url = servertools.normalize_url(servidor, url)
                itemlist.append(item.clone( url=url, server=servidor ))
    else:
        itemlist.append(item.clone())

    return itemlist


def search(item, texto):
    logger.info()
    try:
        item.url = host + 'search?go=' + texto.replace(" ", "+")
        return list_all(item)
    except:
        import sys
        for line in sys.exc_info():
            logger.error("%s" % line)
        return []
