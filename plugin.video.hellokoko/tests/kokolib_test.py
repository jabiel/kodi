import unittest
from resources.lib import kokolib

class Test_kokolib_test(unittest.TestCase):
    def test_decryptDefalc13(self):
        zz = kokolib.decryptDefalc13('Vidto^$2^$0^$%@%ivqgb.zr/rzorq-r4ldnpru45d9-640k360.ugzy^%^Vidto^$2^$1^$%@%ivqgb.zr/rzorq-u65w347cbm3k-640k360.ugzy^%^Vidto^$0^$0^$%@%ivqgb.zr/rzorq-oqvycqder6sk-640k360.ugzy^%^Vidto^$0^$0^$^%^Fileone^$2^$0^$%@%svyrbar.gi/i/59dc690317a2a^%^Fileone^$2^$1^$%@%svyrbar.gi/i/59dcad5c9a3f3^%^Fileone^$0^$0^$%@%svyrbar.gi/i/59e36f3a17120^%^Fileone^$0^$0^$^%^Videowood^$2^$0^$%@%ivqrbjbbq.gi/rzorq/1nb4h^%^Videowood^$2^$1^$^%^Videowood^$0^$0^$^%^Videowood^$0^$0^$^%^Speedvid VIP^$0^$0^$^%^Speedvid VIP^$0^$0^$^%^Speedvid VIP^$0^$0^$^%^Speedvid VIP^$0^$0^$^%^Uptobox VIP^$0^$0^$^%^Uptobox VIP^$0^$0^$^%^Uptobox VIP^$0^$0^$^%^Uptobox VIP^$0^$0^$^%^Stormo VIP^$2^$1^$f%@%jjj.fgbezb.gi/rzorq/194690/^%^Stormo VIP^$2^$2^$f%@%jjj.fgbezb.gi/rzorq/194658/^%^Stormo VIP^$2^$3^$f%@%jjj.fgbezb.gi/rzorq/194670/^%^Stormo VIP^$0^$0^$^%^Stormo VIP^$0^$0^$^%^Stormo VIP^$0^$0^$^%^Streamango VIP^$2^$0^$f%@%fgernznatb.pbz/rzorq/xfoyyezycrbadaqb^%^Streamango VIP^$2^$1^$f%@%fgernznatb.pbz/rzorq/sgrqoobgagefexqg^%^Streamango VIP^$2^$2^$f%@%fgernznatb.pbz/rzorq/scsfnnfsbxerpgzq^%^Streamango VIP^$2^$3^$f%@%fgernznatb.pbz/rzorq/cbxdzonqyeqrrxap^%^Streamango VIP^$0^$0^$f%@%fgernznatb.pbz/rzorq/yfpcnnznsyrdaxbc/Jne_sbe_gur_Cynarg_bs_gur_Ncrf_2017_CY_OQEvc_KivQ-XvG_1_niv^%^Streamango VIP^$0^$0^$^%^Streamango VIP^$0^$0^$^%^Streamango VIP^$0^$0^$^%^Openload VIP^$2^$0^$f%@%bcraybnq.pb/rzorq/3FNTTj6IusV^%^Openload VIP^$2^$1^$f%@%bcraybnq.pb/rzorq/G8F2VGPmrBZ^%^Openload VIP^$2^$2^$f%@%bcraybnq.pb/rzorq/OWz8PqwGUhH^%^Openload VIP^$2^$3^$f%@%bcraybnq.pb/rzorq/8HubkwO3EHf^%^Openload VIP^$0^$0^$f%@%bcraybnq.pb/rzorq/aEJqe4wl4Kt/Jne.sbe.gur.Cynarg.bs.gur.Ncrf.2017.CY.OQEvc.KivQ-XvG_%281%29.niv^%^Openload VIP^$0^$0^$^%^Openload VIP^$0^$2^$f%@%bcraybnq.pb/rzorq/oVvdV2QyqHt/Jne.sbe.gur.Cynarg.bs.gur.Ncrf.2017.CY.720c.OyhEnl.k264.NP3-XvG.zxi^%^Openload [3D] VIP^$7^$3^$f%@%bcraybnq.pb/rzorq/SSzv9Ghcy_R/fxbcvhw_yvax_m_bcraybnq.gkg^%^');
        self.assertTrue(isinstance(zz, list)) # is list
        self.assertEqual(22, len(zz))
        self.assertEqual('Vidto', zz[0][0])


if __name__ == '__main__':
    unittest.main()
