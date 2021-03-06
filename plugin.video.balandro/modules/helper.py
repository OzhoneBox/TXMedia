# -*- coding: utf-8 -*-

import os, sys, time, xbmcaddon
import xbmc, xbmcgui, platform

if sys.version_info[0] >= 3:
    import xbmcvfs
    translatePath = xbmcvfs.translatePath
else:
    translatePath = xbmc.translatePath

from platformcode import config, logger, platformtools
from core import filetools
from core.item import Item

from modules import filters


ADDON_REPO_ADDONS = 'https://balandro.tk/repo/addons.xml'
ADDON_UPDATES_JSON = 'https://balandro.tk/addon_updates/updates-v2.0.0.json'

color_alert = config.get_setting('notification_alert_color', default='red')
color_infor = config.get_setting('notification_infor_color', default='pink')
color_adver = config.get_setting('notification_adver_color', default='violet')
color_avis  = config.get_setting('notification_avis_color', default='yellow')
color_exec  = config.get_setting('notification_exec_color', default='cyan')


_foro = "[COLOR plum][B][I] balandro.tk [/I][/B][/COLOR]"
_telegram = "[COLOR lightblue][B][I] t.me/Balandro_asesor [/I][/B][/COLOR]"
_team = "[COLOR hotpink][B][I] @balandro_dev_requests_bot [/I][/B][/COLOR]"


