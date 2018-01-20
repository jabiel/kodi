import unittest
from resources.lib.resolver import movieurl

class Test_moveresolver_test(unittest.TestCase):
    #def test_A(self):
    #    self.fail("Not implemented")

    def test_openload(self):
        rett = movieurl.findMovieUrl('https://openload.co/embed/ps1y-xUMFSo')
        self.assertEqual(rett[0], False) # False gdy openload nie zparowany
        self.assertTrue(rett[1].startswith('IP address not authorized'))
        
    def test_streamango(self):
        rett = movieurl.findMovieUrl('https://streamango.com/embed/nblrpkcatldpfnln')
        self.assertEqual(rett[0], True)
        self.assertTrue(rett[1].startswith('http'))

    def test_speedvid(self):
        rett = movieurl.findMovieUrl('http://www.speedvid.net/embed-glrvletc2kqh-675x450.html')
        self.assertEqual(rett[0], True)
        self.assertTrue(rett[1].startswith('http'))

    def test_vidto(self):
        rett = movieurl.findMovieUrl('http://vidto.me/embed-6wmoqv73rxss-675x450.html')
        self.assertEqual(rett[0], True)
        self.assertTrue(rett[1].startswith('http'))

    def test_fileone(self):
        rett = movieurl.findMovieUrl('http://fileone.tv/v/5n304o35040n1')
        self.assertEqual(rett[0], True)
        self.assertTrue(rett[1].startswith('http'))
        
    def test_streamplay(self):
        rett = movieurl.findMovieUrl('https://streamplay.to/embed-i5sg5siwdrbl.html')
        self.assertEqual(rett[0], True)
        self.assertTrue(rett[1].startswith('http'))     
        
    def test_Jwplayer1(self):
        html = "test> file: 'http://this.is.url.mp4',<test"
        rett = movieurl.getJwplayerFile(html)
        self.assertEqual(rett[0], True)
        self.assertEqual(rett[1], 'http://this.is.url.mp4')

    def test_Jwplayer2(self):
        html = 'test> file: "http://this.is.url.mp4",<test'
        rett = movieurl.getJwplayerFile(html)
        self.assertEqual(rett[0], True)
        self.assertEqual(rett[1], 'http://this.is.url.mp4')

if __name__ == '__main__':
    unittest.main()
