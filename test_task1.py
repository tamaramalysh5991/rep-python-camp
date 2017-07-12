import unittest

from task1_func import reverse_iter


class Test_task1(unittest.TestCase):
    '''Unittest for task1.
    Coverage 100%
    '''

    def setUp(self):
        self.reverse_exp = reverse_iter

    def test_exception(self):
        '''Test checks exceptions ValueError
        and AttributeError
        '''
        with self.assertRaises(ValueError):
            next(self.reverse_exp([]))
        with self.assertRaises(ValueError):
            next(self.reverse_exp(''))
        with self.assertRaises(AttributeError):
            next(self.reverse_exp(2))

    def test_0(self):
        '''Test checks how code works with iterable'''
        s = reverse_iter([1, 2, 3])
        self.assertEqual(next(s), 3)
        self.assertEqual(next(s), 2)
        self.assertEqual(next(s), 1)


if __name__ == '__main__':
    unittest.main()