def mainlist(item):
    logger.info()
    itemlist = []

    descartar_xxx = config.get_setting('descartar_xxx', default=False)
    descartar_anime = config.get_setting('descartar_anime', default=False)

    itemlist.append(item.clone( action='', title= 'Contacto:', text_color='blue', thumbnail=config.get_thumb('pencil'), folder=False ))
    itemlist.append(item.clone( action='', title= ' - Telegram ' + _telegram + ' Asesoramiento, Dudas, Consultas, etc. ', folder=False, thumbnail=config.get_thumb('telegram') ))
    itemlist.append(item.clone( action='', title= ' - Foro ' + _foro + ' Novedades, Sugerencias, Instalaciones, etc.', folder=False, thumbnail=config.get_thumb('foro') ))

    itemlist.append(item.clone( action='', title= 'Uso:', text_color='limegreen', thumbnail=config.get_thumb('dev'), folder=False ))
    itemlist.append(item.clone( action='show_help_tips', title= ' - Trucos y consejos varios', folder=False ))
    itemlist.append(item.clone( action='show_help_use', title= ' - Ejemplos de niveles de uso', folder=False ))
    itemlist.append(item.clone( action='show_help_faq', title= ' - FAQS - Preguntas y respuestas', folder=False ))
    itemlist.append(item.clone( action='show_help_settings', title= ' - Notas sobre algunos par??metros de la configuraci??n', folder=False ))
    itemlist.append(item.clone( action='show_help_register', title= ' - Informaci??n dominios que requieren registrase', folder=False, thumbnail=config.get_thumb('news') ))
    itemlist.append(item.clone( channel='actions', title= ' - Ajustes configuraci??n (categor??a canales)', action = 'open_settings', folder=False, thumbnail=config.get_thumb('settings') ))

    itemlist.append(item.clone( action='', title= 'Canales:', text_color='chartreuse', thumbnail=config.get_thumb('dev'), folder=False ))
    if config.get_setting('developer_mode', default=False):
        itemlist.append(item.clone( action='show_channels_list', title= ' - Todos los canales', tipo = 'all', folder=False, thumbnail=config.get_thumb('stack') ))

    itemlist.append(item.clone( action='show_channels_list', title= ' - Qu?? canales est??n disponibles', folder=False, thumbnail=config.get_thumb('stack') ))
    itemlist.append(item.clone( action='channels_prefered', title= ' - Qu?? canales tiene marcados como preferidos', folder=False, thumbnail=config.get_thumb('stack') ))
    itemlist.append(item.clone( action='channels_no_actives', title= ' - Qu?? canales tiene marcados como desactivados', folder=False, thumbnail=config.get_thumb('stack') ))
    itemlist.append(item.clone( action='show_channels_list', title= ' - Qu?? canales est??n inestables', no_stable = True, folder=False, thumbnail=config.get_thumb('stack') ))
    itemlist.append(item.clone( action='show_channels_list', title= ' - Qu?? canales requieren cuenta', cta_register = True, folder=False, thumbnail=config.get_thumb('stack') ))
    itemlist.append(item.clone( action='show_channels_list', title= ' - Qu?? canales est??n temporalmente inactivos', temp_no_active = True, folder=False, thumbnail=config.get_thumb('stack') ))
    itemlist.append(item.clone( action='show_channels_list', title= ' - Qu?? canales est??n inactivos', no_active = True, folder=False, thumbnail=config.get_thumb('stack') ))

    itemlist.append(item.clone( action='', title= 'Proxies:', text_color='red', thumbnail=config.get_thumb('flame'), folder=False ))
    itemlist.append(item.clone( action='channels_with_proxies', title= ' - Qu?? canales pueden usar proxies', folder=False, thumbnail=config.get_thumb('stack') ))
    itemlist.append(item.clone( action='show_help_proxies', title= ' - Informaci??n uso de proxies', folder=False ))
    itemlist.append(item.clone( channel='actions', title= ' - Ajustes configuraci??n (categor??a proxies)', action = 'open_settings', folder=False, thumbnail=config.get_thumb('settings') ))

    itemlist.append(item.clone( action='', title= 'Torrents:', text_color='moccasin', thumbnail=config.get_thumb('torrents'), folder=False ))
    itemlist.append(item.clone( action='show_clients_torrent', title= ' - Clientes externos torrent soportados', folder=False, thumbnail=config.get_thumb('cloud') ))
    itemlist.append(item.clone( action='channels_only_torrents', title= ' - Qu?? canales pueden contener archivos torrent', folder=False, thumbnail=config.get_thumb('stack') ))
    itemlist.append(item.clone( action='show_help_torrents', title= ' - ?? D??nde obtener los add-ons para torrents ?', folder=False ))
    itemlist.append(item.clone( channel='actions', title= ' - Ajustes configuraci??n (categor??a torrents)', action = 'open_settings', folder=False, thumbnail=config.get_thumb('settings') ))

    itemlist.append(item.clone( action='', title='Buscar:', text_color='cyan', thumbnail=config.get_thumb('magnifyingglass'), folder=False ))
    itemlist.append(item.clone( channel='search', action='show_help', title = ' - Informaci??n sobre b??squedas', folder=False ))
    itemlist.append(item.clone( channel='tmdblists', action='show_help', title= ' - Informaci??n b??squedas y listas en TMDB', folder=False ))
    itemlist.append(item.clone( action='channels_no_actives', title= ' - Qu?? canales no intervienen en las b??squedas (desactivados)', folder=False, thumbnail=config.get_thumb('stack') ))
    itemlist.append(item.clone( channel='filters', title = ' - Excluir canales en las b??squedas', action = 'mainlist', thumbnail=config.get_thumb('stack') ))
    itemlist.append(item.clone( channel='proxysearch', title = ' - Configurar proxies a usar (en los canales que los necesiten)', action = 'proxysearch_all', thumbnail=config.get_thumb('flame') ))
    itemlist.append(item.clone( channel='actions', title= ' - Ajustes configuraci??n (categor??a buscar)', action = 'open_settings', folder=False, thumbnail=config.get_thumb('settings') ))

    itemlist.append(item.clone( action='', title='Preferidos:', text_color='springgreen', thumbnail=config.get_thumb('videolibrary'), folder=False ))
    itemlist.append(item.clone( action='show_help_tracking', title= ' - Informaci??n c??mo funciona', folder=False ))
    itemlist.append(item.clone( action='show_help_tracking_update', title= ' - B??squeda autom??tica de nuevos episodios', folder=False, thumbnail=config.get_thumb('videolibrary') ))
    itemlist.append(item.clone( channel='actions', title= ' - Ajustes configuraci??n (categor??a preferidos)', action = 'open_settings', folder=False, thumbnail=config.get_thumb('settings') ))

    itemlist.append(item.clone( action='', title='Descargas:', text_color='plum', thumbnail=config.get_thumb('download'), folder=False ))
    itemlist.append(item.clone( channel='actions', action='show_ubicacion', title= ' - Donde se ubican las descargas', folder=False, thumbnail=config.get_thumb('tools') ))
    itemlist.append(item.clone( channel='actions', title= ' - Ajustes configuraci??n (categor??a descargas)', action = 'open_settings', folder=False, thumbnail=config.get_thumb('settings') ))

    itemlist.append(item.clone( action='', title='Actualizar:', text_color='salmon', thumbnail=config.get_thumb('tools'), folder=False ))
    itemlist.append(item.clone( channel='actions', title= ' - Comprobar ??ltimas actualizaciones tipo Fix', action = 'check_addon_updates', folder=False, thumbnail=config.get_thumb('download') ))
    itemlist.append(item.clone( channel='actions', title= ' - Forzar todas las actualizaciones tipo Fix', action = 'check_addon_updates_force', folder=False, thumbnail=config.get_thumb('download') ))
    itemlist.append(item.clone( action='show_last_fix', title= ' - Informaci??n ??ltimo fix instalado', folder=False, thumbnail=config.get_thumb('news') ))
    itemlist.append(item.clone( channel='actions', title= ' - Ajustes configuraci??n (categor??a actualizar)', action = 'open_settings', folder=False, thumbnail=config.get_thumb('settings') ))

    presentar = True
    if descartar_xxx:
        if descartar_anime: presentar = False

    if presentar:
        itemlist.append(item.clone( action='', title= 'Parental:', text_color='orangered', thumbnail=config.get_thumb('roadblock'), folder=False ))

        if not descartar_anime:
            itemlist.append(item.clone( action='channels_only_animes', title= ' - Qu?? canales pueden tener contenido de animes', folder=False, thumbnail=config.get_thumb('anime') ))

        if not descartar_xxx:
            itemlist.append(item.clone( action='channels_only_adults', title= ' - Qu?? canales pueden tener contenido para adultos', folder=False, thumbnail=config.get_thumb('adults') ))
            itemlist.append(item.clone( action='show_help_adults', title= ' - Informacion Control parental (+18)', folder=False ))

        itemlist.append(item.clone( channel='actions', title= ' - Ajustes configuraci??n (categor??a canales)', action = 'open_settings', folder=False, thumbnail=config.get_thumb('settings') ))

    itemlist.append(item.clone( action='', title='Servidores:', text_color='gold', thumbnail=config.get_thumb('bolt'), folder=False ))
    if config.get_setting('developer_mode', default=False):
        itemlist.append(item.clone( action='show_servers_list', title= ' - Todos los servidores', tipo = 'all', folder=False, thumbnail=config.get_thumb('bolt') ))

    itemlist.append(item.clone( action='show_servers_list', title= ' - Qu?? servidores est??n disponibles', tipo = 'activos', folder=False, thumbnail=config.get_thumb('bolt') ))
    itemlist.append(item.clone( action='show_servers_list', title= ' - Qu?? servidores tienen v??as alternativas', tipo = 'alternativos', folder=False, thumbnail=config.get_thumb('bolt') ))
    itemlist.append(item.clone( action='show_servers_list', title= ' - Qu?? servidores se detectan pero no est??n soportados', tipo = 'sinsoporte', folder=False, thumbnail=config.get_thumb('bolt') ))
    itemlist.append(item.clone( action='show_servers_list', title= ' - Qu?? servidores est??n inactivos', tipo = 'inactivos', folder=False, thumbnail=config.get_thumb('bolt') ))

    itemlist.append(item.clone( channel='actions', title= ' - Ajustes configuraci??n (categor??a play)', action = 'open_settings', folder=False, thumbnail=config.get_thumb('settings') ))

    itemlist.append(item.clone( action='', title= 'Media Center:', text_color='pink', thumbnail=config.get_thumb('computer'), folder=False ))
    itemlist.append(item.clone( action='show_log', title= ' - Visualizar el fichero log de su Media Center', folder=False, thumbnail=config.get_thumb('computer') ))
    itemlist.append(item.clone( action='copy_log', title= ' - Obtener una copia del fichero log de su Media Center', folder=False, thumbnail=config.get_thumb('folder') ))
    #itemlist.append(item.clone( action='upload_pastebin', title= ' - Subir a Pastebin el fichero log de su Media Center', folder=False, thumbnail=config.get_thumb('cloud') ))
    itemlist.append(item.clone( action='show_advs', title= ' - Visualizar el fichero advancedsettings de su Media Center', folder=False, thumbnail=config.get_thumb('keyboard') ))
    itemlist.append(item.clone( channel='actions', title= ' - Ajustes configuraci??n (categor??a sistema)', action = 'open_settings', folder=False, thumbnail=config.get_thumb('settings') ))

    itemlist.append(item.clone( action='', title= 'Sistema:', text_color='yellow', thumbnail=config.get_thumb('tools'), folder=False ))
    itemlist.append(item.clone( action='show_test', title= ' - Test status del sistema', folder=False, thumbnail=config.get_thumb('computer') ))
    itemlist.append(item.clone( channel='actions', title= ' - Comprobar el estado de su internet', action = 'test_internet', folder=False, thumbnail=config.get_thumb('crossroads') ))
    itemlist.append(item.clone( action='show_sets', title= ' - Visualizar sus ajustes personalizados', folder=False, thumbnail=config.get_thumb('settings') ))
    itemlist.append(item.clone( action='show_cook', title= ' - Visualizar su fichero de cookies', folder=False, thumbnail=config.get_thumb('folder') ))
    itemlist.append(item.clone( channel='actions', title= ' - Ajustes configuraci??n', action = 'open_settings', folder=False, thumbnail=config.get_thumb('settings') ))

    itemlist.append(item.clone( action='', title='Versi??n:', text_color='violet', thumbnail=config.get_thumb('quote'), folder=False ))
    itemlist.append(item.clone( action='show_version', title= ' - Informaci??n versi??n', folder=False, thumbnail=config.get_thumb('news') ))
    itemlist.append(item.clone( action='show_changelog', title= ' - Historial de cambios', folder=False, thumbnail=config.get_thumb('news') ))

    itemlist.append(item.clone( action='', title='Desarrollo:', text_color='fuchsia', thumbnail=config.get_thumb('quote'), folder=False ))
    itemlist.append(item.clone( action='', title= ' - Team ' + _team + ' Unirse al Equipo de Desarrollo', folder=False, thumbnail=config.get_thumb('team') ))
    itemlist.append(item.clone( action='show_dev_notes', title= ' - Notas para developers', folder=False, thumbnail=config.get_thumb('tools') ))
    itemlist.append(item.clone( action='show_license', title= ' - Licencia (Gnu Gpl v3)', folder=False, thumbnail=config.get_thumb('megaphone') ))
    itemlist.append(item.clone( action='show_legalidad', title= ' - Legalidad', folder=False, thumbnail=config.get_thumb('megaphone') ))

    return itemlist


def channels_only_animes(item):
    logger.info()

    filters.only_animes(item)

def channels_only_adults(item):
    logger.info()

    filters.only_adults(item)

def show_channels_list(item):
    logger.info()

    filters.show_channels_list(item)

def channels_with_proxies(item):
    logger.info()

    filters.with_proxies(item)

def channels_no_actives(item):
    logger.info()

    filters.no_actives(item)

def channels_prefered(item):
    logger.info()

    filters.only_prefered(item)

def channels_inestables(item):
    logger.info()

    item.no_stable = True

    filters.show_channels_list(item)

def channels_only_torrents(item):
    logger.info()

    filters.only_torrents(item)

def show_clients_torrent(item):
    logger.info()

    filters.show_clients_torrent(item)

def show_servers_list(item):
    logger.info()

    if not item.tipo: # por si venimos de config
        item.tipo = 'activos'

    filters.show_servers_list(item)


