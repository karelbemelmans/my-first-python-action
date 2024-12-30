import unittest
from greet import greet

class TestGreet(unittest.TestCase):
    
    
    def test_greet_with_valid_input(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_greet_with_empty_string(self):
        self.assertEqual(greet(""), "Hello, !")

    def test_greet_with_none(self):
        self.assertEqual(greet(None), "Hello, None!")


if __name__ == '__main__':
    unittest.main()
