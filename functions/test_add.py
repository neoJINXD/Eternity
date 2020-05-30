import unittest
from add import add

class TempTest(unittest.TestCase):
    def test_add(self):
        self.assertEquals(add(1,2), 3)


if __name__ == '__main__':
    unittest.main()