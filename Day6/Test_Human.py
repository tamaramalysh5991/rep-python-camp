import unittest
from human import Person, PersonMixin, Woman, Man
from human import SmallFertility, SexBetweenNotSpouse, NotAdulthood, HomosexualLove


class TestHuman(unittest.TestCase):

    def setUp(self):
        self.Valya = Woman('Valentina', 'Brown', 1938)
        self.Leon = Man('leon', 'Val', 1955)
        self.Leon.proposed(self.Valya)
        self.Leon.marriage(self.Valya)
        self.Gornostay = self.Valya.family
        # Valya.list_family.append(Valya.family)

        self.Andrey = Man('Andrey', 'Malysh', 1968)
        self.Marina = Woman('Marina', 'Malysh', 1968)
        self.Andrey.proposed(self.Marina)
        self.Andrey.marriage(self.Marina)
        self.Malyshevy = self.Marina.family

        self.Marina.root_family = self.Gornostay
        self.Gornostay.children.append(self.Marina)
        # Marina.list_family.append(Marina.family)

        self.Tamara = Woman('Toma', 'Malysheva', 1995)
        self.Tamara.family = self.Malyshevy
        self.Tamara.root_family = self.Malyshevy
        self.Malyshevy.add(self.Tamara)
        self.Denis = Man('Denis', 'Tverd', 1992)
        self.Denis.proposed(self.Tamara)
        self.Denis.marriage(self.Tamara)
        self.Denis.sex(self.Tamara)
        self.Denis.sex(self.Tamara)
        self.Denis.sex(self.Tamara)
        self.Denis.sex(self.Tamara)
        self.Sam = Woman('Sam', 'Snoy', 1955)
        self.Drogo = Man('Drogo', 'Khal', 1992)
        self.Leon.family.add(self.Sam)
        self.Leon.family.add(self.Drogo)
        self.Asha = Woman('Asha', 'n', 1995)
        self.Drogo.proposed(self.Asha)
        self.Drogo.marriage(self.Asha)
        self.Drogo.sex(self.Asha)
        self.Tamara.family.divorce()
        self.Andrey = Man('Andrey', 'Mensh', 1990)
        self.Andrey.proposed(self.Tamara)
        self.Andrey.marriage(self.Tamara)
        self.Andrey.sex(self.Tamara)
        self.Deny= Woman('Deny', 'B', 1990)
        self.Don = Man('Don', 'Grey', 1990)
        self.Don.proposed(self.Deny)
        self.Deny.marriage(self.Don)

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
            leon.sex(valya)

    def test_2(self):
        self.assertEqual(self.Tamara.great_grandmother, None)
        self.assertEqual(self.Tamara.husband.first_name, 'Andrey')
        self.assertNotEqual(self.Valya.great_grandchildren, [])
        self.assertEqual(self.Tamara.grandchildren, [])
        self.assertNotEqual(self.Tamara.cousin, [])
        self.assertNotEqual(self.Tamara.son, [])
        self.assertNotEqual(self.Tamara.daughter, [])
        self.assertEqual(self.Tamara.parents, [self.Tamara.mother, self.Tamara.father])

    def test_3(self):
        with self.assertRaises(Exception):
            self.Denis.husband
        with self.assertRaises(Exception):
            self.Tamara.wife

    def test_4(self):
        self.assertNotEqual(self.Denis.wife, self.Tamara)
        self.assertNotEqual(self.Tamara.children_in_family, [])
        self.assertEqual(self.Andrey.wife, self.Tamara)

    def test_5(self):
        S = Woman('s', 's', 2009)
        Kola = Man('Denis', 'Tverd', 1992)
        woman_test = Woman('s', 's', 1990)
        with self.assertRaises(NotAdulthood):
            Kola.sex(S)
        with self.assertRaises(NotAdulthood):
            Kola.marriage(S)
        with self.assertRaises(SexBetweenNotSpouse):
            Kola.sex(woman_test)


if __name__ == '__main__':
    unittest.main()