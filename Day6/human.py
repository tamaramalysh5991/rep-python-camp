import abc
import datetime
import random
import names
from itertools import chain, filterfalse
from functools import reduce
# from human_exceptions import SmallFertility, SexBetweenNotSpouse, NotAdulthood, HomosexualLove
import itertools
import collections
from functools import wraps


def flatten(x):
    """This method flatten a list
    Args:
        x (list) nested list
    """
    if isinstance(x, collections.Iterable):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]

class SmallFertility(Exception):

    """ Exception raised when Male and Female not enough fertility
        for child birth
    """
    pass


class SexBetweenNotSpouse(Exception):

    """ Exception raised when Male and Female try sex if them not are spouses
    """
    pass


class HomosexualLove(Exception):

    """ Exception raised when Man try sex with Man or Woman try sex with Woman
    """
    pass

class NotAdulthood(Exception):

    """ Exception raised when Male try sex with infant.
    """
    pass

class Person(abc.ABC):
    """Base class of Family tree
    Initializes a instance of Person - self-contained unit
    As a human instance a Person have name, year of year of birth, family and fertility.


    Attributes:
        first_name (str): Human readable string describing first nameDenis.Ta
        last_name (str): Human readable string describing last name
        birth(int): year of birth of Person
        fertility (float): this param defines the ability to conceive of Person
        spouse (obj of Man or Woman): spouse of Person
        family (Family) : family of Person, after marriage changes
        root_family (Family): family from where the Person came

    """
    ADULTHOOD = 18

    def __init__(self, first_name, last_name, birth, family=None):

        self.first_name = first_name
        self.last_name = last_name
        self.birth = birth
        self.fertility = random.choice([True, False])
        self.spouse = None
        self.family = family
        self.root_family = family or Family()
        self.list_family = []


