import abc
from datetime import  datetime, date, time
import itertools

class Person(abc.ABC):
    ID = itertools.count()


    def __init__(self, first_name, last_name, birth, gender, height, weight, parent = None, level = 0):
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


    #def age(self, birth):
        #age = datetime.now() - datetime(birth)

    def dic(self):
        attr = vars(self)
        #return attr
        for key in attr:
            print(key, ':', attr[key],'\n')


#Toma = Person('Green', 1995, 'f', 165, 55)

'''def ancestors(genealogy, person):
	if person in genealogy:
		parents = genealogy[person]
		result = parents
		for parent in parents:
			result = result + ancestors(genealogy,parent)
		return result
	return []'''