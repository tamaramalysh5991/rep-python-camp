import abc
# from datetime import  datetime, date, time
import random
import names
from collections import namedtuple
from itertools import chain


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
        self.family = family
        self.root_family = family or Family()
        self.list_family = []


class PersonMixin(object):
    """Class PersonMixin
    All instances of Person can use this methods.

    This class contain virtual properties (Son, Daughter,
    Brother, Sister, Spouse, Wife, Husband, Grandfather,
    Grandmother, GrandChildren, Uncle, Aunt and etc).

    Also PersonMixin contain method of marriage
    and method of divorce.

    """
    @property
    def grandchildren(self):
        """Return grandchildren of Person
        Grandchildren are children of children of Person
        """
        grandchild = []
        for child in self.children:
            grandchild += child.children
        return list(chain(grandchild))

    @property
    def cousin(self):
        """This property return cousins
        Cousins are children of aunt and uncle
        """
        aunt_children = []
        uncle_children = []
        for aunt in self.aunt:
            aunt_children += aunt.children
        for uncle in self.uncle:
            uncle_children += uncle.children
        #  total = list(chain(aunt_children, uncle_children))
        return list(chain(aunt_children, uncle_children))

    @property
    def grandparents(self):
        return list(chain(self.grandmother, self.grandfather))

    @property
    def parents(self):
        """This property return parents of Person """
        return [self.mother, self.father]

    @property
    def great_grandmother(self):
        """Property return great grandmothers
        Grandmother is mother of grandmother
        """
        great_grandmother = []
        for grand in self.grandparents:
            great_grandmother.append(grand.mother)
            return list(chain(great_grandmother))

    @property
    def aunt(self):
        """Property return list of aunts
        Aunt is sister of father or mother
        """
        return list(chain(self.root_family.mother.sisters, self.root_family.father.sisters))

    @property
    def uncle(self):
        """Property return list of uncles
        Uncle is brother of mother or father
        """
        return list(chain(self.root_family.mother.brothers, self.root_family.father.brothers))

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
        return list(chain([self.mother.mother,
                self.father.mother]))

    @property
    def grandfather(self):
        """This property returns list of grandfather for Person"""
        return list(chain([self.mother.father,
                self.father.father]))

    @property
    def mother(self):
        """This property returns mother for Person"""
        return self.root_family.mother

    @property
    def father(self):
        """This property returns father for Person"""
        return self.root_family.father

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
            return self.spouse.first_name

    @property
    def children(self):
        children = []
        for f in self.list_family:
            children += f.children
        return list(chain(children))

        '''for f in self.list_family:
            # return list(chain([child for child in f.children]))
            for child in f.children:
                children.append(child)
        return children'''

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

    # Father = namedtuple('Male', 'first_name, last_name')
    # Mother = namedtuple('Female', 'first_name, last_name')

    def __init__(self, father=None, mother=None):
        self.mother = mother or Woman('Eve', 'Goddess', 0,
                                      Family(father='Godness', mother='Godness'))
        self.father = father or Man('Adam', 'Goddess', 0,
                                    Family(father='Godness', mother='Godness'))
        self.children = []
        self._divorced = False

    def __iadd__(self, child):
        """This method add child in Family"""
        self.children.append(child)

    add = __iadd__

    def add_child(self, person):
        """This method add an already existing person in the Family"""
        person.root_family = self
        self.children.append(person)
        if not person.spouse:
            person.family = self

    '''@property    
    def divorce(self):
        return self._divorced'''

    # @divorce.setter
    def divorce(self):
        """This method release a divorce.
        After divorce father and mother can marriage again.
        Status of divorce of family change on True.

        """
        # if isinstance(value, bool):
        # raise Exception('Its not exist')
        self.father.propose = False
        self.mother.propose = False
        # self.mother.spouse = None
        # self.father.spouse = None
        self._divorced = True


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
        super(Man,self).__init__(*args, **kwargs)
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
            raise AttributeError('You dont"t married on man!')

        # if self.family.divorced or woman.family.divorced:
            # raise Exception('')

        probability_of_consent = random.choice([True, False])
        if True:  # probability_of_consent:
            print('She say Yes!')
            woman.propose = True
            self.propose = True

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

    if True:  # man.fertility or woman.fertility:
        print('baby!')
        gender = random.choice([Man, Woman])
        name = random.choice(gender.NAMES)
        baby = gender(name, man.last_name, 2017)
        baby.root_family = woman.family
        # baby.family = woman.family
        # woman.family.children.append(baby)
        woman.family.add(baby)
    else:
        raise Exception('Small fertility')

Valya = Woman('Valentina', 'Brown', 1938)
Leon = Man('leon', 'Val', 1955)
Gornostay = Family(Leon, Valya)
Leon.family= Gornostay
Valya.family = Gornostay
Valya.list_family.append(Valya.family)

Andrey = Man('Andrey', 'Malysh', 1968)
Marina = Woman('Marina', 'Malysh', 1968)
Malyshevy = Family(Andrey, Marina)

Andrey.family = Malyshevy
Marina.root_family = Gornostay
Gornostay.children.append(Marina)
Marina.family = Malyshevy
Marina.list_family.append(Marina.family)

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
Asha = Woman('Asha', 'n', 1995)
Drogo.proposed(Asha)
Drogo.marriage(Asha)
sex(Drogo, Asha)
Tamara.family.divorce()
Andrey = Man('Andrey', 'Mensh', 1990)
Andrey.proposed(Tamara)
Andrey.marriage(Tamara)
sex(Andrey, Tamara)


# Tamara.mother.mother.first_name
