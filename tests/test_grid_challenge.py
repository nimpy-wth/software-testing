from codefortest.grid_challenge import gridChallenge
import unittest
class gridChallengeTest(unittest.TestCase):
    def test1(self):
        grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        test = gridChallenge(grid)
        self.assertEqual(test,'YES')

    def test2(self):
        grid = ['tjxxx','xtxxj','rzzzz','zzrzz','rzzzz']
        test = gridChallenge(grid)
        self.assertEqual(test,'YES')
    
    def test3(self):
        grid = ['mpxz','abcd','wlmf']
        test = gridChallenge(grid)
        self.assertEqual(test,'NO')
    
    def test4(self):
        grid = ['x']
        test = gridChallenge(grid)
        self.assertEqual(test,'YES')
    
    def test5(self):
        grid = ['kluyisde','kemlpmgy','saoijvrm','uepjcbzf','jhyvurka','jyxqffln','pcgoabqr','ilnwvrgr']
        test = gridChallenge(grid)
        self.assertEqual(test,'NO')
    
    def test6(self):
        grid = ['chilis','pepper','smooth']
        grid2 = ['vbznfwg','eacklwk','bmarzvp','rwgnjqd','xqddtln','wuxtduk','rzmfcik'] 
        test = gridChallenge(grid)
        test2 = gridChallenge(grid2)
        self.assertEqual(test,'NO')
        self.assertEqual(test2,'NO')

    
    def test7(self):
        grid = ['abc','hjk','mpq','rtv']
        test = gridChallenge(grid)
        self.assertEqual(test,'YES')
    
    def test8(self):
        grid = ['ftotqxnjquxgwrqojbrkchm','sbdnfhrcjliwbenpdzjowon','oairvbagzvarwxyhxqvqsfq','vmginsurwctumktwiwnvfxo','kyaisbjookoanmlckjpozgn','flxdfstvmaydfyhrxgslvqx','xxadhevmlowzlfnaixfikkr','pteyzihzbcqqkcteeiedvjj','efqhgzbdeawgzqnkqejmypr','yjmabzsmezbqegnbvfbvepw','rysyinyfrerdqnglcgtwvii','ehhwdexdvynkwsynzpuieei','zvlixvggpwaunzccgdpgndb','xxrweuvgtgwgoumxdecdbzy','mgpwhsododrjobkfhhxhddo']
        test = gridChallenge(grid)
        self.assertEqual(test,'NO')
    
    def test9(self):
        grid = ['mkcapoir','rgayuerbca']
        test = gridChallenge(grid)
        self.assertEqual(test,'NO')
    
    def test10(self):
        grid = ['yyyyyyyyyyyyyyyyyyyeyy','yyyyyyyyyyyyyyyyhyyyyy','yzyyyyyyyyyzyylyyyyyyz','zyyyylyyzyyyyyyyyzyyyy','zyyzzyzyzzzyzzzyzyyzwz','zzzyzzzyzyzyzyzzywyyzz','wzyzzzzyzzzyzyzzyzzzzz','yzzyzwyzzzzzzyzzzzzzyz','zzzzzzzyzzyyzzzzwzzzzz','zzzyzzyzzzzzzzwzzzyzzz','zzzzzzzzzzyyzzzzzzwyzz','zzzzzzzzzzzzzzzzzzzzwz','zzzzzzzzwzzzzzzzzzzzzz','zzzzzzzzzzzzzzzzzzzwzz','zzzzzzzzzzzzzzzzzwzzzz','zzzzzzzzzzzzzzzzzzzzzw','zzzzzzzzzzzxzzzzzzzzzz','zzzzzzzzzzzzzzzzzzzzzx','zzzzzzzzyzzzzzzzzzzzzz','zzzzzzzzzzyzzzzzzzzzzz','zzzzzzzzzzzzzzzyzzzzzz','zzzzzzzzzzzzzzzzyzzzzz']
        test = gridChallenge(grid)
        self.assertEqual(test,'YES')