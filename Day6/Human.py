import abc
# from datetime import  datetime, date, time
import itertools
import weakref
import uuid


class Person(abc.ABC):
    '''Base class of Family tree
    Initializes a Person

    '''
    ID = itertools.count()
    isinstances = []

    def __init__(self, first_name, last_name, birth, gender):
        self.__class__.isinstances.append(weakref.proxy(self))
        self.first_name = first_name
        self.id = next(self.__class__.ID)
        self.last_name = last_name
        self.birth = birth
        self.gender = gender
        # self.parent = parent
        # self.married - married
        #   self.created = created or datetime.now()=

    def sex(self):
        pass

    def add_mother(self):
        pass

    def add_father(self):
        pass

    def __dict__(self):
        attr = vars(self)
        for key in attr:
            print(key, ':', attr[key], '\n')

    def __str__(self):
        ''''''
        print('[Person: %s, %s]', self.first_name, self.last_name)


class Woman(Person):
    def __init__(self, first_name, last_name, birth, gender, maiden_name=None):
        super().__init__(first_name, last_name, birth, gender)


class Man(Person):
    def __init__(self, first_name, last_name, birth, gender):
        super().__init__(first_name, last_name, birth, gender)

    def propose(self):
        pass


class Family:
    '''Class of Family'''

    # def __init__(self):
    family_id = uuid.uuid4()

    def mother(self):
        pass

    def father(self):
        pass

    def sister(self):
        pass

    def brother(self):
        pass

    def marriage(Woman, Man):
        '''marriage and create new Family'''
        Family()
        Woman.married = True
        Man.married = True
        Woman.spouse = Man.first_name
        Woman.husband = Man.first_name
        Woman.maiden_name = Woman.last_name
        Woman.last_name = Man.last_name
        Man.spouse = Woman.first_name
        Man.wife = Woman.first_name
        Woman.id = Family.family_id
        Man.id = Family.family_id


Tamara = Woman('Toma', 'Malysheva', 1995, 'f')
Denis = Man('Denis', 'Tverd', 1992, 'm')
# Andrey  = Man('Andrey', 'Shilov', 1991, 'm', 179, 75)
