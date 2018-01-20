# -*- coding: utf-8 -*-
# Resolves move url from most of hosting websites
import re, sys

class Streamango():
    def decode(self, encoded, code):
        #from https://github.com/jsergio123/script.module.urlresolver - kodi vstream
        _0x59b81a = ""
        k = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
        k = k[::-1]

        count = 0

        for index in range(0, len(encoded) - 1):
            while count <= len(encoded) - 1:
                _0x4a2f3a = k.index(encoded[count])
                count += 1
                _0x29d5bf = k.index(encoded[count])
                count += 1
                _0x3b6833 = k.index(encoded[count])
                count += 1
                _0x426d70 = k.index(encoded[count])
                count += 1

                _0x2e4782 = ((_0x4a2f3a << 2) | (_0x29d5bf >> 4))
                _0x2c0540 = (((_0x29d5bf & 15) << 4) | (_0x3b6833 >> 2))
                _0x5a46ef = ((_0x3b6833 & 3) << 6) | _0x426d70
                _0x2e4782 = _0x2e4782 ^ code

                _0x59b81a = str(_0x59b81a) + chr(_0x2e4782)

                if _0x3b6833 != 64:
                    _0x59b81a = str(_0x59b81a) + chr(_0x2c0540)
                if _0x3b6833 != 64:
                    _0x59b81a = str(_0x59b81a) + chr(_0x5a46ef)

        return _0x59b81a

    def getMediaUrl(self, sourceCode):
        #sourceCode = self.net.http_GET(self.url, headers=self.headers).content.decode('unicode_escape')
        
        videoUrl = ''
        resultado = re.search('''srces\.push\({type:"video/mp4",src:\w+\('([^']+)',(\d+)''', sourceCode)

        if resultado:
            source = self.decode(resultado.group(1), int(resultado.group(2)))
            if source:
                source = "http:%s" % source if source.startswith("//") else source
                source = source.split("/")
                if not source[-1].isdigit():
                    source[-1] = re.sub('[^\d]', '', source[-1])
                videoUrl = "/".join(source)

        return videoUrl

