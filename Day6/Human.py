import abc
from datetime import  datetime, date, time
import itertools
import gc

import weakref

class Person(abc.ABC):
    ID = itertools.count()
    isinstances = []


    def __init__(self, first_name, last_name, birth, gender, height, weight, married = False, spouse = None, parent = None, level = 0):
        self.__class__.isinstances.append(weakref.proxy(self))
        self.first_name = first_name
        self.id = next(self.__class__.ID)
        self.last_name = last_name
        self.birth = birth
        self.gender = gender
        self.height = int(height)
        self.weight = int(weight)
        self.parent = parent
        self.level = level
        self.children = []
        #self.married - married
        #   self.created = created or datetime.now()=


    #def age(self, birth):
        #age = datetime.now() - datetime(birth)

    def dic(self):
        attr = vars(self)
        #return attr
        for key in attr:
            print(key, ':', attr[key],'\n')

    def __str__(self):
        print( '[Person: %s, %s]', self.first_name, self.last_name)








class Woman(Person):
    def __init__(self, first_name, last_name, birth, gender, height, weight, married = False, spouse = None,  husband = None, parent = None, level = 0, maiden_name=None  ):
        super().__init__(first_name, last_name, birth, gender, height, weight, married = False, spouse = None,  parent = None, level=0)



class Man(Person):
    def __init__(self, first_name, last_name, birth, gender, height, weight, married = False,  spouse = None, wife = None, parent = None, level = 0):
        super().__init__( first_name, last_name, birth, gender, height, weight, married = False,  spouse = None, parent=None, level=0)

    def propose(self):
        pass



def marriage(Woman, Man):
    Woman.married = True
    Man.married = True
    Woman.spouse = Man.first_name
    Woman.husband = Man.first_name
    Woman.maiden_name = Woman.last_name
    Woman.last_name = Man.last_name
    Man.spouse = Woman.first_name
    Man.wife = Woman.first_name

def print_all():
    for instance in Person.isinstances:
        print(instance.first_name)
        #print(instance.__dict__)

'''def Parent(Person.y, Person.q):
    pass'''


class Family:

    def mother(self):
        pass

    def father(self):
        pass

    def sister(self):
        pass

    def brother(self):
        pass



#Toma = Person('Green', 1995, 'f', 165, 55)

'''def ancestors(genealogy, person):
	if person in genealogy:
		parents = genealogy[person]
		result = parents
		for parent in parents:
			result = result + ancestors(genealogy,parent)
		return result
	return []'''

# Tamara = Woman('Toma', 'Malysheva', 1995, 'f', 164, 55)
# Denis = Man('Denis', 'Tverd', 1992, 'm', 179, 75)
# Andrey  = Man('Andrey', 'Shilov', 1991, 'm', 179, 75)
