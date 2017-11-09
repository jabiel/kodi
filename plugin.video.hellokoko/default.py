# -*- coding: utf-8 -*-
import re, os, time, sys
import urllib, urllib2, urlparse
import xbmcplugin, xbmcgui, xbmcaddon
from resources.lib import kokolib


addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
addon_handle = int(sys.argv[1])
sysaddon = sys.argv[0]
xbmcplugin.setContent(addon_handle, 'movies')
cookieFile = 'koko.cookie'

line1 = "Hello swiecei!"
line2 = "Tu mowi Jaroslaw"
line3 = "Z kodiego"

baseUrl = 'http://kokosik1207.pl'

mainMenu = [
             ["[COLOR=blue]Ostatnio dodane[/COLOR]",'/newposts/',"FilmList"],
             ["Seriale",'/seriale/',"FilmList"],
			 ["Gatunek",'g',"SubCategory"],
			 ["Wersja",'w',"SubCategory"],
			 ["Rok",'r',"SubCategory"],
             ["Narzedzia","0","Tools"]
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

def addMenu(name,url,mode,folder,contextmenu='',info='',icon='',content='',premium='',isPlayable = False, param1='',param2='',param3=''):
    u=sysaddon+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&icon="+urllib.quote_plus(icon)+"&content="+content+"&premium="+premium+"&param1="+urllib.quote_plus(param1)+"&param2="+urllib.quote_plus(param2)+"&param3="+urllib.quote_plus(param3)
    
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=icon)
    liz.setInfo( type="video", infoLabels = info )
    if isPlayable:
        liz.setProperty('IsPlayable', 'True')
    if contextmenu:
        liz.addContextMenuItems(contextmenu)
    ok=xbmcplugin.addDirectoryItem(handle=addon_handle,url=u,listitem=liz,isFolder=folder)
    return ok

def buildMenu(menuList):
    for i in menuList:
        addMenu(i[0],i[1],i[2],True)
    #addMenu('[COLOR=green]Szukaj[/COLOR]','0','Search',True)

def subCategory(url):
	if(url == 'g'):
		buildMenu(gatMenu)
	if(url == 'w'):
		buildMenu(werMenu)
	if(url == 'r'):
		buildMenu(rokMenu)
	xbmcplugin.endOfDirectory(addon_handle)

def filmList(url):
	movieList = kokolib.getTitleList(baseUrl + url)
	for mm in movieList:
		addMenu(mm[1],mm[0],'MovieDetails',True)
		
	xbmcplugin.endOfDirectory(addon_handle)
	
	#def play(stream_url):
#	play_item = xbmcgui.ListItem(path=stream_url)
#	play_item.setProperty('IsPlayable','true')
#	xbmcplugin.setResolvedUrl(addon_handle, True, listitem=play_item)

# play2 dziala
def play2(stream_url):
	listitem = xbmcgui.ListItem("play2")
	xbmc.Player().play(stream_url, listitem)

def findAndPlayStream(url):
	movieUrl = kokolib.findMovieUrl(url)	
	if movieUrl[0]:
		play2(movieUrl[1])
	else:
		xbmcgui.Dialog().ok(addonname, movieUrl[1])  
#
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
	html = kokolib.httpRequest(query_data, loginData)
	loggedin = isLoggedin(html)
	xbmcgui.Dialog().ok(addonname, 'Podane login lub haslo sa nieprawidlowe', addon.getSetting('kokosik.user') + ":" + addon.getSetting('kokosik.pass'))  
	return loggedin
	

def movieDetails(url):
	query_data2 = { 'url': url, 'use_cookie': True, 'cookiefile': cookieFile, 'save_cookie': False, 'load_cookie': True, 'return_data': True }
	html = kokolib.httpRequest(query_data2)
	loggedin = isLoggedin(html)
	if(not loggedin):
		checkHasCredentials()
		loggedin = login()
		if(loggedin):
			html = kokolib.httpRequest(query_data2)
		
	lst = kokolib.listVideoProviders(html)
	for z in lst:
		addMenu(z[0] + " " + z[1] + " "+ z[2],z[3],'FindAndPlay',True)
		
	xbmcplugin.endOfDirectory(addon_handle)
	

		
## MAIN LOOP
params = dict(urlparse.parse_qsl(sys.argv[2].replace('?','')))

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
		filmList(url)
elif mode=='MovieDetails':
		movieDetails(url)
elif mode=='FindAndPlay':
		findAndPlayStream(url)
		#xbmcgui.Dialog().ok(addonname, mode, url, line3)
elif mode=='SubCategory':
		subCategory(url)
elif mode=='Tools':
        toolsMenu()
		