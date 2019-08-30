import unittest
from StringMe import StringMe

class TestStringMe(unittest.TestCase):
    def test_reflect(self):
        expected = "alicia"
        instance = StringMe(expected)
        actual = instance.reflect()
        self.assertEqual(expected, actual)
        
