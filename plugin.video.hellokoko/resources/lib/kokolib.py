# -*- coding: utf-8 -*-
import re, os.path
#import urllib, urllib2, urlparse, cookielib
import string, json
#import xbmcgui
from resources.lib.resolver import movieurl
from resources.lib import hellotools

rot13 = string.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

quality_arr = {
    '0': '360p',
    '1': '480p',
    '2': '720p',
    '3': '1080p',
    '':''
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
    '12': 'Inne',
    '':''
}

def getNextPage(html):
    pageshtml = re.compile('<div class="paginator"(.*?)</div>', re.DOTALL).findall(html)
    if pageshtml:
        result = re.compile('<a href="(.*?)">(.*?)<', re.DOTALL).findall(pageshtml[0])
        if len(result)>0:
            return result[-1]
    return None

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
    list2 = re.compile('defalc13="(.*?)"').findall(html)
    return decryptDefalc13(list2[0])


# retuurn True, url or False, Error message
def findMovieUrl(url):
    return movieurl.findMovieUrl(url)

def parseSearchHtml(html):
    rr = re.compile('<div class="News">(.*?)<div class="viewn_details">(.*?)</span>', re.DOTALL).findall(html)
    tt = re.compile('<div class="Text">(.*?)</div>', re.DOTALL).findall(html)
    yy = re.compile('Dodaj do ulubionych"></i></a></span></span>(.*?)</span>', re.DOTALL).findall(html)
    uu = re.compile('<div class="viewn_open"><a href="(.*?)"', re.DOTALL).findall(html)
    result = []
    for idx, val in enumerate(rr):
        result.append((hellotools.stripHtml(val[1]), hellotools.stripHtml(yy[idx]), hellotools.stripHtml(uu[idx]), hellotools.stripHtml(tt[idx])))
    return result


# getTitleList returns list of movies from given url
def getTitleList(html):
    html = hellotools.repPolChars(html)
    list2 = re.compile('news-title"><a href="(.*?)">(.*?)<').findall(html)
    #list3 = removeDuplicates(list2)
    genres = re.compile('\| Kategoria:(.*?)</span>').findall(html)
    descs = re.compile('<div class="movie-desc">(.*?)</div>', re.DOTALL).findall(html)
    rates = re.compile('title="OCENA FILMWEB"/>(.*?)</div>', re.DOTALL).findall(html)
    imgList = re.compile('yt-c fullfeature(.*?)<div', re.DOTALL).findall(html)
    
    imgSrc = re.compile('<img src="(.*?)"')
    result = []
    for idx, val in enumerate(list2):
        title = val[1].replace('*','')
        genr = hellotools.stripHtml(genres[idx]).replace('&raquo;','')      
        imgs = imgSrc.findall(imgList[idx])
        img = ''
        if len(imgs)>0:
            img = imgs[0]
        # print img
        filmwebrate = "\n"
        try:
            filmwebrate = " [COLOR=yellow]Filmweb: " + hellotools.stripHtml(rates[idx])+"[/COLOR]\n"
        except :
            pass
        

        result.append((val[0], title, hellotools.stripHtml(genres[idx]), filmwebrate + hellotools.stripHtml(descs[idx]), img))
    return result