def show_help_register(item):
    logger.info()

    txt = '*) Determinadas webs obligan a registrase para permitir su acceso.'

    txt += '[CR][CR]'
    txt += ' Es importante usar [B][COLOR gold]cuentas secundarias[/COLOR][/B] para registrarse, nunca useis las vuestras personales.'

    txt += '[CR][CR]'
    txt += '*) Para ello desde otro equipo debeis accecder a la web en cuesti??n y registraros (darse de alta)'

    txt += '[CR][CR]'
    txt += ' Si desconoceis el dominio actual de esa web, mediante un navegador localizar su [B][COLOR gold]twitter[/COLOR][/B]'

    txt += '[CR][CR]'
    txt += ' Por ejemplo [B][COLOR gold]hdfull twitter oficial[/COLOR][/B]'

    txt += '[CR][CR]'
    txt += '*) Imprescindible tomar buena nota de vuestro [B][COLOR gold]Usuario y Contrase??a[/COLOR][/B] para cada web.'

    txt += '[CR][CR]'
    txt += '*) Una vez tengais vuestros datos, podeis informarlos en la configuraci??n, o bien se os solicitar?? al acceder a ese canal determinado.'

    txt += '[CR][CR]'
    txt += '*) Para el caso concreto del servidor [B][COLOR gold]Uptobox[/COLOR][/B]'

    txt += '[CR][CR]'
    txt += ' Acceder desde otro equipo a [B][COLOR gold]uptobox.com/pin[/COLOR][/B]'

    txt += '[CR][CR]'
    txt += '*) En el caso de no estar registrados proceder a ello (darse de alta)'

    txt += '[CR][CR]'
    txt += ' Iniciar la sesi??n con vuestras credenciales'
    txt += ' e introducir el [B][COLOR gold]PIN[/COLOR][/B] que se os mostr?? en la ventana al intentar reproducir, para tener vinculada vuestra cuenta.'

    txt += '[CR][CR]'
    txt += '*) Mientras mantengais las sesiones abiertas via navegador en estos dominios, no tendreis q volver a informar vuestras credenciales.'

    platformtools.dialog_textviewer('Informaci??n dominios que requieren registrase', txt)


def show_help_settings(item):
    logger.info()

    txt = '*) Las opciones para los [COLOR gold]listados de canales[/COLOR] se usan si marcas canales como preferidos o desactivados.'
    txt += ' Esto lo puedes hacer desde el men?? contextual en los listados de canales.'

    txt += '[CR][CR]'
    txt += '*) En "B??squedas" el par??metro "[COLOR gold]Resultados previsualizados por canal[/COLOR]" sirve para limitar el n??mero de coincidencias que se muestran en la pantalla de b??squeda global.'
    txt += ' Es para que no salga un listado demasiado largo ya que algunos canales son m??s sensibles que otros y pueden devolver bastantes resultados.'
    txt += ' Pero de todas maneras se puede acceder al listado de todos los resultados de cada canal concreto.'
    txt += ' Dispones de m??s par??metros personalizables en la configuraci??n "Buscar".'

    txt += '[CR][CR]'
    txt += '*) En "Reproducci??n" se puede activar Autoplay para no tener que seleccionar un servidor para reproducir.'
    txt += ' Si hay alg??n canal para el que quieras desactivar el autoplay puedes indicarlo en la configuraci??n "Play".'

    txt += '[CR][CR]'
    txt += '*) En "Reproducci??n" los par??metros para ordenar/filtrar los enlaces [COLOR gold]por idioma[/COLOR] permiten indicar nuestras preferencias de idiomas.'
    txt += ' Entre Espa??ol, Latino y Versi??n Original elije el orden que prefieres, o descarta alguno de ellos si no te interesa.'
    txt += ' Todo ello puedes personalizarlo en la configuraci??n "Play".'

    txt += '[CR][CR]'
    txt += '*) En "Reproducci??n" los par??metros para ordenar los enlaces [COLOR gold]por calidad[/COLOR] permiten mostrar antes los de m??s calidad en lugar de mostrarlos seg??n el orden que tienen en la web.'
    txt += ' Algunos canales tienen valores fiables de calidad pero otros no, depende de cada web.'
    txt += ' Todo ello puedes personalizarlo en la configuraci??n "Play".'

    txt += '[CR][CR]'
    txt += '*) En "Reproducci??n" los par??metros para ordenar/filtrar los enlaces [COLOR gold]por servidores[/COLOR] permiten hacer algunos ajustes en funci??n de los servers.'
    txt += ' Si no quieres que te salgan enlaces de ciertos servidores, escr??belos en "descartados" (ej: torrent,mega).'
    txt += ' Y si quieres priorizar algunos servidores escr??belos en "preferentes" (ej: torrent,mega), o al rev??s en "??ltima opci??n" (ej: torrent,mega).'
    txt += ' Para modificar estas opciones necesitas saber qu?? servidores te funcionan mejor y peor, en caso de duda no hace falta que lo modifiques.'
    txt += ' Todo ello puedes personalizarlo en la configuraci??n "Play".'

    txt += '[CR][CR]'
    txt += '*) Una opci??n que puede provocar una demora en los tiempos de respuesta es en configuraci??n "TMDB" si se activa "[COLOR gold]buscar informaci??n extendida[/COLOR]".'
    txt += ' Esto provoca que los listados de pel??culas y series de todos los canales tarden m??s en mostrarse ya que se hace una segunda llamada a TMDB para intentar recuperar m??s datos.'

    txt += '[CR][CR]'
    txt += '*) En "TMDB" se pueden desactivar las "[COLOR gold]llamadas a TMDB en los listados[/COLOR]".'
    txt += ' Esto provoca que los listados de pel??culas y series de todos los canales tarden menos en mostrarse pero en la mayor??a de casos no tendr??n informaci??n como la sinopsis y las car??tulas ser??n de baja calidad.'
    txt += ' Puede ser ??til desactivarlo temporalmente en casos d??nde alguna pel??cula/serie no se identifica correctamente en tmdb y se quieran ver los datos originales de la web.'

    txt += '[CR][CR]'
    txt += '*) Exiten m??s par??metros en la [COLOR gold]Configuracion[/COLOR] de Balandro,  para tener personalizada su ejecuci??n.'
    txt += ' Divididos en agruaciones [COLOR gold]Canales, Play, Proxies, Torrents, Buscar, Preferidos, Descargas, Actualizar, etc.[/COLOR].'

    platformtools.dialog_textviewer('Notas sobre algunos par??metros de la configuraci??n', txt)


def show_help_tips(item):
    logger.info()

    txt = '*) Es importante usar el [B][COLOR gold]men?? contextual[/COLOR][/B] para acceder a acciones que se pueden realizar sobre los elementos de los listados.'
    txt += ' Si dispones de un teclado puedes acceder a ??l pulsando la tecla C, en dispositivos t??ctiles manteniendo pulsado un elemento, y en mandos de tv-box manteniendo pulsado el bot??n de selecci??n.'
    txt += ' Si usas un mando de TV es recomendable configurar una de sus teclas con "ContextMenu".'

    txt += '[CR][CR]'
    txt += '*) En los listados de canales puedes usar el men?? contextual para marcarlos como Desactivado/Activo/Preferido.'
    txt += ' De esta manera podr??s tener tus [COLOR gold]canales preferidos[/COLOR] al inicio y quitar o mover al final los que no te interesen.'
    txt += ' Los canales desactivados son accesibles pero no forman parte de las b??squedas.'

    txt += '[CR][CR]'
    txt += '*) Si en alg??n canal encuentras una pel??cula/serie que te interesa pero fallan sus enlaces, accede al men?? contextual y selecciona'
    txt += ' "[COLOR gold]buscar en otros canales[/COLOR]" para ver si est?? disponible en alg??n otro canal.'

    txt += '[CR][CR]'
    txt += '*) Desde cualquier pantalla despl??zate hacia el lateral izquierdo para desplegar algunas [COLOR gold]opciones standard de su Media Center[/COLOR].'
    txt += ' All?? tienes siempre un acceso directo a la Configuraci??n del addon y tambi??n puedes cambiar el tipo de vista que se aplica a los listados.'
    txt += ' Entre Lista, Cartel, Mays., Muro de informaci??n, Lista amplia, Muro, Fanart, escoge como prefieres ver la informaci??n.'

    txt += '[CR][CR]'
    txt += '*) Algunos canales de series tienen un listado de [COLOR gold]??ltimos episodios[/COLOR]. En funci??n de las caracter??sticas de las webs, los enlaces llevan'
    txt += ' a ver el cap??tulo o a listar las temporadas de la serie. Cuando es posible, desde el enlace se ve el episodio y desde el men?? contextual'
    txt += ' se puede acceder a la temporada concreta o la lista de temporadas.'

    txt += '[CR][CR]'
    txt += '*) Para seguir series es recomendable usar la opci??n [COLOR gold]Preferidos[/COLOR]. Busca la serie que te interese en cualquiera de los canales y desde el men?? contextual gu??rdala.'
    txt += ' Luego ves a "Preferidos" d??nde podr??s gestionar lo necesario para la serie. Adem??s puedes usar "Buscar en otros canales" y desde el listado de resultados con el men??'
    txt += ' contextual tambi??n los puedes guardar y se a??adir??n a los enlaces que ya ten??as. De esta manera tendr??s alternativas en diferentes enlaces por si alg??n d??a falla alguno o desaparece.'

    platformtools.dialog_textviewer('Trucos y consejos varios', txt)


