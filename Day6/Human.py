import abc
# from datetime import  datetime, date, time
import itertools
import weakref
import uuid
import random
import names


class Person(abc.ABC):
    """Base class of Family tree
    Initializes a Person.

    Atributes:
        first_name (str) =  Human readable string describing first nameDenis.Ta
        last_name (str) =  Human readable string describing last name
        id (uuid) = generete uniq id
        b


    """
    # isinstances = []

    def __init__(self, first_name, last_name, birth, gender):
        # self.__class__.isinstances.append(weakref.proxy(self))
        self.first_name = first_name
        self.id = uuid.uuid4()
        self.last_name = last_name
        self.birth = birth
        self.gender = gender
        self.fertility = random.random()
        self.spouse = None
        self.family = Family()
        # self.parent = parent
        # self.married - married
        #   self.created = created or datetime.now()=


class Family:
    """Class of Family"""

    family_id = uuid.uuid4()

    def __init__(self, father=None, mother=None):
        self.mother = mother
        self.father = father
        self.sister = []
        self.brother = []
        self.children = []

    """def add_sister_brother(self):
        for child in self.children:
            if child.gender == 'm':
                self.brother.append(child)
            else:
                self.sister.append(child)"""


class PersonMixin(object):
    """Class PersonMixin"""

    # @staticmethod
    def marriage(self, person):
        """marriage and create new Family"""
        if not (self.propose or person.propose):
            raise AttributeError('They are not engaged!')
        f = Family()
        person.family = f
        self.family = f
        person.spouse = self
        self.spouse = person
        if isinstance(person, Woman):
            person.maiden_name = person.last_name
            person.last_name = self.last_name
            person.status = 'Wife'
            self.status = 'Husband'
            f.mother = person
            f.father = self
        else:
            self.maiden_name = self.last_name
            self.last_name = person.last_name
            self.status = 'Wife'
            person.status = 'Husband'
            f.mother = self
            f.father = person

    # @classmethod
    def sex(self, person):
        """New member of family"""

        if not (self.spouse == person and person.spouse == self):
            AttributeError('It not a spouse')
        total_fertility = self.fertility + person.fertility - (self.fertility * person.fertility)
        if total_fertility > 0.5:
            print('baby!')
            gender = ['f', 'm']
            g = random.choice(gender)
            if g == 'f':
                name = names.get_first_name(gender='female')
                baby = Woman(name, person.last_name, 2017, g)
            else:
                name = names.get_first_name(gender='male')
                baby = Man(name, person.last_name, 2017, g)
            baby.family = person.family
            person.family.children.append(baby)
            if isinstance(person, Woman):
                baby.family.mother = person
                baby.family.father = self
            else:
                baby.family.mother = self
                baby.family.father = person
            if len(person.family.children) != 0:
                # person.family.add_sister_brother()
                if isinstance(baby, Man):
                    person.family.brother.append(baby)
                else:
                    person.family.sister.append(baby)
        else:
                print('Ops!')


class Woman(Person, Family, PersonMixin):
    """Class Woman(Person)"""

    def __init__(self, first_name, last_name, birth, gender,
                 status=None, propose=False, maiden_name=None, spouse=None):
        super().__init__(first_name, last_name, birth, gender)
        self.spouse = spouse
        self.maiden_name = maiden_name
        self.root_id = self.id
        self.propose = propose
        self.status = status


class Man(Person, Family, PersonMixin):
    """Class Man (Person)"""

    def __init__(self, first_name, last_name, birth,
                 gender, propose=False, status=None, spouse=None):
        super().__init__(first_name, last_name, birth, gender)
        self.spouse = spouse
        self.root_id = self.id
        self.propose = propose
        self.status = status

    def proposed(self, person):
        if isinstance(person, Man):
            raise AttributeError('You dont"t married on man!')

        probability_of_consent = random.random()
        if probability_of_consent:  # > 0.5
            print('She say Yes!')
            person.propose = True
            self.propose = True
            person.status = 'Fiancee'
            self.status = 'Fiance'


Andrey = Man('Andrey', 'Shilov', 1991, 'm')

Tamara = Woman('Toma', 'Malysheva', 1995, 'f')
Denis = Man('Denis', 'Tverd', 1992, 'm')
Denis.proposed(Tamara)
Denis.marriage(Tamara)
Denis.sex(Tamara)

