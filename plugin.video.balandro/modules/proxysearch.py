# -*- coding: utf-8 -*-

import os, re

import xbmcgui

from platformcode import config, logger, platformtools
from core.item import Item
from core import channeltools, scrapertools, httptools, proxytools, filetools

color_list_prefe = config.get_setting('channels_list_prefe_color', default='gold')
color_list_proxies = config.get_setting('channels_list_proxies_color', default='red')
color_list_inactive = config.get_setting('channels_list_inactive_color', default='gray')

color_alert = config.get_setting('notification_alert_color', default='red')
color_infor = config.get_setting('notification_infor_color', default='pink')
color_adver = config.get_setting('notification_adver_color', default='violet')
color_avis  = config.get_setting('notification_avis_color', default='yellow')
color_exec  = config.get_setting('notification_exec_color', default='cyan')


channels_poe = [
        ['documaniatv', 'https://www.documaniatv.com/'],
        ['gdrive', 'https://drive.google.com/drive/'],
        ['hdfull', 'https://hdfullcdn.cc/'],
        ['playdede', 'https://playdede.com/']
        ]


def proxysearch_all(item):
    logger.info()

    your_ip = ''

    try:
       data = httptools.downloadpage('http://httpbin.org/ip').data
       data = re.sub(r'\n|\r|\t|\s{2}|&nbsp;', '', data)
       your_ip = scrapertools.find_single_match(str(data), '.*?"origin".*?"(.*?)"')
    except:
       pass

    if not your_ip:
        try:
           your_ip = httptools.downloadpage('http://ipinfo.io/ip').data
        except:
           pass

    if not your_ip:
        try:
           your_ip = httptools.downloadpage('http://www.icanhazip.com/').data
        except:
           pass

    if not your_ip:
        platformtools.dialog_ok(config.__addon_name, '[COLOR red][B]Parece que NO hay conexión con internet.[/B][/COLOR]', 'Compruebelo realizando cualquier Búsqueda, desde un Navegador Web ')

    proxies_auto = config.get_setting('proxies_auto', default=True)

    proxies_provider = config.get_setting('proxies_provider', default='10')
    if proxies_provider == 10:
        proxies_todos = True
    else:
        proxies_todos = False

    if proxies_todos:
        if proxies_auto:
            if not platformtools.dialog_yesno(config.__addon_name, '[COLOR plum][B]Este proceso requerirá un considerable espacio de tiempo según su configuración actual de proxies.[/B][/COLOR]', "[COLOR yellow]¿ Desea iniciar la búsqueda de proxies para 'Todos' los canales que los necesiten ?[/COLOR]"):
               return
        else:
           platformtools.dialog_ok(config.__addon_name, '[COLOR red][B]En los Ajustes categoría proxies de la configuración, No tiene el Modo buscar automaticamente.[/B][/COLOR]')
           return

    cfg_excludes = 'proxysearch_excludes'
    channels_excludes = config.get_setting(cfg_excludes, default='')

    proceso_seleccionar = True

    filtros = {'searchable': True}
    ch_list = channeltools.get_channels_list(filtros=filtros)

    if ch_list:
        if platformtools.dialog_yesno(config.__addon_name, '[COLOR red]¿ Desea Quitar previamente los Proxies memorizados en Todos los canales ?[/COLOR]'):
           for ch in ch_list:
               if not 'proxies' in ch['notes'].lower():
                   continue

               # por NAME vensiones anteriores a 2.0
               cfg_proxies_channel = 'channel_' + ch['name'] + '_proxies'

               if config.get_setting(cfg_proxies_channel, default=''):
                   config.set_setting(cfg_proxies_channel, '')

                   cfg_proxytools_max_channel = 'channel_' + ch['name'] + '_proxytools_max'
                   if config.get_setting(cfg_proxytools_max_channel, default=''): config.set_setting(cfg_proxytools_max_channel, '')

                   cfg_proxytools_provider = 'channel_' + ch['name'] + '_proxytools_provider'
                   if config.get_setting(cfg_proxytools_provider, default=''): config.set_setting(cfg_proxytools_provider, '')

               # por ID
               cfg_proxies_channel = 'channel_' + ch['id'] + '_proxies'
               cfg_proxytools_max_channel = 'channel_' + ch['id'] + '_proxytools_max'
               cfg_proxytools_provider = 'channel_' + ch['id'] + '_proxytools_provider'

               if not config.get_setting(cfg_proxies_channel, default=''):
                   if not config.get_setting(cfg_proxytools_max_channel, default=''):
                       if not config.get_setting(cfg_proxytools_provider, default=''):
                           continue

               if config.get_setting(cfg_proxies_channel, default=''): config.set_setting(cfg_proxies_channel, '')
               if config.get_setting(cfg_proxytools_max_channel, default=''): config.set_setting(cfg_proxytools_max_channel, '')
               if config.get_setting(cfg_proxytools_provider, default=''): config.set_setting(cfg_proxytools_provider, '')

           proceso_seleccionar = False

           if channels_excludes:
               config.set_setting(cfg_excludes, '')
               platformtools.dialog_ok(config.__addon_name, '[B][COLOR %s]Proxies y sus canales excluidos eliminados[/B][/COLOR]' % color_infor)
           else:
               platformtools.dialog_ok(config.__addon_name, '[B][COLOR %s]Proxies eliminados[/B][/COLOR]' % color_infor)

    if proceso_seleccionar:
        if not channels_excludes:
            if not platformtools.dialog_yesno(config.__addon_name, '[COLOR plum]¿ Quiere excluir canales en la búsqueda Global de Configurar proxies a usar en los canales que los necesiten ?[/COLOR]'):
                proceso_seleccionar = False

    filtros = { 'searchable': True, 'status': 0}

    ch_list = channeltools.get_channels_list(filtros=filtros)

    if proceso_seleccionar:
       preselect = []
       channels_ids = []
       opciones = []

       i = 0
       for ch in ch_list:
           if not 'proxies' in ch['notes'].lower():
               continue

           i =+1

       if i == 0:
           platformtools.dialog_notification(config.__addon_name, '[B][COLOR %s]Sin canales con proxies memorizados[/B][/COLOR]' % color_adver)
           return

       if channels_excludes:
           channels_orden = []

           i = 0
           for ch in ch_list:
               channels_orden.append(ch['id'])
               i += 1

           channels_preselct = str(channels_excludes).replace('[', '').replace(']', ',')

           matches = scrapertools.find_multiple_matches(channels_preselct, "(.*?), '(.*?)',")
           for ch_nro, ch_name in matches:
               if not ch_name in channels_orden[int(ch_nro)]:
                   tex1 = '[COLOR plum]El orden de la lista de los canales ha variado respecto a su lista anterior (Preferidos, Desactivados, Inactivos ó Anulados).[/COLOR]'
                   tex2 = '[COLOR cyan][B]Deberá seleccionar de nuevo los canales a excluir deseados.[/B][/COLOR]'
                   tex3 = '[COLOR red]Porque se eliminan los canales memorizados para excluirlos de [COLOR yellow] Configurar proxies a usar [/COLOR]'
                   platformtools.dialog_ok(config.__addon_name, tex1, tex2, tex3)
                   config.set_setting(cfg_excludes, '')
                   preselect = []
                   break

               ch_nro = ch_nro.strip()
               preselect.append(int(ch_nro))

       i = 0
       for ch in ch_list:
           if not 'proxies' in ch['notes'].lower():
               continue

           if not channels_excludes: preselect.append(i)
           channels_ids.append(ch['id'])
           i += 1

       for ch in ch_list:
           if not 'proxies' in ch['notes'].lower():
               continue

           cfg_proxies_channel = 'channel_' + ch['id'] + '_proxies'
           cfg_proxytools_max_channel = 'channel_' + ch['id'] + '_proxytools_max'
           cfg_proxytools_provider = 'channel_' + ch['id'] + '_proxytools_provider'

           if not config.get_setting(cfg_proxies_channel, default=''):
               if not config.get_setting(cfg_proxytools_max_channel, default=''):
                   if not config.get_setting(cfg_proxytools_provider, default=''):
                       continue

           info = ''

           if channels_excludes:
               channels_preselct = str(channels_excludes).replace('[', '').replace(']', ',')
               if ("'" + ch['id'] + "'") in str(channels_preselct):
                   info = info + '[COLOR moccasin][B]EXCLUIDO [/B][/COLOR]'

           if ch['status'] == 1:
               info = info + '[B][COLOR %s][I] Preferido [/I][/B][/COLOR]' % color_list_prefe
           elif ch['status'] == -1:
               info = info + '[B][COLOR %s][I] Desactivado [/I][/B][/COLOR]' % color_list_inactive

           if 'dominios' in ch['notes'].lower():
               dominio = config.get_setting('channel_' + ch['id'] + '_dominio', default='')
               if dominio:
                   dominio = dominio.replace('https://', '').replace('/', '')
                   info = info + '[B][COLOR cyan] %s [/B][/COLOR]' % dominio

           if config.get_setting(cfg_proxies_channel, default=''):
               info = info + '[B][COLOR %s] Proxies [/B][/COLOR]' % color_list_proxies
           elif config.get_setting(cfg_proxytools_provider, default=''):
               info = info + '[COLOR yellowgreen][B] Sin proxies [/B][/COLOR]'
           elif config.get_setting(cfg_proxytools_max_channel, default=''):
               info = info + '[COLOR yellowgreen][B] Sin proxies [/B][/COLOR]'

           tipos = ch['search_types']
           tipos = str(tipos).replace('[', '').replace(']', '').replace("'", '')
           tipos = str(tipos).replace('movie', 'Películas').replace('tvshow', 'Series').replace('documentary', 'Documentales').replace('all,', '')

           if info: info = info + '  '
           info = info + '[COLOR mediumspringgreen][B]' + tipos + '[/B][/COLOR]'

           idiomas = ch['language']
           idiomas = str(idiomas).replace('[', '').replace(']', '').replace("'", '')
           idiomas = str(idiomas).replace('cast', 'Esp').replace('lat', 'Lat').replace('vose', 'Vose')

           if info: info = info + '  '
           info = info + '[COLOR mediumaquamarine]' + idiomas + '[/COLOR]'

           it = xbmcgui.ListItem(ch['name'], info)
           it.setArt({'thumb': ch['thumbnail']})
           opciones.append(it)

       ret = xbmcgui.Dialog().multiselect('Excluir canales en las búsquedas de [COLOR yellow] Proxies [/COLOR]', opciones, preselect=preselect, useDetails=True)

       if ret is None:
           if platformtools.dialog_yesno(config.__addon_name, "[COLOR tan]¿ Desea abandonar la búsqueda de proxies para 'Todos' los canales que los necesiten ?[/COLOR]"):
               return

       seleccionados = channels_excluded_list(ret, channels_ids, channels_excludes)

       if str(seleccionados) == '[]': seleccionados = ''
       config.set_setting(cfg_excludes, str(seleccionados))

    channels_excludes = config.get_setting(cfg_excludes, default='')

    for ch in ch_list:
        if not 'proxies' in ch['notes'].lower():
            continue

        if channels_excludes:
            channels_preselct = str(channels_excludes).replace('[', '').replace(']', ',')
            if ("'" + ch['id'] + "'") in str(channels_preselct):
                platformtools.dialog_notification(ch['name'], '[B][COLOR %s]Ignorado por excluido[/COLOR][/B]' % color_exec)
                continue

        proxysearch_channel(item, ch['id'], ch['name'])

    txt = 'Revise los canales, porque podria ser que algún canal no los necesite ó viceversa, '
    txt += 'para ello bastará con entrar al canal y ver si se presentan listas en cualquiera de sus opciones, '
    txt += 'en este caso deberá eliminar los proxies memorizados ó configurarlos de nuevo dentro del canal.'

    platformtools.dialog_ok(config.__addon_name, 'Proceso configurar proxies a usar y su memorización Finalizado.', '[COLOR yellow][B]' + txt + '[/COLOR][/B]')