def show_help_use(item):
    logger.info()

    txt = '[COLOR gold]Nivel 1, casual[/COLOR][CR]'
    txt += 'Accede por ejemplo a Pel??culas o Series desde el men?? principal, entra en alguno de los canales y navega por sus diferentes opciones hasta encontrar una pel??cula que te interese.'
    txt += ' Al entrar en la pel??cula se mostrar?? un di??logo con diferentes opciones de v??deos encontrados.'
    txt += ' Prueba con el primero y si el enlace es v??lido empezar?? a reproducirse. Sino, prueba con alguno de los otros enlaces disponibles.'
    txt += ' Si ninguno funcionara, desde el enlace de la pel??cula accede al men?? contextual y selecciona "Buscar en otros canales".'

    txt += '[CR][CR][COLOR gold]Nivel 2, directo[/COLOR][CR]'
    txt += 'Si quieres ver una pel??cula/serie concreta, accede a "Buscar" desde el men?? principal y escribe el t??tulo en el buscador.'
    txt += ' Te saldr?? una lista con las coincidencias en todos los canales disponibles.'

    txt += '[CR][CR][COLOR gold]Nivel 3, planificador[/COLOR][CR]'
    txt += 'Navega por los diferentes canales y ves apuntando las pel??culas/series que te puedan interesar.'
    txt += ' Para ello accede al men?? contextual desde cualquier pel??cula/serie y selecciona "Guardar enlace".'
    txt += ' Cuando quieras ver una pel??cula/serie, accede a "Preferidos" desde el men?? principal d??nde estar?? todo lo guardado.'

    txt += '[CR][CR][COLOR gold]Nivel 4, asegurador[/COLOR][CR]'
    txt += 'Descarga algunas pel??culas para tener listas para ver sin depender de la saturaci??n de la red/servidores en momentos puntuales.'
    txt += ' Desde cualquier pel??cula/episodio, tanto en los canales como en "Preferidos", accede al men?? contextual y "Descargar v??deo".'
    txt += ' Selecciona alguno de los enlaces igual que cuando se quiere reproducir y empezar?? la descarga.'
    txt += ' Para ver lo descargado, accede a "Descargas" desde el men?? principal.'

    txt += '[CR][CR][COLOR gold]Nivel 5, coleccionista[/COLOR][CR]'
    txt += 'Desde "Preferidos" accede a "Gestionar listas", d??nde puedes crear diferentes listas para organizarte las pel??culas y series que te interesen.'
    txt += ' Por ejemplo puedes tener listas para distintos usuarios de Balandro (Padres, Esposa, Hijos, etc.) o de diferentes tem??ticas, o para guardar lo que ya hayas visto, o para pasar tus recomendaciones a alg??n amigo, etc.'

    platformtools.dialog_textviewer('Ejemplos de uso de Balandro', txt)


def show_help_faq(item):
    logger.info()

    txt = '[COLOR gold]?? De d??nde viene Balandro ?[/COLOR][CR]'
    txt += 'Balandro es un addon derivado de Pelisalacarta y Alfa, simplificado a nivel interno de c??digo y a nivel funcional para el usuario.'
    txt += ' Puede ser ??til en dispositivos poco potentes como las Raspberry Pi u otros TvBox y para usuarios que no se quieran complicar mucho.'
    txt += ' Al ser un addon de tipo navegador, tiene el nombre de un velero ya que balandro era una embarcaci??n ligera y maniobrable, muy apreciada por los piratas.'

    txt += '[CR][CR][COLOR gold]?? Qu?? caracter??sticas tiene Balandro ?[/COLOR][CR]'
    txt += 'Principalmente permite acceder a los contenidos de webs con v??deos de pel??culas y series para reproducirlos y/o guardarlos, y'
    txt += ' dispone de unos Preferidos propios d??nde poder apuntar todas las Pel??culas y Series que interesen al usuario.'
    txt += ' Se pueden configurar m??ltiples opciones, por ejemplo la preferencia de idioma, la reproducci??n autom??tica, los colores para los listados, los servidores preferidos, excluir canales en las b??squedas, etc.'

    txt += '[CR][CR][COLOR gold]?? C??mo funciona el Autoplay ?[/COLOR][CR]'
    txt += 'Se puede activar la funci??n de reproducci??n autom??tica desde la configuraci??n del addon.'
    txt += ' Si se activa, al ver una pel??cula o episodio se intenta reproducir el primero de los enlaces que funcione, sin mostrarse el di??logo de selecci??n de servidor.'
    txt += ' Los enlaces se intentan secuencialmente en el mismo orden que se ver??a en el di??logo, por lo que es importante haber establecido las preferencias de idioma, servidores y calidades.'

    txt += '[CR][CR][COLOR gold]?? En qu?? orden se muestran los enlaces de servidores ?[/COLOR][CR]'
    txt += 'El orden inicial es por la fecha de los enlaces, para tener al principio los ??ltimos actualizados ya que es m??s probable que sigan vigentes, aunque en los canales que no lo informan es seg??n el orden que devuelve la web.'
    txt += ' Desde la configuraci??n se puede activar el ordenar por calidades, pero su utilidad va a depender de lo que muestre cada canal y la fiabilidad que tenga.'
    txt += ' A partir de aqu??, si hay preferencias de servidores en la configuraci??n, se cambia el orden para mostrar al principio los servidores preferentes y al final los de ??ltima opci??n.'
    txt += ' Y finalmente se agrupan en funci??n de las preferencias de idiomas del usuario.'

    txt += '[CR][CR][COLOR gold]?? Funcionan los enlaces Torrent ?[/COLOR][CR]'
    txt += 'El addon est?? preparado para tratarlos usando un gestor de torrents externo, tipo Quasar, Elementum, etc.'
    txt += ' Estos gestores externos torrents no estan incluidos en Balandro y deben Instalarse por separado.'
    txt += ' Adem??s, debe indicarse Obligatoriamente en la configuraci??n de Balandro cual va a ser su gestor de torrents habitual.'

    platformtools.dialog_textviewer('FAQ - Preguntas y respuestas', txt)


