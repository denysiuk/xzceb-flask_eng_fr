import unittest
from translator import english_to_french, french_to_english
class tests(unittest.TestCase): 
    def test_english_to_french(self): 
        self.assertEqual(english_to_french('Hello'), "Bonjour")
        self.assertIsNone(None, "Test value is not none.")
         
    def test_french_to_english(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertIsNone(None, "Test value is not none.")

unittest.main()