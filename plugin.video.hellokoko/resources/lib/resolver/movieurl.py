# -*- coding: utf-8 -*-
# Resolves movie url from most of hosting websites
import re, sys, urllib2
import string, json
#from resources.lib.resolver 
from resources.lib.resolver import aadecode, streamango, packer

MovieNotFound = 'Nie znalazlem filmu'

# returns True, 'url' or False, 'Error message'
def findMovieUrl(url):
    # html = httpRequest({ 'url': url, 'return_data': True, 'header':{ 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0', 'referer':'http://kokosik1207.pl/2678-movie.html' } })
    html = httpGet(url)
    if not html:
        return False, 'Link nie dziala'

    try:
        if("videowood.tv" in url):
            addrscr = aadecode.decode(html)
            if addrscr:
                return getJwplayerFile(html)
                #addr = re.compile("http:(.*?).mp4").findall(addrscr)
                #if(len(addr)>0):
                #    return True, "http:" + addr[0] + ".mp4"
                #return False, "Nie znalazlem filmu na videowood.tv"
            return False, "Nie znalazlem aacode na videowood.tv"

        if ("speedvid." in url):
            movieid = re.compile("embed-(.*?)-").findall(url)
            newurl = 'http://www.speedvid.net/'+movieid[0]+'.html'
            html = httpGet(newurl)
            #html = re.sub("(<!--.*?-->)", "", html, flags=re.MULTILINE);
            ##zzz = aadecode.decode(html)
            #qqq = packer.unpack(html)
            #www = packer.unpack(qqq)

            return getJwplayerFile(html)
            #addr = re.compile("file: '(.*?)'").findall(html)
            #if(len(addr)>0):
            #        return True, addr[0]
            #return False, "Nie znalazlem filmu na fileone.tv"


        if ("vidto.me" in url):
            return getJwplayerFile(html)
            #addr = re.compile('file:"(.*?)"').findall(html)
            #if(len(addr)>0):
            #    return True, addr[0]
            #return False, "Nie znalazlem filmu na vidto.me" 

        if ("fileone.tv" in url):
            return getJwplayerFile(html)
            #addr = re.compile("file: '(.*?)'").findall(html)
            #if(len(addr)>0):
            #        return True, addr[0]
            #return False, "Nie znalazlem filmu na fileone.tv" 

        if ("stormo.tv" in url): # https://www.stormo.tv/embed/209929/
            return getJwplayerFile(html)
            #addr = re.compile("file: '(.*?)'").findall(html)
            #if(len(addr)>0):
            #    return True, addr[0]
            #return False, "Nie znalazlem filmu na stormo.tv"

        if("openload." in url):
            return openload(url)
        if("streamango." in url): # https://streamango.com/embed/qkketdbklaobbded
            maddr = streamango.Streamango().getMediaUrl(html)
            if maddr:
                return True, maddr 
            return False, 'Nie znalazłem filmu na streamango'

        if("raptu." in url or 'rapidvideo.' in url): # https://www.raptu.com/e/FIDVTFGYVO
            addr = re.compile('sources": \[\{"file":"(.*?)"').findall(html)
            if(len(addr)>0):
                    murll = addr[0].replace('\\/','/')
                    return True, murll
            return False, "Nie znalazlem filmu na rapidvideo" 

        if("streamplay." in url): 
            return False, "Jeszcze nie dziala ale pracuje na nim" 

    except :
        return False, "Movie resolver error: " + str(sys.exc_info()[0]) + ": " +  str(sys.exc_info()[1])

    return False, "Nie znam takiego providera " + url

def httpGet(url):
    try:
        opener = urllib2.build_opener()
        opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
        response = opener.open(url).read()
        return response #urllib2.urlopen(url).read()
    except :
        return ''

def getJwplayerFile(html):
    addr = re.compile("file ?: ?['\"](.*?)['\"]").findall(html)
    if(len(addr)>0):
        return True, addr[0]
    return False, "Nie znalazlem filmu"
    

def openload(url):
    movieParams = re.compile('(?://|\.)(openload\.(?:io|co))/(?:embed|f)/([0-9a-zA-Z-_]+)').findall(url)[0]
    jss = httpGet('https://api.openload.co/1/streaming/get?file=' + movieParams[1])
    zz = json.loads(jss)
    if(zz['status'] != 200):
        return False, zz['msg'] # IP address not authorized. Visit https:\/\/olpair.com
    return True, zz['result']['url']