def show_help_tracking(item):
    logger.info()

    txt = '[COLOR gold]?? C??mo se guardan las pel??culas o series ?[/COLOR][CR]'
    txt += 'Desde cualquiera de los canales d??nde se listen pel??culas o series, accede al men?? contextual y selecciona "Guardar pel??cula/serie".'
    txt += ' En el caso de pel??culas es casi instant??neo, y para series puede demorarse unos segundos si tiene muchas temporadas/episodios.'
    txt += ' Para ver y gestionar todo lo que tengas, accede a "Preferidos" desde el men?? principal del addon.'
    txt += ' Tambi??n puedes guardar una temporada o episodios concretos.'

    txt += '[CR][CR][COLOR gold]?? Qu?? pasa si una pel??cula/serie no est?? correctamente identificada ?[/COLOR][CR]'
    txt += 'Esto puede suceder cuando la pel??cula/serie no est?? bien escrita en la web de la que procede o si hay varias pel??culas con el mismo t??tulo.'
    txt += ' Si no se detecta te saldr?? un di??logo para seleccionar entre varias opciones o para cambiar el texto de b??squeda.'
    txt += ' Desde las opciones de configuraci??n puedes activar que se muestre siempre el di??logo de confirmaci??n, para evitar que se detecte incorrectamente.'

    txt += '[CR][CR][COLOR gold]?? Y si no se puede identificar la pel??cula/serie ?[/COLOR][CR]'
    txt += 'Es necesario poder identificar cualquier pel??cula/serie en TMDB, sino no se puede guardar.'
    txt += ' Si no existe en [COLOR gold]themoviedb.org[/COLOR] o tiene datos incompletos puedes completar all?? la informaci??n ya que es un proyecto comunitario y agradecer??n tu aportaci??n.'

    txt += '[CR][CR][COLOR gold]?? Se puede guardar la misma pel??cula/serie desde canales diferentes ?[/COLOR][CR]'
    txt += 'S??, al guardar se apuntan en la base de datos interna los datos propios de la pel??cula, serie, temporada o episodio, y tambi??n el enlace al canal de d??nde se ha guardado.'
    txt += ' De esta manera puedes tener diferentes alternativas por si alg??n canal fallara o no tuviera enlaces v??lidos.'
    txt += ' Si tienes enlaces de varios canales, al reproducir podr??s escoger en cual intentarlo.'

    txt += '[CR][CR][COLOR gold]?? Se guardan las marcas de pel??culas/episodios ya vistos ?[/COLOR][CR]'
    txt += 'S??, su Media Center gestiona autom??ticamente las marcas de visto/no visto.'
    txt += ' Estas marcas est??n en la base de datos de su Media Center pero no en las propias de Balandro.'

    txt += '[CR][CR][COLOR gold]?? Qu?? pasa si un enlace guardado deja de funcionar ?[/COLOR][CR]'
    txt += 'A veces las webs desaparecen o cambian de estructura y/o de enlaces, y eso provoca que en Preferidos dejen de ser v??lidos.'
    txt += ' Al acceder a un enlace que da error, se muestra un di??logo para escoger si se quiere "Buscar en otros canales" o "Volver a buscar en el mismo canal".'
    txt += ' Si la web ha dejado de funcionar deber??s buscar en otros canales, pero si ha sufrido cambios puedes volver a buscar en ella.'

    txt += '[CR][CR][COLOR gold]?? Se puede compartir una lista de Preferidos ?[/COLOR][CR]'
    txt += 'De momento puedes hacerlo manualmente. En la carpeta userdata del addon, dentro de "tracking_dbs" est??n los ficheros [COLOR gold].sqlite[/COLOR] de cada lista que tengas creada.'
    txt += ' Puedes copiar estos ficheros y llevarlos a otros dispositivos.'

    txt += '[CR][CR][COLOR gold]?? C??mo invertir el orden de los episodios ?[/COLOR][CR]'
    txt += 'Por defecto los episodios dentro de una temporada se muestran en orden ascendente, del primero al ??ltimo.'
    txt += ' Si prefieres que sea al rev??s, desde el men?? contextual de una temporada selecciona "Invertir el orden de los episodios" y'
    txt += ' tu preferencia quedar?? guardada para esa temporada.'

    txt += '[CR][CR][COLOR gold]?? Hay alguna l??mitaci??n en los episodios a guardar por cada temporada ?[/COLOR][CR]'
    txt += 'Si, no se almacenar??n m??s de 50 episodios por temporada, si fuera necesario, debe gestionar esa serie y/o temporada'
    txt += ' a trav??s de los "favoritos/videoteca gen??rica" de su Media Center.'

    txt += '[CR][CR][COLOR gold]?? C??mo integrar los Preferidos en la Videoteca de su Media Center? ?[/COLOR][CR]'
    txt += 'Una alternativa es a??adir los Preferidos de Balandro a los "favoritos/videoteca gen??rica" de su Media center.'
    txt += ' o bien, a??adir el contenido de Preferidos de Balandro a la "Videoteca gen??rica" de su Media center, con el addon externo "ADD TO LIB"'

    platformtools.dialog_textviewer('Preferidos y su Funcionamiento', txt)


def show_help_tracking_update(item):
    logger.info()

    txt = '[COLOR gold]?? Qu?? es el servicio de b??squeda de nuevos episodios ?[/COLOR][CR]'
    txt += 'El servicio es un proceso de Balandro que se ejecuta al iniciarse su Media Center, y se encarga de comprobar cuando hay que buscar actualizaciones.'
    txt += ' En la configuraci??n dentro de "Actualizar" puedes indicar cada cuanto tiempo deben hacerse las comprobaciones.'
    txt += ' Por defecto es dos veces al d??a, cada 12 horas, pero puedes cambiarlo.'
    txt += ' Si lo tienes desactivado, puedes ejecutar manualmente la misma b??squeda desde el men?? contextual de "Series" dentro de "Preferidos".'

    txt += '[CR][CR][COLOR gold]?? C??mo se activa la b??squeda de nuevos episodios para series ?[/COLOR][CR]'
    txt += 'Desde el listado de series dentro de "Preferidos" accede a "Gestionar serie" desde el men?? contextual.'
    txt += ' Al seleccionar "Programar b??squeda autom??tica de nuevos episodios" podr??s definir el seguimiento que quieres darle a la serie'
    txt += ' e indicar cada cuanto tiempo hay que hacer la comprobaci??n de si hay nuevos episodios.'

    txt += '[CR][CR][COLOR gold]?? C??mo se combina el servicio con las series ?[/COLOR][CR]'
    txt += 'Cada vez que se ejecuta el servicio (1, 2, 3 o 4 veces por d??a) se buscan las series que tienen activada la b??squeda autom??tica.'
    txt += ' Por cada serie seg??n su propia periodicidad se ejecuta o no la b??squeda.'
    txt += ' Esto permite por ejemplo tener series que s??lo requieren una actualizaci??n por semana, y otras d??nde conviene comprobar cada d??a.'

    txt += '[CR][CR][COLOR gold]?? Por qu?? la b??squeda de nuevos episodios est?? desactivada por defecto ?[/COLOR][CR]'
    txt += 'Es preferible ser prudente con las actualizaciones para no saturar m??s las webs de d??nde se obtiene la informaci??n.'
    txt += ' Por esta raz??n al guardar series por defecto no tienen activada la comprobaci??n de nuevos episodios y hay que indicarlo expl??citamente si se quiere.'
    txt += ' Si por ejemplo sigues una serie ya terminada seguramente no necesitar??s buscar nuevos episodios, en cambio si sigues una serie de un show diario s?? te interesar??.'

    txt += '[CR][CR][COLOR gold]?? D??nde se ven los nuevos episodios encontrados ?[/COLOR][CR]'
    txt += 'En "Preferidos" estar??n dentro de sus series respectivas, pero tambi??n se puede ver un listado de los ??ltimos episodios a??adidos'
    txt += ' por fecha de emisi??n o de actualizaci??n en los canales.'

    platformtools.dialog_textviewer('B??squeda autom??tica de nuevos episodios', txt)


