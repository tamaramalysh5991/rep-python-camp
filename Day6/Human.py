from abc import ABCMeta
# from datetime import  datetime, date, time
import itertools
import weakref
import random
import names


class Person(metaclass=ABCMeta):
    """Base class of Family tree
    Initializes a Person

    Attributes:
        first_name (str): Human readable string describing first nameDenis.Ta
        last_name (str): Human readable string describing last name
        birth(int): year of birth of Person
        fertility (float): this param defines the ability to conceive of Person
        spouse (obj of Man or Woman): spouse of Person
        family (Family) : family of Person, after marriage changes
        root_family (Family): family from where the Person came
    """

    def __init__(self, first_name, last_name, birth, family=None):

        self.first_name = first_name
        self.last_name = last_name
        self.birth = birth
        self.fertility = random.random()
        self.spouse = None
        self.family = family
        self.root_family = self.family


class Family:
    """Class of Family
    Attributes:
        mother (obj) : mother in family
        father (obj) : father in family
        children (list) : contain list of children
    """

    def __init__(self, father, mother):

        self.mother = mother
        self.father = father
        self.children = []


class PersonMixin(object):
    """Class PersonMixin"""

    def marriage(self, person):
        """marriage and create new Family

        Args:
            person (Person): spouse for self

        Raises:
            AttributeError: The couple was be able engaged

        """
        if not (self.propose or person.propose):
            raise AttributeError('They are not engaged!')
        person.spouse = self
        self.spouse = person
        if isinstance(person, Woman):
            person.family = Family(self, person)
            person.maiden_name = person.last_name
            person.last_name = self.last_name
        else:
            person.family = Family(person, self)
            self.maiden_name = self.last_name
            self.last_name = person.last_name

    @property
    def grandmother(person):
        return person.mother.mother, person.father.mother

    @property
    def grandfather(person):
        return [person.root_family.mother.root_family.father.first_name,
                person.root_family.father.root_family.father.first_name]

    @property
    def mother(self):
        return self.root_family.mother

    @property
    def father(self):
        return self.root_family.father

    @property
    def husband(self):
        if isinstance(self, Man):
            raise Exception('Man don"t have a husband!')
        return self.spouse.first_name

    @property
    def wife(self):
        if isinstance(self, Woman):
            raise Exception('Woman don"t have a wife!')
        return self.spouse.first_name

    @property
    def children(self):
        return [child for child in self.family.children]

    @property
    def son(self):
        return [male.first_name for male in self.family.children if isinstance(male, Man)]

    @property
    def daughter(self):
        return [female.first_name for female in self.family.children if isinstance(female, Woman)]

    def divorce(self):
        """Fuction for divorce family

        """
        if isinstance(self, Woman):
            self.last_name = self.maiden_name
        else:
            self.spouse.last_name = self.spouse.maiden_name
            self.family = self.root_family
        self.propose = False
        self.spouse.propose = False
        self.spouse.spouse = None
        self.spouse = None

    def add_child_in_family(self, family):
        self.root_family = Family
        family.children.append(self)
        if not self.spouse:
            self.family = family


class Woman(Person, Family, PersonMixin):
    """Class Woman(Person)

    Attributes:
        spouse (Person): spouse of Woman
        propose (bool): label of betrohal
        fiancee (bool):  label of betrohal
        maiden_name (str): param contain maiden name
    """

    def __init__(self, first_name, last_name, birth, family=None,
                 fiancee = False, propose=False, maiden_name=None, spouse=None):
        super().__init__(first_name, last_name, birth, family=None)
        self.spouse = spouse
        self.maiden_name = maiden_name
        self.propose = propose
        self.fiancee = fiancee


class Man(Person, Family, PersonMixin):
    """Class Man (Person)

    Attributes:
        spouse (Person): spouse of Man
        propose (bool): label of betrohal
        fiance (bool):  label of betrohal

    """

    def __init__(self, first_name, last_name, birth,
                 family=None, propose=False, fiance=False, spouse=None):
        super().__init__(first_name, last_name, birth, family=None)
        self.spouse = spouse
        self.propose = propose
        self.fiance = fiance

    def proposed(self, woman):
        """Function of betrothal
        Args:
        woman (Woman): Narrowed, she's only woman

        Raises:
            AttributeError: betrothal is possible only between a man and a woman

        """
        if isinstance(woman, Man):
            raise AttributeError('You dont"t married on man!')

        probability_of_consent = random.random()
        if probability_of_consent > 0.5:
            print('She say Yes!')
            woman.propose = True
            self.propose = True
            woman.fiancee = True
            self.fiance = True


def total_fertility(man, woman):
    """Function defines total fertility man and woman
    Args:
        param man(Man): instanes of Man
        param woman(Woman): instames of Woman
    Return:
        total_fertilities(float) : total fertility of man and woman
    """
    total_fertilities = man.fertility + woman.fertility - (man.fertility * woman.fertility)
    return total_fertilities


def sex(man, woman):
    """New member of family (child).
    Child added in family of woman.
    Gender and name randomly generated

    Args:
        man (Man): instance of Man
        woman (Woman): instance of Woman

    Raises:
        AttributeError: sex is possible only between a man and a woman
        AttributeError: sex is possible only with the spouses
    """
    if not isinstance(man, Man) or not isinstance(woman, Woman):
        raise AttributeError('It not possible')

    if not (man.spouse == woman and woman.spouse == man):
        AttributeError('It not a spouse')

    if total_fertility(man, woman) > 0.5:
        print('baby!')
        gender = random.choice([Man, Woman])
        if isinstance(gender, Man):
            name = names.get_first_name(gender='male')
        else:
            name = names.get_first_name(gender='female')
        baby = gender(name, man.last_name, 2017)
        baby.family = woman.family
        woman.family.children.append(baby)
    else:
        raise Exception('Small fertility')

Valya = Woman('Valentina', 'Brown', 1938)
Leon = Woman('Leon', 'Brown', 1938)
Gornostay = Family(Leon, Valya)
Leon.family= Gornostay
Valya.family = Gornostay

Andrey = Man('Andrey', 'Malysh', 1968)
Marina = Woman('Marina', 'Malysh', 1968)
Malyshevy = Family(Andrey, Marina)
Andrey.family = Malyshevy
Marina.root_family = Gornostay
Gornostay.children.append(Marina)
Marina.family = Malyshevy

Tamara = Woman('Toma', 'Malysheva', 1995)
Tamara.family = Malyshevy
Tamara.root_family = Malyshevy
Malyshevy.children.append(Tamara)
Denis = Man('Denis', 'Tverd', 1992)
Denis.proposed(Tamara)
Denis.marriage(Tamara)
sex(Denis, Tamara)
Tamara.mother.mother.first_name
