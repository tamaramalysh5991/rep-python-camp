import unittest

from task0 import cycle_number


class Test_task0(unittest.TestCase):
    '''Unittest for task0.
    Coverage 100%
    '''

    def test_0(self):
        '''Test checks argument 0'''
        s = cycle_number(0)
        self.assertEqual(next(s), 0)

    def test_pozitive(self):
        '''Test checks pozitive numbers'''
        s = cycle_number(3)
        self.assertEqual(next(s), 0)
        self.assertEqual(next(s), 1)
        self.assertEqual(next(s), 2)

    def test_negative(self):
        '''Test checks negative numbers'''
        s = cycle_number(-3)
        self.assertEqual(next(s), 0)
        self.assertEqual(next(s), -1)
        self.assertEqual(next(s), -2)

    def test_exception(self):
        '''Test checks exception
        Raise:
            AttributeError
        '''
        with self.assertRaises(AttributeError):
            next(cycle_number('Commander Shepard'))


if __name__ == '__main__':
    unittest.main()