def show_help_proxies(item):
    logger.info()

    txt = '[COLOR gold]?? Por qu?? en algunos canales hay una opci??n para configurar proxies ?[/COLOR][CR]'
    txt += 'Ciertos canales sufren bloqueos por parte de algunos pa??ses/operadoras que no permiten acceder a su contenido.'
    txt += ' Mediante el uso de proxies se puede evitar esa restricci??n.'

    txt += '[CR][CR][COLOR gold]?? En qu?? canales hay que usar los proxies ?[/COLOR][CR]'
    txt += 'Depende de la conexi??n de cada usuario (el pa??s d??nde se conecta, con qu?? operadora, qu?? dns tiene configurados, si usa o no vpn, ...).'
    txt += ' Lo m??s aconsejable es probar primero si funcionan sin necesidad de proxies ya que es lo m??s c??modo y r??pido.'
    txt += ' Aunque un canal tenga la opci??n de proxies no es obligatorio usarlos, hacerlo solamente si es necesario.'

    txt += '[CR][CR][COLOR gold]?? Se pueden descartar los canales que requieren proxies ?[/COLOR][CR]'
    txt += 'S??, desde la opci??n dentro de buscar [COLOR gold]Excluir canales en las b??squedas[/COLOR].'
    txt += 'Tambi??n, desde el listado de canales de pel??culas y/o series, en el men?? contextual se pueden desactivar los canales deseados.'
    txt += ' De esta manera quedar??n descartados para las b??squedas globales, se evitar??n sus mensajes relacionados con los proxies'
    txt += ' y se acelerar?? la b??squeda.'

    txt += '[CR][CR][COLOR gold]?? C??mo se usa la configuraci??n de proxies ?[/COLOR][CR]'
    txt += 'Por defecto en la configuraci??n de Balandro esta activada la opci??n "Buscar proxies automaticamente" ello efectua un barrido de b??squeda de acuerdo con el proveedor informado.'
    txt += '[CR][CR]'
    txt += 'En la configuraci??n de "Proxies" se pueden personalizar (Dejar de buscar si se hallaron suficientes v??lidos, Proveedor de proxies habitual, Limitar la cantidad de v??lidos a memorizar,'
    txt += ' las solicitudes de Anonimidad, Pa??s, etc.)'
    txt += '[CR][CR]'
    txt += 'Una vez finalizado el proceso de b??squeda presentar?? la consola de resultados con varias opciones.'
    txt += '[CR][CR]'
    txt += 'La 1ra opci??n [COLOR gold]Modificar manualmente[/COLOR] sirve por si se quieren escribir los proxies a usar.'
    txt += ' La 2da opci??n [COLOR gold]Buscar nuevos proxies[/COLOR] sirve para realizar una b??squeda de proxies que pueden servir para el canal. Los tres m??s r??pidos entre los v??lidos se guardar??n en la configuraci??n del canal.'
    txt += ' La 3ra opci??n [COLOR gold]Par??metros para buscar[/COLOR] sirve para configurar ciertas opciones para la b??squeda de proxies. Normalmente las opciones por defecto son suficientes pero si fallan se puede probar cambiando alg??n par??metro (la web de d??nde se obtienen, el tipo de proxy, ...).'

    txt += '[CR][CR][COLOR gold]?? Se ralentizan los canales si se utilizan proxies ?[/COLOR][CR]'
    txt += 'S??, acceder a las webs de los canales a trav??s de proxies ralentiza considerablemente lo que tardan en responder.'
    txt += ' A??n as??, hay proxies m??s r??pidos que otros, o m??s estables, o menos saturados, gratu??tos o de pago, etc.'

    txt += '[CR][CR][COLOR gold]?? Por qu?? muchos proxies dejan de funcionar ?[/COLOR][CR]'
    txt += 'Los proxies que se pueden encontrar en la b??squeda son todos gratu??tos pero tienen ciertas limitaciones y no siempre est??n activos.'
    txt += ' Para cada canal se guardan los proxies a utilizar, pero es posible que algunos d??as cuando entres tengas que volver a hacer una b??squeda de proxies porque han dejado de funcionar.'

    platformtools.dialog_textviewer('Utilizaci??n de proxies', txt)


def show_version(item):
    logger.info()

    txt = ''
    try:
       with open(os.path.join(config.get_runtime_path(), 'version.txt'), 'r') as f: txt=f.read(); f.close()
    except:
        try:
            txt = open(os.path.join(config.get_runtime_path(), 'version.txt'), encoding="utf8").read()
        except: pass

    if txt:
       platformtools.dialog_textviewer('Informaci??n versi??n', txt)

def show_changelog(item):
    logger.info()

    txt = ''
    try:
       with open(os.path.join(config.get_runtime_path(), 'changelog.txt'), 'r') as f: txt=f.read(); f.close()
    except:
        try:
            txt = open(os.path.join(config.get_runtime_path(), 'changelog.txt'), encoding="utf8").read()
        except: pass

    if txt:
       platformtools.dialog_textviewer('Historial de cambios', txt)

def show_dev_notes(item):
    logger.info()

    txt = ''
    try:
       with open(os.path.join(config.get_runtime_path(), 'dev-notes.txt'), 'r') as f: txt=f.read(); f.close()
    except:
        try:
            txt = open(os.path.join(config.get_runtime_path(), 'dev-notes.txt'), encoding="utf8").read()
        except: pass

    if txt:
       platformtools.dialog_textviewer('Notas para developers', txt)

def show_log(item):
    logger.info()

    loglevel = config.get_setting('debug', 0)
    if not loglevel >= 2:
        if not platformtools.dialog_yesno(config.__addon_name, 'El nivel actual de informaci??n del fichero LOG de su Media Center NO esta configurado al m??ximo. ?? Desea no obstante visualizarlo ?'): 
            return

    path = translatePath(os.path.join('special://logpath/', ''))

    file_log = 'kodi.log'

    file = path + file_log

    existe = filetools.exists(file)

    if existe == False:
        files = filetools.listdir(path)
        for file_log in files:
            if file_log.endswith('.log') == True:
                file = path + file_log
                existe = filetools.exists(file)
                break

    if existe == False:
        platformtools.dialog_notification(config.__addon_name, '[B][COLOR %s]No se localiza su fichero Log[/COLOR][/B]' % color_alert)
        return

    size = filetools.getsize(file)
    if size > 999999:
        platformtools.dialog_notification(config.__addon_name, '[B][COLOR %s]Cargando fichero log[/COLOR][/B]' % color_infor)

    txt = ''
    try:
        with open(os.path.join(path, file_log), 'r') as f: txt=f.read(); f.close()
    except:
        try:
            txt = open(os.path.join(path, file_log), encoding="utf8").read()
        except: pass

    if txt:
        platformtools.dialog_textviewer('Fichero LOG de su Media Center', txt)


def copy_log(item):
    logger.info()

    loglevel = config.get_setting('debug', 0)
    if not loglevel >= 2:
        if not platformtools.dialog_yesno(config.__addon_name, 'El nivel actual de informaci??n del fichero LOG de su Media Center NO esta configurado al m??ximo. [B][COLOR %s]?? Desea no obstante obtener una copia ?[/B][/COLOR]' % color_infor):
            return

    path = translatePath(os.path.join('special://logpath/', ''))

    file_log = 'kodi.log'

    file = path + file_log

    existe = filetools.exists(file)

    if existe == False:
        files = filetools.listdir(path)
        for file_log in files:
            if file_log.endswith('.log') == True:
                file = path + file_log
                existe = filetools.exists(file)
                break

    if existe == False:
        platformtools.dialog_notification(config.__addon_name, '[B][COLOR %s]No se localiza su fichero Log[/COLOR][/B]' % color_alert)
        return

    destino_path = xbmcgui.Dialog().browseSingle(3, 'Seleccionar carpeta d??nde copiar', 'files', '', False, False, '')
    if not destino_path: return

    origen = os.path.join(path, file_log)
    destino = filetools.join(destino_path, file_log)
    if not filetools.copy(origen, destino, silent=False):
        platformtools.dialog_ok(config.__addon_name, 'Error, no se ha podido copiar el fichero Log!', origen, destino)
        return

    platformtools.dialog_notification('Fichero Log copiado', file_log)

    time.sleep(0.5)

    loglevel = config.get_setting('debug', 0)
    if not loglevel == 0:
        if not platformtools.dialog_yesno(config.__addon_name, 'La configuraci??n actual del nivel de informaci??n del fichero LOG de su Media Center REDUCE el rendimiento de su equipo. [B][COLOR %s]?? Desea mantener ese Nivel de informaci??n ?[/B][/COLOR]' % color_avis):
            config.set_setting('debug', '0')

