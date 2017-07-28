import unittest
from Human import Person, PersonMixin, Woman, Man, sex


class TestHuman(unittest.TestCase):

    def test_0(self):
        valya = Woman('Valentina', 'Brown', 1938)
        leon = Man('leon', 'Val', 1955)
        Peter = Man('l', 'Val', 1955)
        with self.assertRaises(AttributeError):
            leon.marriage(valya)
        with self.assertRaises(AttributeError):
            leon.proposed(Peter)

    def test_1(self):
        valya = Woman('Valentina', 'Brown', 1938)
        leon = Man('leon', 'Val', 1955)
        with self.assertRaises(AttributeError):
            sex(leon, valya)

if __name__ == '__main__':
    unittest.main()