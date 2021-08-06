import unittest

def greetings():
    return 'Hello World!'

class HelloworldTests(unittest.TestCase):
    
    def test_get_helloworld(self):
        self.assertEqual(greetings(), 'Hello World!')

unittest.main()




