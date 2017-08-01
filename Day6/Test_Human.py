import unittest
from Human import Person, PersonMixin, Woman, Man
from human_exceptions import SmallFertility, SexBetweenNotSpouse, NotAdulthood, HomosexualLove


class TestHuman(unittest.TestCase):

    def setUp(self):
        Valya = Woman('Valentina', 'Brown', 1938)
        Leon = Man('leon', 'Val', 1955)
        Leon.proposed(Valya)
        Leon.marriage(Valya)
        Gornostay = Valya.family
        # Valya.list_family.append(Valya.family)

        Andrey = Man('Andrey', 'Malysh', 1968)
        Marina = Woman('Marina', 'Malysh', 1968)
        Andrey.proposed(Marina)
        Andrey.marriage(Marina)
        Malyshevy = Marina.family

        Marina.root_family = Gornostay
        Gornostay.children.append(Marina)
        # Marina.list_family.append(Marina.family)

        Tamara = Woman('Toma', 'Malysheva', 1995)
        Tamara.family = Malyshevy
        Tamara.root_family = Malyshevy
        Malyshevy.add(Tamara)
        Denis = Man('Denis', 'Tverd', 1992)
        Denis.proposed(Tamara)
        Denis.marriage(Tamara)
        Denis.sex(Tamara)
        Denis.sex(Tamara)
        Denis.sex(Tamara)
        Denis.sex(Tamara)
        Sam = Woman('Sam', 'Snoy', 1955)
        Drogo = Man('Drogo', 'Khal', 1992)
        Leon.family.add(Sam)
        Leon.family.add(Drogo)
        Asha = Woman('Asha', 'n', 1995)
        Drogo.proposed(Asha)
        Drogo.marriage(Asha)
        Drogo.sex(Asha)
        Tamara.family.divorce()
        Andrey = Man('Andrey', 'Mensh', 1990)
        Andrey.proposed(Tamara)
        Andrey.marriage(Tamara)
        Andrey.sex(Tamara)
        Deny = Woman('Deny', 'B', 1990)
        Don = Man('Don', 'Grey', 1990)
        Don.proposed(Deny)
        Deny.marriage(Don)

    def test_0(self):
        valya = Woman('Valentina', 'Brown', 1938)
        leon = Man('leon', 'Val', 1955)
        Peter = Man('l', 'Val', 1955)
        with self.assertRaises(SexBetweenNotSpouse):
            leon.marriage(valya)
        with self.assertRaises(HomosexualLove):
            leon.proposed(Peter)

    def test_1(self):
        valya = Woman('Valentina', 'Brown', 1938)
        leon = Man('leon', 'Val', 1955)
        with self.assertRaises(SexBetweenNotSpouse):
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
        with self.assertRaises(NotAdulthood):
            Denis.sex(S)
        with self.assertRaises(NotAdulthood):
            Denis.marriage(S)
        with self.assertRaises(AttributeError):
            Denis.sex(woman_test)


if __name__ == '__main__':
    unittest.main()