class PersonMixin(object):
    """Class PersonMixin
    All instances of Person can use this method

    This class contain virtual properties (Son, Daughter,
    Brother, Sister, Spouse, Wife, Husband, Grandfather,
    Grandmother, GrandChildren, Uncle, Aunt and etc).

    Also PersonMixin contain method of marriage
    and method of divorce.

    """
    @property
    def age(self):
        """This property return age of person"""
        age = datetime.date(self.birth, 1, 1)
        return datetime.date.today().year - age.year

    @property
    def great_grandchildren(self):
        """This property return great_grandchildren """
        # great_child = list(chain([child.children for child in self.grandchildren]))
        # return list(chain.from_iterable(great_child))
        return flatten(self.down(-2))

    @property
    def grandchildren(self):
        """Return grandchildren of Persona
        Grandchildren are children of children of Person
        """
        # grandchild = [child.children for child in self.children]
        # return list(chain.from_iterable([child.children for child in self.children]))
        return flatten(self.down(-1))

    @property
    def cousin(self):
        """This property return cousins
        Cousins are children of aunt and uncle
        """
        aunt_children = list(chain.from_iterable([aunt.children for aunt in self.aunt]))
        uncle_children = list(chain.from_iterable([uncle.children for uncle in self.uncle]))
        #  total = list(chain(aunt_children, uncle_children))
        return list(chain(aunt_children, uncle_children))

    @property
    def grandparents(self):
        """This property return list of grandparents"""
        # return list(chain(self.grandmother, self.grandfather))
        return flatten(self.ancestors(1))

    @property
    def parents(self):
        """This property return parents of Person """
        return [self.mother, self.father]

    @property
    def great_grandmother(self):
        """Property return great grandmothers
        Grandmother is mother of grandmother
        """
        # great_grandmother = [grand.mother for grand in self.grandparents]
        # return list(chain(great_grandmother))
        return list(filterfalse(lambda x: x is None,
                                [family.mother for family in flatten(self.ancestors(2))]))

    @property
    def aunt(self):
        """Property return list of aunts
        Aunt is sister of father or mother
        """
        return list(chain(self.root_family.mother.sisters,
                          self.root_family.father.sisters))

    @property
    def uncle(self):
        """Property return list of uncles
        Uncle is brother of mother or father
        """
        return list(chain(self.root_family.mother.brothers,
                          self.root_family.father.brothers))

    @property
    def brothers(self):
        """Property return list of brother of Person"""
        return [male
                for male in self.root_family.children
                if isinstance(male, Man) and male != self]

    @property
    def sisters(self):
        """Property return list of sisters of Person"""
        return [s
                for s in self.root_family.children
                if isinstance(s, Woman) and s != self]

    @property
    def grandmother(self):
        """This property returns list of grandmother for Person"""
        #return list(chain([self.mother.mother, self.father.mother]))
        return list(chain([family.mother for family in self.ancestors(1)]))

    @property
    def grandfather(self):
        """This property returns list of grandfather for Person"""
        return list(chain([self.mother.father,
                self.father.father]))

    @property
    def mother(self):
        """This property returns mother for Person"""
        return self.ancestors().mother

    @property
    def father(self):
        """This property returns father for Person"""
        return self.ancestors().father

    @property
    def husband(self):
        """This method returns husband of Woman.
        Raises:
            Exception: Man don"t have a husband!
            Only woman can have a husband
        """
        if isinstance(self, Man):
            raise Exception('Man don"t have a husband!')
        if not self.family.divorced:
            return self.spouse

    @property
    def wife(self):
        """This property returns wife of Man.
        Raises:
            Exception: Woman don"t have a wife!
            Only man can have a wife"""
        if isinstance(self, Woman):
            raise Exception('Woman don"t have a wife!')
        if not self.family.divorced:
            return self.spouse

    @property
    def children(self):
        """This property return all children of person"""
        children = []
        for f in self.list_family:
            children += f.children
        return list(chain(children))

    @property
    def children_in_family(self):
        """This method returns list of children for Person"""
        return [child for child in self.family.children]

    @property
    def son(self):
        """This method returns list of sons for Person"""
        return [male
                for male in self.children
                if isinstance(male, Man)]

    @property
    def daughter(self):
        """This method returns list of daughters for Person"""
        return [female
                for female in self.children
                if isinstance(female, Woman)]

    @property
    def family_all(self):
        """This property return all members of root family"""
        return list(chain([self.family.mother, self.family.father], self.family.children))

    @property
    def root_family_all(self):
        """This property return all members of root family"""
        return list(chain([self.root_family.mother, self.root_family.father], self.root_family.children))



    def marriage(self, person):
        """Marriage and create new Family.
        Marriage is possible when propose
        of Man and Woman is True.
        Create new Family, where Woman is mother,
        and Man is father.
        Also Woman change last_name.
        Property person.spouse points to the object of Person(Man or Woman)
        Property person.family changed on new Family.
        If Man or Woman have children, they added in new family.
        Args:
            person (Person): spouse for self

        Raises:
            Exception: marriage is not possible between underage persons
            AttributeError: The couple was be able engaged

        """
        if self.age < Person.ADULTHOOD or person.age < Person.ADULTHOOD:
            raise NotAdulthood ('Too early')
        if not (self.propose or person.propose):
            raise SexBetweenNotSpouse('They are not engaged!')

        person.spouse = self
        self.spouse = person

        if isinstance(person, Woman):
            person.family = Family(self, person)
            person.maiden_name = person.last_name
            person.last_name = self.last_name
            self.family = person.family
        else:
            self.family = Family(person, self)
            self.maiden_name = self.last_name
            self.last_name = person.last_name
            person.family = self.family

        person.list_family.append(person.family)
        self.list_family.append(self.family)

    @property
    def root_family_parents(self):
        return [self.root_family.mother, self.root_family.father]


    def ancestors(self, level=0):
        """This function return linage of family
        Args:
            level (int): lineage level for how much steps need return
        """
        memo = {0: self.root_family}
        if level == 0:
            return memo[0]
        try:
            if self.root_family_all is None:
                return None
        except:
            raise Exception('end')

        if level not in memo:
            memo[level] = list(chain(PersonMixin.ancestors(person, level - 1) for person in self.root_family_parents))
            # lst = list(PersonMixin.rec(person, level - 1) for person in self.root_family_parents)
            return memo[level]

    def ancestors1(self, level=0):
        """This function return linage of family
            Args:
                level (int): lineage level for how much steps need return
        """
        if level == 0:
            return self.root_family
        if self.root_family_all is None:
            return None
        lst = []
        for person in self.root_family_parents:
            lst.append(PersonMixin.ancestors1(person, level - 1))
        return lst


    def down(self, level=0):
        """This method return descendant of person
        Args:
            level (int): lineage level for how much steps need return"""
        if level == 0:
            return self.children
        else:
            return list(chain(PersonMixin.down(child, level + 1) for child in self.children))

    def descendant(self, level=0):
        """This method return descendant of person
        Args:
            level (int): lineage level for how much steps need return"""
        if level == 0:
            return self.children
        for child in self.children:
            yield from PersonMixin.down(child, level - 1)
        return PersonMixin.down(self)





