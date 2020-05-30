import unittest
from functions.add import add


# test class
class TestAdd(unittest.TestCase):

    # make sure to write good tests (all the edge cases),
    # not just a lot of cases
    def test_add(self):
        self.assertEqual(add(1, 1), 2)

    def test_raise_error(self):
        with self.assertRaises(ValueError):
            add(1, 2)


# Allows us to run the tests immediately when this file is run
if __name__ == '__main__':
    unittest.main()
