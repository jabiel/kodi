# -*- coding: utf-8 -*-
import re, os.path
import urllib, urllib2, urlparse, cookielib
import string
from resources.lib import aadecode

rot13 = string.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

quality_arr = {
    '0': '360p',
    '1': '480p',
    '2': '720p',
    '3': '1080p'
}

lang_arr = {
    '0': 'Lektor PL',
    '1': 'Lektor amatorski',
    '2': 'Napisy PL',
    '3': 'Polski',
    '4': 'Dubbing',
    '5': 'ENG',
    '6': 'IVO',
    '7': 'Napisy PL / Lektor PL',
    '8': 'Napisy PL / Lektor IVO',
    '9': 'Napisy PL / Dubbing',
    '10': 'Lektor PL / Dubbing',
    '11': 'Dubbing KINO',
    '12': 'Inne'
}

def removeDuplicates(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def webRequestString(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0')

        try:
            response = urllib2.urlopen(req)
            link=response.read()
            response.close()
        except:
            link=''
        return link

def repPolChars(txt):
        txt = txt.replace('\xc4\x85','a').replace('\xc4\x84','A')
        txt = txt.replace('\xc4\x87','c').replace('\xc4\x86','C')
        txt = txt.replace('\xc4\x99','e').replace('\xc4\x98','E')
        txt = txt.replace('\xc5\x82','l').replace('\xc5\x81','L')
        txt = txt.replace('\xc5\x84','n').replace('\xc5\x83','N')
        txt = txt.replace('\xc3\xb3','o').replace('\xc3\x93','O')
        txt = txt.replace('\xc5\x9b','s').replace('\xc5\x9a','S')
        txt = txt.replace('\xc5\xba','z').replace('\xc5\xb9','Z')
        txt = txt.replace('\xc5\xbc','z').replace('\xc5\xbb','Z')
        return txt

# publics
# getTitleList returns list of movies from given url
def getTitleList(url):
	html = webRequestString(url)
	html = repPolChars(html)
	list2 = re.compile('news-title"><a href="(.*?)">(.*?)<').findall(html)
	list3 = removeDuplicates(list2)
	return list3

# decrypts kokosik urls with movies
def decryptDefalc13(dec13):
	decList = dec13.split("^%^")
	result = list()
	for dec in decList:
		pp = dec.split("^$")
		if(isinstance(pp, list) and len(pp)>2 and len(pp[3]) > 2):
			url = "http" + string.translate(pp[3], rot13).replace('%@%', '://')
			tup1 = (pp[0], lang_arr[pp[1]], quality_arr[pp[2]], url)
			result.append(tup1)
	return result

def listVideoProviders(html):
	#query_data2 = { 'url': url, 'use_cookie': True, 'cookiefile': 'koko.cookie', 'save_cookie': False, 'load_cookie': True, 'return_data': True }
	#html = httpRequest(query_data2)
	
	list2 = re.compile('defalc13="(.*?)"').findall(html)
	return decryptDefalc13(list2[0])



dbg = True

def httpRequest(params = {}, post_data = None):

	#print('params=',params)
	#print('post_data=',post_data)
	#self.proxyURL = '84.10.15.134:8080'
	#self.proxyURL = '178.217.113.62:8080'
	#self.useProxy = True

	def urlOpen(req, customOpeners):
		if len(customOpeners) > 0:
			opener = urllib2.build_opener( *customOpeners )
			response = opener.open(req)
		else:
			response = urllib2.urlopen(req)
		return response

	cj = cookielib.LWPCookieJar()

	response = None
	req	  = None
	out_data = None
	opener   = None

	if 'header' in params:
		headers = params['header']
	else:
		headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0' }

	customOpeners = []
	#cookie support
	if 'use_cookie' not in params and 'cookiefile' in params and ('load_cookie' in params or 'save_cookie' in params):
		params['use_cookie'] = True

	if params.get('use_cookie', False):
		customOpeners.append( urllib2.HTTPCookieProcessor(cj) )
		if params.get('load_cookie', False) and os.path.isfile(params['cookiefile']) :
			cj.load(params['cookiefile'], ignore_discard = True)
	#proxy support
	#if self.useProxy == True:
	#	if dbg == True: print('getURLRequestData USE PROXY')
	#	customOpeners.append( urllib2.ProxyHandler({"http":self.proxyURL}) )

	if None != post_data:
		if dbg == True: print('pCommon - getURLRequestData() -> post data: ' + str(post_data))
		if params.get('raw_post_data', False):
			dataPost = post_data
		else:
			dataPost = urllib.urlencode(post_data)
			#print('dataPost,headers=',dataPost,headers)
		req = urllib2.Request(params['url'], dataPost, headers)
	else:
		req = urllib2.Request(params['url'], None, headers)

	if not params.get('return_data', False):
		out_data = urlOpen(req, customOpeners)
	else:
		gzip_encoding = False
		try:
			response = urlOpen(req, customOpeners)
			if response.info().get('Content-Encoding') == 'gzip':
				gzip_encoding = True
			data = response.read()
			response.close()
		except urllib2.URLError, e:
			if hasattr(e, 'code'):
				"""
				if HTTP_ERRORS[e.code]:
					kom = HTTP_ERRORS[e.code]
				else:
					kom=''
				"""
				try:
					kom = HTTP_ERRORS[e.code]
				except:
					kom=''
				xbmcgui.Dialog().ok('HTTP Error', 'kod: '+str(e.code),kom)
				data = 'Error HTTP:' + str(e.code)
				#print ('Błąd HTTP: '+str(e.code) +' url='+params['url'])
			elif hasattr(e, 'reason'):
				xbmcgui.Dialog().ok('Błąd URL', str(e.reason))
				data = 'Error URL:' + str(e.reason)

		if gzip_encoding:
			print('pCommon - getURLRequestData() -> Content-Encoding == gzip')
			buf = StringIO(data)
			f = gzip.GzipFile(fileobj=buf)
			out_data = f.read()
		else:
			out_data = data

	if params.get('use_cookie', False) and params.get('save_cookie', False):
		#self.checkDir(ptv.getAddonInfo('path') + os.path.sep + "cookies")
		cj.save(params['cookiefile'], ignore_discard = True)

	return out_data
# retuurn True, url or False, Error message
def findMovieUrl(url):
	html = kokolib.httpRequest({ 'url': url, 'return_data': True })
	if("videowood.tv" in url):
		addrscr = aadecode.decode(html)
		if addrscr:
			addr = re.compile("http:(.*?).mp4").findall(addrscr)
			if(len(addr)>0):
				return True, "http:" + addr[0] + ".mp4"
			return False, "Nie znalazlem filmu na videowood.tv"
		return False, "Nie znalazlem aacode na videowood.tv"

	if ("vidto.me" in url or "fileone.tv" in url):
		addr = re.compile('file:"(.*?)"').findall(html)
		if(len(addr)>0):
				return True, addr[0]
		return False, "Nie znalazlem filmu na vidto.me"

	if ("stormo.tv" in url): # https://www.stormo.tv/embed/209929/
		addr = re.compile("file: '(.*?)'").findall(html)
		if(len(addr)>0):
				return True, addr[0]
		return False, "Nie znalazlem filmu na stormo.tv"
	if("openload." in url): # https://openload.co/embed/CHGRbVp4xiU
		movieParams = re.compile('(?://|\.)(openload\.(?:io|co))/(?:embed|f)/([0-9a-zA-Z-_]+)').findall(url)[0] # ('openload.co', 'CHGRbVp4xiU')
		apiUrl = 'https://api.openload.co/1/streaming/get?file=' + movieParams[1]
		jss = kokolib.httpRequest({ 'url': apiUrl, 'return_data': True })
		zz = json.loads(jss)
		if(zz['status'] != 200):
			return False, zz['msg'] # IP address not authorized. Visit https:\/\/olpair.com
		return True, zz['result']['url']
	if("streamango." in url): # https://streamango.com/embed/qkketdbklaobbded
		# https://github.com/orione7/plugin.video.streamondemand-pureita/blob/175ff683ac3f6934a6ee383ba4ecca84bddf1d9c/servers/streamango.py
		return False, "Jeszcze nie dziala"

	return False, "Nie obslugiwany serwer " + url