def show_advs(item):
    logger.info()

    path = translatePath(os.path.join('special://home/userdata', ''))

    file_advs = 'advancedsettings.xml'

    file = path + file_advs

    existe = filetools.exists(file)

    if existe == False:
        platformtools.dialog_notification(config.__addon_name, '[B][COLOR %s]No hay fichero Advancedsettings[/COLOR][/B]' % color_infor)
        return

    txt = ''
    try:
       with open(os.path.join(path, file_advs), 'r') as f: txt=f.read(); f.close()
    except:
        try:
            txt = open(os.path.join(path, file_advs), encoding="utf8").read()
        except: pass

    if txt:
       platformtools.dialog_textviewer('Su fichero Advancedsettings de su Media Center', txt)


def show_help_adults(item):
    logger.info()

    txt = '*) Las webs podrian, en alg??n caso, publicar V??deos con contenido [COLOR gold]No Apto[/COLOR] para menores.'
    txt += ' Balandro cuenta con un apartado en su configuraci??n exclusivo para el [COLOR gold]Control Parental[/COLOR].'
    txt += ' (por defecto este apartado est?? [COLOR gold]Habilitado[/COLOR]).'

    txt += '[CR][CR]'
    txt += '*) Pero no se puede garantizar que todo el material de este tipo se filtre correctamente en determinadas ocasiones.'

    platformtools.dialog_textviewer('Control Parental', txt)


def show_help_torrents(item):
    logger.info()

    txt = '*) A trav??s de un navegador web localize e instale al menos uno de los add-ons de la lista que m??s se adapte a'
    txt += '  sus necesidades y que sea a su vez compatible con su Media Center.'

    txt += '[CR][CR]'
    txt += '*) Add-Ons:[CR]'
    txt += '    - plugin.video.quasar[CR]'
    txt += '    - plugin.video.elementum[CR]'
    txt += '    - plugin.video.torrenter[CR]'
    txt += '    - plugin.video.torrentin[CR]'
    txt += '    - plugin.video.torrest[CR]'
    txt += '    - plugin.video.pulsar[CR]'
    txt += '    - plugin.video.stream[CR]'
    txt += '    - plugin.video.xbmctorrent'

    txt += '[CR][CR]'
    txt += '*) A modo de ejemplo para [COLOR gold]Elementum[/COLOR] puede acceder a su web oficial en "elementum.surge.sh"'

    txt += '[CR][CR]'
    txt += '*) Existen m??ltiples sitios webs en donde puede localizar estos add-ons, entre estos sitios le recomendamos'
    txt += '   acceda a este [COLOR gold]fuentekodileia.github.io[/COLOR]'

    platformtools.dialog_textviewer('?? D??nde obtener los add-ons para torrents ?', txt)


def show_legalidad(item):
    logger.info()

    txt = '*)[COLOR yellow][B] Balandro [COLOR moccasin][B] Es Totalmente [I] GRATUITO [/I], si Pag?? Por Este Add-On le [I] ENGA??ARON [/I][/B][/COLOR]'
    txt += '[COLOR lightblue][B] y Tiene Como Objeto, Permitir Visualizar Pel??culas, Series y Documentales, etc... [/B][/COLOR]'
    txt += '[COLOR lightblue][B] Todo a Trav??s de Internet y Directamente Desde su Sistema Media Center. [/B][/COLOR]'

    txt += '[CR][CR][COLOR orchid][B] Este Add-On es Tan Solo un Mero Ejercicio de Aprendizaje Del Lenguaje de Programaci??n Python y se Distribuye Sin Ning??n Contenido Multimedia Adjunto al Mismo [/B][/COLOR]'
    txt += '[COLOR lightgrey][B][I] En Consecuencia Solo Las Webs Son Plenamente Responsables de Los Contenidos Que Publiquen [/I][/B][/COLOR]'

    txt += '[CR][CR][COLOR tan][B] ??selo de Acuerdo Con su Criterio y Bajo su Responsabilidad [/B][/COLOR]'
    txt += '[COLOR tan][B] Sus  Creadores Quedar??n Totalmente Eximidos de Toda Repercusi??n Legal, si se Re-Distribuye Solo o Con Acceso a Contenidos Protegidos Por Los Derechos de Autor, Sin el Permiso Explicito de Los Mismos[/B][/COLOR]'

    txt += '[CR][CR]*)[COLOR chocolate][B][I] Si Este Tipo de Contenido Est?? Prohibido en su Pa??s, Solamente Usted Ser?? el Responsable de su Uso [/I][/B][/COLOR] '

    txt += '[CR][CR]*)[COLOR mediumaquamarine][B] Este Add-On es un Proyecto Sin ??nimo de Lucro y Con Fines Educativos, Por lo Tanto Est?? Prohibida su Venta en Solitario o Como Parte de Software Integrado en Cualquier Dispositivo, es Exclusivamente Para un Uso Docente y Personal [/B][/COLOR] '

    txt += '[CR][CR]*)[COLOR red][B][I] Queda Totalmente Prohibida su Re-Distribuci??n, Sin la Autorizaci??n Fehaciente de Sus Creadores [/I][/B][/COLOR] '

    platformtools.dialog_textviewer('Cuestiones Legales', txt)


def show_license(item):
    logger.info()

    txt = ''
    try:
       with open(os.path.join(config.get_runtime_path(), 'LICENSE'), 'r') as f: txt=f.read(); f.close()
    except:
        try:
            txt = open(os.path.join(config.get_runtime_path(), 'LICENSE'), encoding="utf8").read()
        except: pass

    if txt:
       platformtools.dialog_textviewer('Licencia (Gnu Gpl v3)', txt)


