# -*- coding: utf-8 -*-
import re, os.path
import urllib, urllib2, urlparse, cookielib
import string, json

def removeDuplicates(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def stripHtml(text):
    return re.compile(r'(<!--.*?-->|<[^>]*>)').sub('', text).replace('&raquo;','').strip()

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
    req      = None
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
    #    if dbg == True: print('getURLRequestData USE PROXY')
    #    customOpeners.append( urllib2.ProxyHandler({"http":self.proxyURL}) )

    if None != post_data:
        #if dbg == True: print('pCommon - getURLRequestData() -> post data: ' + str(post_data))
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
                print 'HTTP Error '+str(e.code) + ' ' + kom
                xbmcgui.Dialog().ok('HTTP Error', 'kod: '+str(e.code),kom)
                out_data = '' #'Error HTTP:' + str(e.code)
                data = '' # self.net.http_GET(self.url, headers=self.headers).content.decode('unicode_escape')
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

