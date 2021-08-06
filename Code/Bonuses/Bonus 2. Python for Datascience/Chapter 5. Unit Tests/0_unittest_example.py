import unittest

class FirstTestClass(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('rubiks code'.upper(), 'RUBIKS CODE')

    def test_upper_gonna_fail(self):
        self.assertEqual('rubiks code'.upper(), 'RUBIKS code')
        
unittest.main()