def show_test(item):
    from core import httptools, channeltools, scrapertools

    platformtools.dialog_notification(config.__addon_name, '[B][COLOR %s]Cargando informaci??n sistema[/B][/COLOR]' % color_infor)

    your_ip = ''

    try:
       import re
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
	    platformtools.dialog_ok(config.__addon_name, '[COLOR red]Parece que NO hay conexi??n con internet.[/COLOR]', 'Compruebelo realizando cualquier B??squeda, desde un Navegador Web ')

    hay_repo = False
    if xbmc.getCondVisibility('System.HasAddon("%s")' % 'repository.balandro'): hay_repo = True

    access_repo = False
    tex_access_repo = ''
    if hay_repo:
        try:
           data = httptools.downloadpage(ADDON_REPO_ADDONS).data
           if data: access_repo = True
        except:
           tex_access_repo = '[COLOR lightblue][B]No se pudo comprobar[/B][/COLOR]'

    last_ver = ''
    access_last_ver = False
    if hay_repo:
        if access_repo:
            last_ver = scrapertools.find_single_match(data, 'name="' + config.__addon_name + '.*?version="(.*?)"')
            if last_ver: access_last_ver = True

    access_fixes = False
    tex_access_fixes = ''
    if hay_repo:
        if access_repo:
            try:
               data = httptools.downloadpage(ADDON_UPDATES_JSON).data
               if data:
                   access_fixes = True
                   if 'addon_version' not in data or 'fix_version' not in data:
                       access_fixes = None
            except:
               tex_access_fixes = '[COLOR lightblue][B]No se pudo comprobar[/B][/COLOR]'


    txt = '[CR][CR][COLOR fuchsia]Balandro[/COLOR][CR]'

    if not your_ip:
        your_ip = '[COLOR red][B] Sin Conexi??n [/B][/COLOR]'

    txt += '- [COLOR gold]Conexi??n internet:[/COLOR]  %s ' % your_ip
    txt += '[CR][CR]'

    tex_repo = ' Instalado'
    if hay_repo == False: tex_repo = '[COLOR red][B] No instalado, No recibir?? m??s versiones [/B][/COLOR]'


    txt += '- [COLOR gold]Repositorio:[/COLOR]  %s ' % tex_repo
    txt += '[CR][CR]'
    tex_access_repo = ' Accesible'
    if access_repo == False:
        if tex_access_repo == '':
            tex_access_repo = '[COLOR red][B] Sin conexi??n, No accesible [/B][/COLOR]'

    txt += '- [COLOR gold]Conexi??n con repositorio:[/COLOR]  %s ' % tex_access_repo
    txt += '[CR][CR]'

    if access_last_ver:
        tex_access_last_ver = '  ' + last_ver
    else: tex_access_last_ver = '[COLOR red][B] ??ltima versi??n, No accesible [/B][/COLOR]'

    txt += '- [COLOR gold]??ltima versi??n:[/COLOR]  %s ' % tex_access_last_ver
    txt += '[CR][CR]'

    if not tex_access_fixes:
        tex_access_fixes = ' Accesibles'
        if access_fixes == None: tex_access_fixes = '[COLOR yellow] Sin actualizaciones tipo Fix pendientes [/COLOR]'
        elif access_fixes == False: tex_access_fixes = '[COLOR red][B] Fixes sobre ??ltima versi??n, No accesibles [/B][/COLOR]'

    txt += '- [COLOR gold]Fixes sobre ??ltima versi??n:[/COLOR]  %s ' % tex_access_fixes
    txt += '[CR][CR]'

    txt += '- [COLOR gold]Versi??n instalada:[/COLOR]  [COLOR yellow][B]%s[/B][/COLOR]' % config.get_addon_version()
    txt += '[CR][CR]'

    folder_down = config.get_setting('downloadpath', default='')
    if not folder_down == '':
        txt += '- [COLOR gold]Carpeta descargas:[/COLOR]  [COLOR moccasin]%s[/COLOR]' % folder_down
        txt += '[CR][CR]'

    tex_dom = ''
    cinecalidad_dominio = config.get_setting('channel_cinecalidad_dominio', default='')
    if not cinecalidad_dominio == '': tex_dom = tex_dom + cinecalidad_dominio + '  '

    hdfull_dominio = config.get_setting('channel_hdfull_dominio', default='')
    if not hdfull_dominio == '': tex_dom = tex_dom + hdfull_dominio

    if tex_dom:
        txt += '- [COLOR gold]Dominios:[/COLOR]  [COLOR springgreen]%s[/COLOR]' %  str(tex_dom).replace('https://', '').replace('/', '')
        txt += '[CR][CR]'

    filtros = {'searchable': True}
    opciones = []

    ch_list = channeltools.get_channels_list(filtros=filtros)

    if ch_list:
       txt_ch = ''

       for ch in ch_list:
           cfg_proxies_channel = 'channel_' + ch['id'] + '_proxies'
           cfg_proxytools_max_channel = 'channel_' + ch['id'] + '_proxytools_max'

           if not config.get_setting(cfg_proxies_channel, default=''):
               if not config.get_setting(cfg_proxytools_max_channel, default=''):
                   continue

           txt_ch += '[COLOR red]%s[/COLOR]  ' % ch['name']

       if not txt_ch: txt_ch = 'No hay canales con proxies' 
       txt += '- [COLOR gold]Proxies:[/COLOR]  %s' %  str(txt_ch)

    cliente_torrent = config.get_setting('cliente_torrent', default='Ninguno')
    if cliente_torrent == 'Ninguno': tex_tor = '[COLOR moccasin]Ninguno[/COLOR]'
    elif cliente_torrent == 'Seleccionar':  tex_tor = 'Seleccionar'
    else:
      tex_tor = cliente_torrent
      cliente_torrent = 'plugin.video.' + cliente_torrent.lower()
      if xbmc.getCondVisibility('System.HasAddon("%s")' % cliente_torrent):
          tex_tor += '  Instalado'
      else:
          tex_tor += '  [COLOR red][B]No instalado[/B][/COLOR]'

    txt += '[CR][CR]- [COLOR gold]Motor torrent:[/COLOR]  %s' % tex_tor

    if xbmc.getCondVisibility('System.HasAddon("plugin.video.youtube")'):
        tex_yt = '  Instalado'
    else:
        tex_yt = '  [COLOR red][B]No instalado[/B][/COLOR]'

    txt += '[CR][CR]- [COLOR gold]Youtube addon:[/COLOR]  %s' % tex_yt

    if xbmc.getCondVisibility('System.HasAddon("script.module.resolveurl")'):
        tex_yt = '  Instalado'
    else:
        tex_yt = '  [COLOR red][B]No instalado[/B][/COLOR]'

    txt += '[CR][CR]- [COLOR gold]ResolveUrl script:[/COLOR]  %s' % tex_yt

    loglevel = config.get_setting('debug', 0)
    if loglevel == 0: tex_niv = 'Solo Errores'
    elif loglevel == 1: tex_niv = 'Errores e Informaci??n'
    else: tex_niv = 'M??xima Informaci??n'

    txt += '[CR][CR]- [COLOR gold]Log:[/COLOR]  %s' % tex_niv

    txt += '[CR][CR][COLOR fuchsia]Entorno[/COLOR][CR]'

    txt += '- [COLOR gold]Media center:[/COLOR]  [COLOR coral]%s[/COLOR]' % str(xbmc.getInfoLabel('System.BuildVersion'))
    txt += '[CR][CR]'

    plataforma = platform.uname()

    txt += '- [COLOR gold]Sistema:[/COLOR]  %s-%s-%s' %  (str(plataforma[0]), str(plataforma[2]), str(plataforma[3]))
    txt += '[CR][CR]'

    txt += '- [COLOR gold]Python:[/COLOR]  %s.%s.%s' % (str(sys.version_info[0]), str(sys.version_info[1]), str(sys.version_info[2]))
    txt += '[CR][CR]'

    if last_ver:
        if not config.get_addon_version() == last_ver:
            platformtools.dialog_ok(config.__addon_name, 'Versi??n instalada[COLOR coral][B] ' + config.get_addon_version() + '[/B][/COLOR]', '??ltima Versi??n disponible [COLOR yellow][B] ' + last_ver + '[/B][/COLOR]')

    platformtools.dialog_textviewer('Test status sistema', txt)


def show_last_fix(item):
    logger.info()

    path = os.path.join(config.get_runtime_path(), 'last_fix.json')

    existe = filetools.exists(path)
    if existe == False:
        platformtools.dialog_notification(config.__addon_name, '[B][COLOR %s]No hay fichero Fix[/COLOR][/B]' % color_infor)
        return

    txt = ''
    try:
       with open(path, 'r') as f: txt=f.read(); f.close()
    except:
        try:
            txt = open(path, encoding="utf8").read()
        except: pass

    if txt:
       txt = txt.replace('{', '').replace('}', '').replace('[', '').replace(']', '').replace(',', '').replace('"', '').replace("'", '').strip()
       platformtools.dialog_textviewer('Informaci??n del ??ltimo Fix instalado', txt)


def show_sets(item):
    logger.info()

    file_sets = os.path.join(config.get_data_path(), "settings.xml")

    existe = filetools.exists(file_sets)

    if existe == False:
        platformtools.dialog_notification(config.__addon_name, '[B][COLOR %s]No existe settings.xml[/COLOR][/B]' % color_alert)
        return

    txt = ''
    try:
       with open(os.path.join(file_sets), 'r') as f: txt=f.read(); f.close()
    except:
        try:
            txt = open(os.path.join(file_sets), encoding="utf8").read()
        except: pass

    if txt:
       platformtools.dialog_textviewer('Su fichero de Ajustes personalizados', txt)

def show_cook(item):
    logger.info()

    file_cook = os.path.join(config.get_data_path(), "cookies.dat")

    existe = filetools.exists(file_cook)

    if existe == False:
        platformtools.dialog_notification(config.__addon_name, '[B][COLOR %s]No existe cookies.dat[/COLOR][/B]' % color_adver)
        return

    txt = ''
    try:
       with open(os.path.join(file_cook), 'r') as f: txt=f.read(); f.close()
    except:
        try:
            txt = open(os.path.join(file_cook), encoding="utf8").read()
        except: pass

    if txt:
       platformtools.dialog_textviewer('Su fichero de Cookies', txt)
