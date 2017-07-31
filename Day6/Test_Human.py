import unittest
from Human import Person, PersonMixin, Woman, Man
from text import *


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
            valya.sex(leon)

    def test_2(self):
        self.assertEqual(Tamara.great_grandmother[0].first_name, 'Eve')
        self.assertEqual(Tamara.husband.first_name, 'Andrey')
        self.assertNotEqual(Valya.great_grandchildren, [])
        self.assertEqual(Tamara.grandchildren, [])
        self.assertNotEqual(Tamara.cousin, [])
        self.assertNotEqual(Tamara.son, [])
        self.assertNotEqual(Tamara.daughter, [])
        self.assertEqual(Tamara.parents, [Tamara.mother, Tamara.father])

    def test_3(self):
        with self.assertRaises(Exception):
            Denis.husband
        with self.assertRaises(Exception):
            Tamara.wife

    def test_4(self):
        self.assertNotEqual(Denis.wife, Tamara)
        self.assertNotEqual(Tamara.children_in_family, [])
        self.assertEqual(Andrey.wife, Tamara)

    def test_5(self):
        S = Woman('s', 's', 2009)
        woman_test = Woman('s', 's', 1990)
        with self.assertRaises(Exception):
            Denis.sex(S)
        with self.assertRaises(Exception):
            Denis.marriage(S)
        with self.assertRaises(AttributeError):
            Denis.sex(woman_test)


if __name__ == '__main__':
    unittest.main()