def channels_excluded_list(ret, channels_ids, channels_excludes):
    logger.info()

    channel_sel = []
    seleccionados = []

    if channels_excludes:
        for ch in ret:
            channel_sel.append(ch)
    else:
        nro_sel = 0
        for ch in ret:
            if not ch == nro_sel:
                channel_sel.append(nro_sel)
                nro_sel += 1

                while not (nro_sel == ch):
                    channel_sel.append(nro_sel)
                    nro_sel += 1

            nro_sel += 1

    for ch_sel in channel_sel:
        seleccionados.append(ch_sel)
        i_id = 0

        for channel_id in channels_ids:
            if ch_sel == i_id: seleccionados.append(channel_id)
            i_id += 1

    return seleccionados


def proxysearch_channel(item, channel_id, channel_name):
    logger.info()

    el_canal = '[B][COLOR %s]' % color_exec
    el_canal += channel_name
    el_canal += '[COLOR %s] buscando ...[/COLOR][/B]' % color_avis
    platformtools.dialog_notification('Buscar proxies', el_canal)

    channel_py = channel_id + '.py'
    filename_py = os.path.join(config.get_runtime_path(), 'channels', channel_py)

    dominio = config.get_setting('dominio', channel_id, default='')

    host = ''

    channel_poe = "'" + channel_id + "'"
    esta_en_poe = False

    if channel_poe in str(channels_poe):
        for x in channels_poe:
            if x[0] == channel_id:
               esta_en_poe = True
               channel_poe = x[0]
               host = x[1]
               break

    if not esta_en_poe:
       if dominio:
           host = dominio
       else:
           try:
              data = filetools.read(filename_py)
           except:
              el_canal = ('Se ignora este canal en el proceso, no se pudo acceder a su módulo ' + channel_py  + '[B][COLOR %s] en el caso de que requiera proxies, deberá efectuar esta Configuracíon dentro del propio canal.') % color_alert
              platformtools.dialog_ok(config.__addon_name + ' ' + channel_name , el_canal + '[/COLOR][/B]')
              return

           part_py = 'mainlist'
           if 'configurar_proxies' in data: part_py = 'configurar_proxies'
           elif 'do_downloadpage' in data: part_py = 'do_downloadpage'

           bloc = scrapertools.find_single_match(data.lower(), '(.*?)' + part_py)
           bloc = re.sub(r'\n|\r|\t|\s{2}|&nbsp;', '', bloc)

           host = scrapertools.find_single_match(bloc, 'host.*?"(.*?)"')
           if not host:
               host = scrapertools.find_single_match(bloc, "host.*?'(.*?)'")

    host = host.strip()

    if not host:
        if dominio:
            host = dominio

    if not host:
        if channel_name == 'NewPct1':
            el_canal = ('Se ignora este canal en el proceso, porque Falta seleccionar que dominio "CLON" se utilizará  [B][COLOR %s]' + channel_name) % color_alert
        else:
            el_canal = ('Se ignora este canal en el proceso, porque Falta seleccionar que dominio "HOST" se utilizará  [B][COLOR %s]' + channel_name) % color_alert
        platformtools.dialog_ok(config.__addon_name, el_canal + '[/COLOR][/B]')
        return

    cfg_proxies_channel = 'channel_' + channel_id + '_proxies'

    if not config.get_setting(cfg_proxies_channel, default=''):
        response = httptools.downloadpage(host, raise_weberror=False)
        if response.sucess == True:
            if len(response.data) > 999:
                 el_canal = ('[B][COLOR %s]No necesita proxies  ') % color_list_proxies
                 el_canal += ('[COLOR %s]' + channel_name + '[/COLOR][/B]') % color_exec
                 platformtools.dialog_notification(config.__addon_name, el_canal)
                 return

    return proxytools.configurar_proxies_canal(channel_name, host)


def channels_proxysearch_del(item):
    logger.info()

    cfg_excludes = 'proxysearch_excludes'
    canales_excluidos = config.get_setting(cfg_excludes, default='')

    canales_excluidos = scrapertools.find_multiple_matches(str(canales_excluidos), "(.*?), '(.*?)'")

    txt_excluidos = ''

    for orden_nro, id_canal in canales_excluidos:
        if not txt_excluidos: txt_excluidos = id_canal.capitalize()
        else: txt_excluidos += (', ' + id_canal.capitalize())

    if not platformtools.dialog_yesno(config.__addon_name, '[COLOR plum]' + str(txt_excluidos) + '[/COLOR]', '[COLOR red]¿ Desea anular los canales memorizados para excluirlos de Configurar Proxies a usar ?[/COLOR]'):
        return

    config.set_setting(cfg_excludes, '')

    platformtools.itemlist_refresh()