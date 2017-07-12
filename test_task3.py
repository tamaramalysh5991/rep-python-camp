import unittest

from task3_func import integers


class Test_task1(unittest.TestCase):
    '''Unittest for task3.
    Coverage 100%
    '''

    def test1(self):
        '''Test checks how integers() works'''
        s = integers()
        self.assertEqual(next(s), 1)
        self.assertEqual(next(s), 2)
        self.assertEqual(next(s), 3)
        self.assertEqual(next(s), 4)
        s1 = integers()
        self.assertEqual(next(s1), 5)


if __name__ == '__main__':
    unittest.main()
