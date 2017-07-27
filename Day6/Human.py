import abc
# from datetime import  datetime, date, time
import random
import names
from collections import namedtuple


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

    def __init__(self, first_name, last_name, birth, family=None):

        self.first_name = first_name
        self.last_name = last_name
        self.birth = birth
        self.fertility = random.choice([True, False])
        self.spouse = None
        self.family = family or Family()
        self.root_family = self.family


class PersonMixin(object):
    """Class PersonMixin
    All instances of Person can use this methods.

    This class contain virtual properties (Son, Daughter,
    Brother, Sister, Spouse, Wife, Husband, Grandfather,
    Grandmother, GrandChildren, Uncle, Aunt).

    Also PersonMixin contain method of marriage
    and method of divorce.

    """
    @property
    def parents(self):
        """This property return parents of Person """
        return [self.mother, self.father]

    @property
    def aunt(self):
        """Property return list of aunts
        Aunt is sister of father or mother
        """
        return [self.root_family.mother.sisters, self.root_family.father.sisters]

    @property
    def uncle(self):
        """Property return list of uncles
        Uncle is brother of mother or father
        """
        return [self.root_family.mother.brothers, self.root_family.father.brothers]

    @property
    def brothers(self):
        """Property return list of brother of Person"""
        return [male.first_name
                for male in self.root_family.children
                if isinstance(male, Man) and male != self]

    @property
    def sisters(self):
        """Property return list of sisters of Person"""
        return [s.first_name
                for s in self.root_family.children
                if isinstance(s, Woman) and s != self]

    @property
    def grandmother(self):
        """This property returns list of grandmother for Person"""
        return [self.mother.mother.first_name,
                self.father.mother.first_name]

    @property
    def grandfather(self):
        """This property returns list of grandfather for Person"""
        return [self.mother.father.first_name,
                self.father.father.first_name]

    @property
    def mother(self):
        """This property returns mother for Person"""
        return self.root_family.mother.first_name

    @property
    def father(self):
        """This property returns father for Person"""
        return self.root_family.father.first_name

    @property
    def husband(self):
        """This method returns husband of Woman.
        Raises:
            Exception: Man don"t have a husband!
            Only woman can have a husband
        """
        if isinstance(self, Man):
            raise Exception('Man don"t have a husband!')
        return self.spouse.first_name

    @property
    def wife(self):
        """This property returns wife of Man.
        Raises:
            Exception: Woman don"t have a wife!
            Only man can have a wife"""
        if isinstance(self, Woman):
            raise Exception('Woman don"t have a wife!')
        return self.spouse.first_name

    @property
    def children(self):
        """This method returns list of children for Person"""
        return [child for child in self.family.children]

    @property
    def son(self):
        """This method returns list of sons for Person"""
        return [male.first_name
                for male in self.family.children
                if isinstance(male, Man)]

    @property
    def daughter(self):
        """This method returns list of daughters for Person"""
        return [female.first_name
                for female in self.family.children
                if isinstance(female, Woman)]

    '''def divorced(self):
        """Function for divorce family"""
        print('Divorce')
        return self.divorced'''

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
            AttributeError: The couple was be able engaged

        """
        if not (self.propose or person.propose):
            raise AttributeError('They are not engaged!')
        person.spouse = self
        self.spouse = person

        children_person = []
        children_self = []

        if person.family.divorced and (person.family.father == person
                                       or person.family.mother == person):
            children_person = person.family.children

        if self.family.divorced and (self.family.father == self
                                     or self.family.father):
            children_self = self.family.children

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

        for child in children_self:
            self.family.add(child)
        for child in children_person:
            self.family.add(child)


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
        children (list) : contain children
    """

    Father = namedtuple('Male', 'first_name, last_name')
    Mother = namedtuple('Female', 'first_name, last_name')

    def __init__(self, father=None, mother=None):
        self.mother = mother or Family.Mother('Eve', 'Goddess',)
        self.father = father or Family.Father('Adam', 'Goddess',)
        self.children = []
        self.divorced = False

    def __iadd__(self, child):
        """This method add child in Family"""
        self.children.append(child)

    def add_child(self, person):
        """This method add an already existing person in the Family"""
        person.root_family = self
        self.children.append(person)
        if not person.spouse:
            person.family = self

    add = __iadd__

    # @divorced.setter
    def divorce(self):
        """This method release a divorce.
        After divorce father and mother can marriage again.
        Status of divorce of family change on True.

        """
        self.father.propose = False
        self.mother.propose = False
        self.mother.spouse = None
        self.father.spouse = None
        self.divorced = True


class Woman(Person, Family, PersonMixin):
    """Fabric of Person type of Woman
    Woman can choice her last_name.

    Attributes:
        spouse (Person): spouse of Woman
        propose (bool): label of betrothal
        fiancee (bool):  label of betrothal
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

    def __init__(self, first_name, last_name, birth, family=None):
        super().__init__(first_name, last_name, birth, family)
        self.spouse = None
        self.maiden_name = None
        self.propose = False
        self.fiancee = False


class Man(Person, Family, PersonMixin):
    """Class Man (Person)
    Fabric of Person type of Man
    Man can do propose.

    Attributes:
        spouse (Person): spouse of Man
        propose (bool): label of betrothal
        fiance (bool):  label of betrothal

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

    def __init__(self, first_name, last_name, birth,
                 family=None):
        super().__init__(first_name, last_name, birth, family)
        self.spouse = None
        self.propose = False
        self.fiance = False

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
            raise AttributeError('You dont"t married on man!')

        # if self.family.divorced or woman.family.divorced:
            # raise Exception('')

        probability_of_consent = random.choice([True, False])
        if True:  # probability_of_consent:
            print('She say Yes!')
            woman.propose = True
            self.propose = True
            woman.fiancee = True
            self.fiance = True
        else:
            print('She say No(')


def sex(man, woman):
    """New member of family (child).
    Child added in family of woman in children list.
    Gender and name randomly generated.


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

    if man.fertility or woman.fertility:
        print('baby!')
        gender = random.choice([Man, Woman])
        name = random.choice(gender.NAMES)
        baby = gender(name, man.last_name, 2017)
        baby.root_family = woman.family
        baby.family = woman.family
        # woman.family.children.append(baby)
        woman.family.add(baby)
    else:
        raise Exception('Small fertility')

Valya = Woman('Valentina', 'Brown', 1938)
Leon = Man('Leon', 'Brown', 1938)
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
sex(Denis, Tamara)
sex(Denis, Tamara)
sex(Denis, Tamara)
Sam = Woman('Sam', 'Snoy', 1955)
Drogo = Man('Drogo', 'Khal', 1992)
Leon.family.add_child(Sam)
Leon.family.add_child(Drogo)
Andrey = Man('Andrey', 'Mensh', 1990)
Andrey.proposed(Tamara)
Andrey.marriage(Tamara)


# Tamara.mother.mother.first_name
