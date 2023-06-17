import unittest

from translator import *

class e2f(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("hello"),"bonjour")
        self.assertEqual(english_to_french("cat"),"chat")
        self.assertNotEqual(english_to_french("dog"),"bonheur")
class f2e(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("bonjour"),"hello")
        self.assertEqual(french_to_english("bonheur"),"happiness")
        self.assertNotEqual(french_to_english("chat"),"dog")


if __name__ == '__main__':
    unittest.main()  
