# -*- coding: utf-8 -*-
# from resources.lib import kokolib
# from resources.lib import aadecode
import re
import json
import imp
kokolib = imp.load_source('kokolib', '.\\plugin.video.hellokoko\\resources\\lib\\kokolib.py')
	
# znalezione na stronie kokosika w javascrypcie
#defalc13="Vidto^$2^$0^$%@%ivqgb.zr/rzorq-dibclbsn98w1-640k360.ugzy^%^Vidto^$2^$1^$%@%ivqgb.zr/rzorq-ghqg1lxau7we-640k360.ugzy^%^Vidto^$0^$0^$^%^Vidto^$0^$0^$^%^Videowood^$2^$0^$%@%ivqrbjbbq.gi/rzorq/1nhk6^%^Videowood^$0^$0^$^%^Videowood^$0^$0^$^%^Videowood^$0^$0^$^%^Fileone^$2^$0^$%@%svyrbar.gi/i/59fee045f09fd^%^Fileone^$2^$1^$%@%svyrbar.gi/i/59fee0a1c3aa8^%^Fileone^$0^$0^$^%^Fileone^$0^$0^$^%^^$0^$0^$^%^^$0^$0^$^%^^$0^$0^$^%^^$0^$0^$^%^^$0^$0^$^%^^$0^$0^$^%^^$0^$0^$^%^^$0^$0^$^%^^$0^$0^$^%^^$0^$0^$^%^^$0^$0^$^%^^$0^$0^$^%^^$0^$0^$^%^^$0^$0^$^%^^$0^$0^$^%^^$0^$0^$^%^Streamango VIP^$2^$0^$f%@%fgernznatb.pbz/rzorq/zabfyxdeqbngfeea/Ohaalzna_Iratrnapr_2017_CY_FHOORQ_JRO-QY_KIvQ-ZBEF_niv^%^Streamango VIP^$2^$1^$f%@%fgernznatb.pbz/rzorq/rcpgdbxgyaqgepcn/Ohaalzna_Iratrnapr_2017_CY_FHOORQ_480c_JRO-QY_KIvQ_NP3-ZBEF_niv^%^Streamango VIP^$2^$2^$^%^Streamango VIP^$0^$0^$^%^Streamango VIP^$0^$0^$^%^Streamango VIP^$0^$0^$^%^Openload VIP^$2^$0^$f%@%bcraybnq.pb/rzorq/d4CojzfCbY4/Ohaalzna_Iratrnapr_%282017%29_CY.FHOORQ.JRO-QY.KIvQ-ZBEF.niv^%^Openload VIP^$2^$1^$^%^Openload VIP^$2^$2^$^%^Openload VIP^$0^$0^$^%^Openload VIP^$0^$0^$^%^Openload VIP^$0^$0^$"
#tmpll = kokolib.decryptDefalc13(defalc13)
#print tmpll
#f = open('kokosik_lista.html')
#html = f.read()

#list3 = kokolib.getTitleList('http://kokosik1207.pl/filmy/akcja/')
#print 'list3:'
#for l in list3:
#	print l[0] + " " + l[1]

#query_data = { 'url': 'http://kokosik1207.pl/', 'use_cookie': True, 'cookiefile': 'koko.cookie', 'save_cookie': True, 'load_cookie': False, 'use_post': True, 'return_data': True }
#loginData   = { 'login_name': 'mojjj', 'login_password': 'jfucker', 'login':'submit' }
#kokolib.httpRequest(query_data, loginData)

#query_data2 = { 'url': 'http://kokosik1207.pl/2565-wojna-o-planete-malp-war-for-the-planet-of-the-apes.html', 'use_cookie': True, 'cookiefile': 'koko.cookie', 'save_cookie': False, 'load_cookie': True, 'return_data': True }
#html = kokolib.httpRequest(query_data2)
#f = open('kokosik_zalog.html', 'w')
#f.write(html)
#f.close
#print 'html:'
#print html
#f = open('kokosik_zalog.html')
#html = f.read()
#print html.find('index.php?action=logout')


