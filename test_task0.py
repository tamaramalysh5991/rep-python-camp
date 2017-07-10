from task0 import cycle_number
import unittest

class Test_task0(unittest.TestCase):
    #def setUp(self):
        #self.cycle_exception = cycle_number

    def test_0(self):
        s = cycle_number(0)
        self.assertEqual(next(s), 0)

    def test_pozitive(self):
        s = cycle_number(3)
        self.assertEqual(next(s), 0)
        self.assertEqual(next(s), 1)
        self.assertEqual(next(s), 2)

    def test_negative(self):
        s = cycle_number(-3)
        self.assertEqual(next(s), 0)
        self.assertEqual(next(s), -1)
        self.assertEqual(next(s), -2)

    def test_exception(self):
        with self.assertRaises(AttributeError):
            next(cycle_number('Commander Shepard'))

if __name__ == '__main__':
    unittest.main()