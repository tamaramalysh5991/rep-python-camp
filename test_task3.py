from task3_func import integers
import unittest

class Test_task1(unittest.TestCase):

    def test1(self):
        s = integers()
        self.assertEqual(next(s), 1)
        self.assertEqual(next(s), 2)
        self.assertEqual(next(s), 3)
        self.assertEqual(next(s), 4)
        s1 = integers()
        self.assertEqual(next(s), 5)


if __name__ == '__main__':
    unittest.main()