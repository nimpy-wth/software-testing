from codefortest.two_char import alternate
import unittest
class TwoCharactersTest(unittest.TestCase):
    def test1(self):
        text = 'beabeefeab'
        test = alternate(text)
        self.assertEqual(test,5)
    
    def test2(self):
        text = 'asvkugfiugsalddlasguifgukvsa'
        test = alternate(text)
        self.assertEqual(test,0)
    
    def test3(self):
        text = 'balvjgararmfjsiopvjnsgaiujijaorfp8awibuwpofm;moeqplmfmav;larpiovrofbiharggancjkeiruvlkmvlmjgopwlpfiauglvmdojmlsannoiw'
        test = alternate(text)
        self.assertEqual(test,8)
    
    def test4(self):
        text = 'ncahoi@#geyc6^n'
        test = alternate(text)
        self.assertEqual(test,3)
    
    def test5(self):
        text = 'hello?'
        test = alternate(text)
        self.assertEqual(test,2)
    
    def test6(self):
        text = 'There was something \'bout you that now I can\'t remember'
        test = alternate(text)
        self.assertEqual(test,6)
    
    def test7(self):
        text = 'It\'s the same damn thing that made my heart surrender'
        test = alternate(text)
        self.assertEqual(test,9)
    
    def test8(self):
        text = 'capibararararara'
        test = alternate(text)
        self.assertEqual(test,2)
    
    def test9(self):
        text = 'abbbabbersbbaagwe'
        test = alternate(text)
        self.assertEqual(test,3)
    
    def test10(self):
        text = 'artificial inteLligence ENgineer'
        test = alternate(text)
        self.assertEqual(test,5)