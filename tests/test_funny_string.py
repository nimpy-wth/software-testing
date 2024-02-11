from codefortest.funny_string import funnyString
import unittest
class FunnyStrTest(unittest.TestCase):
    def test1_is_funny(self):
        text = 'acxz'
        test_is_funny = funnyString(text)
        self.assertEqual(test_is_funny,"Funny")
    
    def test2_is_funny(self):
        text = 'bcxz'
        test_is_funny = funnyString(text)
        self.assertEqual(test_is_funny,"Not Funny")
    
    def test3_is_funny(self):
        text = 'yrzxrxskrtlpwpmtpxvowrxrpxq'
        test_is_funny = funnyString(text)
        self.assertEqual(test_is_funny,"Not Funny")
    
    def test4_is_funny(self):
        text = 'ivvkx'
        test_is_funny = funnyString(text)
        self.assertEqual(test_is_funny,"Not Funny")

    def test5_is_funny(self):
        text = 'xskqyrzyuzxrxpwqunumoumswqvqstwsxzyumnruztlnszskpuntvptzwoqumqyuzryumpvzrwrvyvyqxytuowqrzswpruxruvwyvpvxzxsxszvyrzwrzrwpvnszwptyquoqruyvqyrszxuzystlqvpsxuvopuxpxprsvqtmqrywyzsuovxuyrwopuoqrzyzsuvwqtmorwzvpqvyqwqyvqpvzwromtqwvuszyzrqoupowryuxvouszywyrqmtqvsrpxpxupovuxspvqltsyzuxzsryqvyurqouqytpwzsnvpwrzrwzryvzsxsxzxvpvywvurxurpwszrqwoutyxqyvyvrwrzvpmuyrzuyqmuqowztpvtnupkszsnltzurnmuyzxswtsqvqwsmuomunuqwpxrxzuyzrksyql'
        test_is_funny = funnyString(text)
        self.assertEqual(test_is_funny,"Funny")

    def test6_is_funny(self):
        text = 'oruxsyvwowxzvpskswxtmuwryuxpswrztmprvqtwswtqvrpmtzrwspxuyrwyqxtswowtzvtsksroupmjg'
        test_is_funny = funnyString(text)
        self.assertEqual(test_is_funny,"Funny")
    
    def test7_is_funny(self):
        text = 'recbivvynwminjrsqwyzjuxsxwsntrimwlnggifuescresjvrjvzfsreqlqmezxbkkgrumnzhpskjdhzlcbqwttmfmzinxkzjsqfgefmuwxfzhfmiheebzshlrqzqdyzupecuiqqhnuitbteixjk'
        test_is_funny = funnyString(text)
        self.assertEqual(test_is_funny,"Not Funny")
    
    def test8_is_funny(self):
        text = 'wxstwxuzuyuvyzrsxysxyuvyqxuxyskqwsyqumqrvopvowqumnvrxpwqpwsrnvrztxrxpvuxunvyzvupvupowvyzvzuzwvsrwv'
        test_is_funny = funnyString(text)
        self.assertEqual(test_is_funny,"Funny")

    def test9_is_funny(self):
        text = 'uvzxrumuztyqyvpnji'
        test_is_funny = funnyString(text)
        self.assertEqual(test_is_funny,"Funny")
    
    def test10_is_funny(self):
        text = 'fmpszyvqwxrtvpuwqszvyvotmsxsxuvzyvpwzrpmuxqwtswvytytzsnuxuyrpvtysqoutzurqxury'
        test_is_funny = funnyString(text)
        self.assertEqual(test_is_funny,"Not Funny")
