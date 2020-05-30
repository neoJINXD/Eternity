import unittest
from .sin import sin


class TestSin(unittest.TestCase):

    def test_sin_(self):
        self.assertAlmostEquals()


if __name__ == '__main__':
    unittest.main()