class Family:
    """Class of Family tree
    This class is a model of family
    Each family is a separate cell
    Family can break up (divorce)
    The family consists of mother, father and children
    Parents of Mom and Dad relate to another family (one level higher)
    Grandparents are two levels higher, and so on.

    Args:
        Father, Mother (namedtuple): For the first people (the problem of chicken and eggs),
    seven families are created with the parents of Adam and Eve,
    who are namedtuple

    Attributes:
        mother (obj) : mother in family
        father (obj) : father in family
        children (list) : contain all children in family
        divorced (bool): status of divorce.
    """
    def __init__(self, father=None, mother=None):
        self.mother = mother # or Woman('Eve', 'Goddess', 0,Family(father='Godness', mother='Godness'))
        self.father = father # or Man('Adam', 'Goddess', 0, Family(father='Godness', mother='Godness'))
        self.children = []
        self.divorced = False

    def __iadd__(self, child):
        """This method add child in Family"""
        child.root_family = self
        self.children.append(child)

    add = __iadd__

    def divorce(self):
        """This method release a divorce.
        After divorce father and mother can marriage again.
        Status of divorce of family change on True.
        Status of propose of mother and father change on False.

        """
        self.father.propose = False
        self.mother.propose = False
        self.divorced = True


class Woman(Person, Family, PersonMixin):
    """Fabric of Person type of Woman
    Woman can choice her last_name.

    Attributes:
        spouse (Person): spouse of Woman
        propose (bool): label of betrothal
        maiden_name (str): param contain maiden name
    """
    # NAMES = names.get_first_name(gender='female')

    NAMES = ['Sarah',
             'Mary',
             'Nicole',
             'Mandy',
             'Michelle',
             'Barbara',
             'Sarah',
             'Jessica',
             'Whitney',
             'Sherry']

    #  def __init__(self, first_name, last_name, birth, family=None):
    #  super().__init__(first_name, last_name, birth, family)

    def __init__(self, *args, **kwargs):
        super(Woman, self).__init__(*args, **kwargs)
        self.spouse = None
        self.maiden_name = None
        self.propose = False


class Man(Person, Family, PersonMixin):
    """Class Man (Person)
    Fabric of Person type of Man
    Man can do propose.

    Attributes:
        spouse (Person): spouse of Man
        propose (bool): label of betrothal

    """
    # NAMES = names.get_first_name(gender='male')
    NAMES = ['William',
             'Joseph',
             'Jeffrey',
             'Jeffrey',
             'Joseph',
             'Eric',
             'Jonathan',
             'Justin',
             'Andrew',
             'Christopher']

    def __init__(self, *args, **kwargs):
        super(Man, self).__init__(*args, **kwargs)
        self.spouse = None
        self.propose = False

    def proposed(self, woman):
        """Function of betrothal
        The couple can marriage before.
        Only Man can propose.
        Probability of consent is randomly.

            Args:
                woman (Woman): Narrowed, she's only woman

            Raises:
                AttributeError: betrothal is possible only between a man and a woman

        """

        if isinstance(woman, Man):
            raise HomosexualLove('You dont"t married on man!')

        # if self.family.divorced or woman.family.divorced:
            # raise Exception('')

        probability_of_consent = random.choice([True, False])
        if True:  # probability_of_consent:
            print('She say Yes!')
            woman.propose = True
            self.propose = True

        else:
            woman.propose = False
            self.propose = False
            print('She say No(')

    def sex(self, woman):
        """New member of family (child).
        Child added in family of woman in children list.
        Gender and name randomly generated.
        Year of born automatically assigned for the current year.
        Only Man can initiate sex.

        Args:
            self (Man): instance of Man
            woman (Woman): instance of Woman

        Raises:
            Exception: sex is not possible between underage persons
            AttributeError: sex is possible only between a man and a woman
            AttributeError: sex is possible only with the spouses
        """
        if self.age < Person.ADULTHOOD or woman.age < Person.ADULTHOOD:
            raise NotAdulthood('Too early for sex!')

        if not isinstance(self, Man) or not isinstance(woman, Woman):
            raise HomosexualLove('No sex between man or between woman')

        if not (self.spouse == woman and woman.spouse == self):
            raise SexBetweenNotSpouse('It not a spouse')

        if True:  # man.fertility or woman.fertility:
            print('Congratulations! You have a baby!')
            gender = random.choice([Man, Woman])
            name = random.choice(gender.NAMES)
            baby = gender(name, self.last_name, datetime.date.today().year)
            woman.family.add(baby)
        else:
            raise SmallFertility('Small fertility')


Oksana = Woman('Oks', 'Tverd', 1970)
Oleg = Man('Oleg', 'Tverd', 1970)
Oleg.proposed(Oksana)
Oleg.marriage(Oksana)
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
Oksana.family.add(Denis)
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

Sam = Tamara.children[0]


# Tamara.mother.mother.first_name
