# -*- coding: utf-8 -*-
import re, os, time, sys
import urllib, urllib2, urlparse
import xbmcplugin, xbmcgui, xbmcaddon
from resources.lib import kokolib, hellotools


addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
addon_handle = int(sys.argv[1])
sysaddon = sys.argv[0]
xbmcplugin.setContent(addon_handle, 'movies')
COOKIEPATH  = unicode(addon.getAddonInfo('path') + os.path.sep + "cookies",'utf-8')
cookieFile = COOKIEPATH + os.path.sep + 'koko.cookie'

baseUrl = 'http://kokosik1207.pl'

mainMenu = [
             ["[COLOR=blue]Ostatnio dodane[/COLOR]",'/newposts/',"FilmList"],
             ["Seriale",'/seriale/',"FilmList"],
             ["Kolekcje filmowe",'/kolekcje-filmowe',"FilmList"],
             ["Filmy na prosbe",'/filmy-na-prosbe',"FilmList"],
			 ["Gatunek",'g',"SubCategory"],
			 ["Wersja",'w',"SubCategory"],
			 ["Rok",'r',"SubCategory"],
			 ["[COLOR=green]Szukaj[/COLOR]","0","Search"]
            ]
			
gatMenu = [
             ["Akcja",'/akcja',"FilmList"],
			 ["Animowane",'/animowane',"FilmList"],
			 ["Biograficzne",'/biograficzne',"FilmList"],
			 ["Dokumentalne",'/dokument',"FilmList"],
             ["Dramat","/dramat","FilmList"],
			 ["Familijny","/familijny","FilmList"],
			 ["Fantasy","/fantasy","FilmList"],
			 ["Historyczny","/historyczny","FilmList"],
			 ["Horror","/horror","FilmList"],
			 ["Katastroficzny","/katastroficzny","FilmList"],
			 ["Komedia","/komedia","FilmList"],
			 ["Kryminal","/kryminal","FilmList"],
			 ["Przygodowy","/przygodowy","FilmList"],
			 ["Psychologiczny","/psychologiczny","FilmList"],
			 ["Romans","/romans","FilmList"],
			 ["Sci-Fi","/sci-fi","FilmList"],
			 ["Sensacyjny","/sensacyjny","FilmList"],
			 ["Thriller","/thriller","FilmList"],
			 ["Western","/western","FilmList"]
            ]

werMenu = [
             ["Film polski",'/xfsearch/polski',"FilmList"],
			 ["Napisy PL",'/xfsearch/napisy+pl',"FilmList"],
			 ["Lektor PL",'/xfsearch/lektor+pl',"FilmList"],
			 ["Lektor amatorski",'/xfsearch/lektor+amatorski',"FilmList"],
			 ["Dubbing PL",'/xfsearch/dubbing',"FilmList"],
			 ["Inne",'/xfsearch/inne',"FilmList"]
            ]

rokMenu = [
             ["2017",'/xfsearch/2017',"FilmList"],
			 ["2016",'/xfsearch/2016',"FilmList"],
			 ["2015",'/xfsearch/2015',"FilmList"],
			 ["2014",'/xfsearch/2014',"FilmList"],
             ["2013","/xfsearch/2013","FilmList"],
             ["2012","/xfsearch/2012","FilmList"],
             ["2011","/xfsearch/2011","FilmList"],
			 ["2010","/xfsearch/2010","FilmList"]
            ]

def addMenu(name,url,mode,folder,contextmenu='',info='',icon='',isPlayable = False, img = ''):    
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=icon)
    liz.setInfo( type="video", infoLabels = info )
    if img:
        liz.setArt({ "poster": img  }) # "fanart": "https://image.tmdb.org/t/p/w185/weUSwMdQIa3NaXVzwUoIIcAi85d.jpg"
    if isPlayable:
        liz.setProperty('IsPlayable', 'True')
    if contextmenu:
        liz.addContextMenuItems(contextmenu)

    u=sysaddon+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&icon="+urllib.quote_plus(icon)+"&content="
    ok=xbmcplugin.addDirectoryItem(handle=addon_handle,url=u,listitem=liz,isFolder=folder)
    return ok

def buildMenu(menuList):
    for i in menuList:
        addMenu(i[0],i[1],i[2],True)
    
def subCategory(url):
	if(url == 'g'):
		buildMenu(gatMenu)
	if(url == 'w'):
		buildMenu(werMenu)
	if(url == 'r'):
		buildMenu(rokMenu)
	xbmcplugin.endOfDirectory(addon_handle)

def filmList(url):
    html = hellotools.httpRequest({ 'url':url,  'use_cookie': True, 'cookiefile': cookieFile, 'save_cookie': False, 'load_cookie': True, 'return_data': True })
    movieList = kokolib.getTitleList(html)
    pageing = kokolib.getNextPage(html)
    for mm in movieList:
        info = { "genre":mm[2], "plot": "[COLOR=blue]" + mm[2] + "[/COLOR]. " + mm[3], "title": mm[1] }
        addMenu(mm[1],mm[0],'MovieDetails',True, '', info, '', False, mm[4])

    if pageing:
        addMenu('[COLOR=blue]> Następna strona >[/COLOR] ' + pageing[1], pageing[0],'FilmList', True, '', {"plot":pageing[0]})

    xbmcplugin.endOfDirectory(addon_handle)

# play2 dziala
def play2(stream_url):
	listitem = xbmcgui.ListItem("play2")
	xbmc.Player().play(stream_url, listitem)

