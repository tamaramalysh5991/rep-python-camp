import abc
# from datetime import  datetime, date, time
import itertools
import weakref
import uuid
import random


class Person(abc.ABC):
    """Base class of Family tree
    Initializes a Person.

    Atributes:
        first_name (str) =  Human readable string describing first name
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
        self.fertility = random.triangular()
        self.spouse = None
        # self.parent = parent
        # self.married - married
        #   self.created = created or datetime.now()=

    def sex(self, person):
        if self.spouse == person and person.spouse == self:
            self.fertility = random.triangular()
            person.fertility = random.triangular()
            total_fertility = self.fertility + person.fertility - (self.fertility * person.fertility)
            if total_fertility > 0.5:
                print('baby!')
            else:
                print('Ops!')
        else:
            print('It not a spouse')

    def add_mother(self):
        pass

    def add_father(self):
        pass


class Family:
    """Class of Family"""

    family_id = uuid.uuid4()

    def __init__(self, father, mother):
        self.mother = mother
        self.father = father

    def sister(self):
        pass

    def brother(self):
        pass


class Woman(Person, Family):
    def __init__(self, first_name, last_name, birth, gender, maiden_name=None, spouse=None):
        super().__init__(first_name, last_name, birth, gender)
        self.spouse = spouse
        self.maiden_name = maiden_name
        self.root_id = self.id

    def marriage(self, man):
        """marriage and create new Family"""
        Family(man, self)
        man.spouse = self
        self.maiden_name = self.last_name
        self.last_name = man.last_name
        self.spouse = man
        self.id = Family.family_id
        man.id = Family.family_id


class Man(Person, Family):
    def __init__(self, first_name, last_name, birth, gender, spouse=None):
        super().__init__(first_name, last_name, birth, gender)
        self.spouse = spouse
        self.root_id = self.id

    def propose(self):
        pass

    # @staticmethod
    def marriage(self, woman):
        """marriage and create new Family"""
        Family(self, woman)
        woman.spouse = self
        woman.maiden_name = woman.last_name
        woman.last_name = self.last_name
        self.spouse = woman
        woman.id = Family.family_id
        self.id = Family.family_id

Andrey  = Man('Andrey', 'Shilov', 1991, 'm')

Tamara = Woman('Toma', 'Malysheva', 1995, 'f')
Denis = Man('Denis', 'Tverd', 1992, 'm')
Denis.marriage(Tamara)