#zz = kokolib.decryptDefalc13('Vidto^$2^$0^$%@%ivqgb.zr/rzorq-r4ldnpru45d9-640k360.ugzy^%^Vidto^$2^$1^$%@%ivqgb.zr/rzorq-u65w347cbm3k-640k360.ugzy^%^Vidto^$0^$0^$%@%ivqgb.zr/rzorq-oqvycqder6sk-640k360.ugzy^%^Vidto^$0^$0^$^%^Fileone^$2^$0^$%@%svyrbar.gi/i/59dc690317a2a^%^Fileone^$2^$1^$%@%svyrbar.gi/i/59dcad5c9a3f3^%^Fileone^$0^$0^$%@%svyrbar.gi/i/59e36f3a17120^%^Fileone^$0^$0^$^%^Videowood^$2^$0^$%@%ivqrbjbbq.gi/rzorq/1nb4h^%^Videowood^$2^$1^$^%^Videowood^$0^$0^$^%^Videowood^$0^$0^$^%^Speedvid VIP^$0^$0^$^%^Speedvid VIP^$0^$0^$^%^Speedvid VIP^$0^$0^$^%^Speedvid VIP^$0^$0^$^%^Uptobox VIP^$0^$0^$^%^Uptobox VIP^$0^$0^$^%^Uptobox VIP^$0^$0^$^%^Uptobox VIP^$0^$0^$^%^Stormo VIP^$2^$1^$f%@%jjj.fgbezb.gi/rzorq/194690/^%^Stormo VIP^$2^$2^$f%@%jjj.fgbezb.gi/rzorq/194658/^%^Stormo VIP^$2^$3^$f%@%jjj.fgbezb.gi/rzorq/194670/^%^Stormo VIP^$0^$0^$^%^Stormo VIP^$0^$0^$^%^Stormo VIP^$0^$0^$^%^Streamango VIP^$2^$0^$f%@%fgernznatb.pbz/rzorq/xfoyyezycrbadaqb^%^Streamango VIP^$2^$1^$f%@%fgernznatb.pbz/rzorq/sgrqoobgagefexqg^%^Streamango VIP^$2^$2^$f%@%fgernznatb.pbz/rzorq/scsfnnfsbxerpgzq^%^Streamango VIP^$2^$3^$f%@%fgernznatb.pbz/rzorq/cbxdzonqyeqrrxap^%^Streamango VIP^$0^$0^$f%@%fgernznatb.pbz/rzorq/yfpcnnznsyrdaxbc/Jne_sbe_gur_Cynarg_bs_gur_Ncrf_2017_CY_OQEvc_KivQ-XvG_1_niv^%^Streamango VIP^$0^$0^$^%^Streamango VIP^$0^$0^$^%^Streamango VIP^$0^$0^$^%^Openload VIP^$2^$0^$f%@%bcraybnq.pb/rzorq/3FNTTj6IusV^%^Openload VIP^$2^$1^$f%@%bcraybnq.pb/rzorq/G8F2VGPmrBZ^%^Openload VIP^$2^$2^$f%@%bcraybnq.pb/rzorq/OWz8PqwGUhH^%^Openload VIP^$2^$3^$f%@%bcraybnq.pb/rzorq/8HubkwO3EHf^%^Openload VIP^$0^$0^$f%@%bcraybnq.pb/rzorq/aEJqe4wl4Kt/Jne.sbe.gur.Cynarg.bs.gur.Ncrf.2017.CY.OQEvc.KivQ-XvG_%281%29.niv^%^Openload VIP^$0^$0^$^%^Openload VIP^$0^$2^$f%@%bcraybnq.pb/rzorq/oVvdV2QyqHt/Jne.sbe.gur.Cynarg.bs.gur.Ncrf.2017.CY.720c.OyhEnl.k264.NP3-XvG.zxi^%^Openload [3D] VIP^$7^$3^$f%@%bcraybnq.pb/rzorq/SSzv9Ghcy_R/fxbcvhw_yvax_m_bcraybnq.gkg^%^');
#for z in zz:
#	print z[0] + "   " + z[3]
#ll = kokolib.listVideoProviders('http://kokosik1207.pl/2565-wojna-o-planete-malp-war-for-the-planet-of-the-apes.html')
#print ll

#query_data2 = { 'url': 'http://vidto.me/embed-qvopyofa98j1-640x360.html', 'return_data': True }
#html = kokolib.httpRequest(query_data2)
#f = open('vidto.html', 'w')
#f.write(html)
#f.close
#print html
#print re.compile('file:"(.*?)"').findall(html)

#query_data2 = { 'url': 'http://videowood.tv/embed/1avr9', 'return_data': True }
#html = kokolib.httpRequest(query_data2)
#f = open('openload_co2.html')
#html = f.read()
#scr = aadecode.decode(html)
#print scr #"http:" + re.compile("http:(.*?).mp4").findall(scr)[0] + ".mp4"


#apiUrl = 'https://api.openload.co/1/streaming/get?file=' + 'CHGRbVp4xiU'
#js = kokolib.httpRequest({ 'url': apiUrl, 'return_data': True })
#print js
#js = '{"status":200,"msg":"OK","result":{"name":"Atomic.Blonde.2017.PLSUBBED.BRRiP.XViD-K12.avi.mp4","size":"517819521","sha1":"114f23fda41682190984aa8b0b33d7df71e64909","content_type":"video\/mp4","upload_at":"2017-11-03 07:04:20","url":"https:\/\/oqfnwn.oloadcdn.net\/dl\/l\/kl14zjugIKaalffa\/CHGRbVp4xiU\/Atomic.Blonde.2017.PLSUBBED.BRRiP.XViD-K12.avi.mp4?mime=true","token":"kl14zjugIKaalffa"}}'

#zz = json.loads(js)
#print zz['result']['url']

f = open('koko_pageing.html')
html = f.read()
pp = kokolib.getTitleList(html)
print pp