# uses urlresolver - but urlresolver is shitty
#def findAndPlayStream(url):
#	try:
#		import urlresolver
#		movieUrl = urlresolver.resolve(url)
#		if isinstance(movieUrl, basestring):
#			play2(movieUrl)
#		else:
#			xbmcgui.Dialog().ok(addonname, 'Brak filmu', 'Info: %s' % movieUrl) 
#	except urlresolver.resolver.ResolverError as e:
#		xbmcgui.Dialog().ok(addonname, 'ResolverError: %s' % e) 
#	except:
#		xbmcgui.Dialog().ok(addonname, 'KokoError: %s' % str(sys.exc_info()[0]), str(sys.exc_info()[1]), str(sys.exc_info()[2])) #traceback.format_exc()
	
def findAndPlayStream(url):
	movieUrl = kokolib.findMovieUrl(url)	
	if movieUrl[0]:
		play2(movieUrl[1])
	else:
		xbmcgui.Dialog().ok(addonname, movieUrl[1])  

def checkHasCredentials():
	if not addon.getSetting('kokosik.user') or not addon.getSetting('kokosik.pass'):
		xbmcgui.Dialog().ok(addonname, 'Zaloguj sie', 'Aby ogladac filmy musisz byc zalogowany')  
		addon.openSettings()
		return False
	return True

def isLoggedin(html):
	return html.find('index.php?action=logout') > 0
	
def login():
	query_data = { 'url': 'http://kokosik1207.pl/', 'use_cookie': True, 'cookiefile': cookieFile, 'save_cookie': True, 'load_cookie': False, 'use_post': True, 'return_data': True }
	loginData   = { 'login_name': addon.getSetting('kokosik.user'), 'login_password': addon.getSetting('kokosik.pass'), 'login':'submit' }
	html = hellotools.httpRequest(query_data, loginData)
	loggedin = isLoggedin(html)
	xbmcgui.Dialog().ok(addonname, 'Podane login lub haslo sa nieprawidlowe', addon.getSetting('kokosik.user') + ":" + addon.getSetting('kokosik.pass'))  
	return loggedin
	

def movieDetails(url):
	query_data2 = { 'url': url, 'use_cookie': True, 'cookiefile': cookieFile, 'save_cookie': False, 'load_cookie': True, 'return_data': True }
	html = hellotools.httpRequest(query_data2)
	loggedin = isLoggedin(html)
	if(not loggedin):
		checkHasCredentials()
		loggedin = login()
		if(loggedin):
			html = kokolib.httpRequest(query_data2)
		
	lst = kokolib.listVideoProviders(html)
	movie = kokolib.getTitleList(html)[0]
	for z in lst:
		info = { "plot":str(movie[1]) + "\n" + movie[3] + "\n\n" + z[3], "title":movie[1], "rating":"4" }
		addMenu(z[0] + " " + z[1] + " "+ z[2],z[3],'FindAndPlay', True, '', info, '', False, movie[4])
		
	xbmcplugin.endOfDirectory(addon_handle)

def inputSearchText(text=''):
	textnew = None
	kb = xbmc.Keyboard(text)
	kb.doModal()
	if (kb.isConfirmed()):
		textnew = kb.getText()
	return textnew

def search(key):
    query_data = { 'url': 'http://kokosik1207.pl/', 'use_cookie': True, 'cookiefile': cookieFile, 'save_cookie': False, 'load_cookie': True, 'use_post': True, 'return_data': True }
    postData   = { 'do': 'search', 'subaction':'search', 'story':key, 'x':'0', 'y':'0' }
    html = hellotools.httpRequest(query_data, postData)
    data = kokolib.parseSearchHtml(html)

    for mm in data:
        info = { "genre":mm[1], "plot": "[COLOR=blue]" + mm[1] + "[/COLOR]. " + mm[3], "title": mm[0] }
        addMenu(mm[0],mm[2],'MovieDetails',True, '', info)

    #pageing = kokolib.getNextPage(html)
    #if pageing:
    #    addMenu('[COLOR=blue]> Następna strona >[/COLOR] ' + pageing[1], pageing[0],'FilmList', True, '', {"plot":pageing[0]})

    xbmcplugin.endOfDirectory(addon_handle)

		
## MAIN LOOP
params = dict(urlparse.parse_qsl(sys.argv[2].replace('?','')))

if not os.path.isdir(COOKIEPATH):
	os.mkdir(COOKIEPATH)

url = params.get('url') or None
name = params.get('name') or None
mode = params.get('mode') or None
content = params.get('content') or ''
icon = params.get('icon') or None
premium = params.get('premium') or ''
param1 = params.get('param1') or None
param2 = params.get('param2') or None
param3 = params.get('param3') or None
######################################

if mode==None:
        buildMenu(mainMenu)
        xbmcplugin.endOfDirectory(addon_handle)
        checkHasCredentials()
elif mode=='FilmList':
        if 'http' not in url:
            url = baseUrl + url
        filmList(url)
elif mode=='MovieDetails':
		movieDetails(url)
elif mode=='FindAndPlay':
		findAndPlayStream(url)
elif mode=='SubCategory':
		subCategory(url)
elif mode=='Tools':
        toolsMenu()
elif mode=='Search':
        key = inputSearchText()
        if key:            
            search(key)
            #key=repPolChars(key)
            #addHistoryItem(my_addon_name, key)
            #xbmc.executebuiltin('Container.Refresh')
elif mode=='SearchFromList':
        searchFromList(url)
