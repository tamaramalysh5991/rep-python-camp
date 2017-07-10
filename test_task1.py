from task1_func import reverse_iter
import unittest

class Test_task1(unittest.TestCase):

    def setUp(self):
        self.reverse_exp = reverse_iter

    def test_exception(self):
        with self.assertRaises(ValueError):
            next(self.reverse_exp([]))
        with self.assertRaises(ValueError):
            next(self.reverse_exp(''))
        with self.assertRaises(AttributeError):
            next(self.reverse_exp(2))

    def test_0(self):
        s = reverse_iter([1,2,3])
        self.assertEqual(next(s), 3)
        self.assertEqual(next(s), 2)
        self.assertEqual(next(s), 1)

if __name__ == '__main__':
    unittest.main()