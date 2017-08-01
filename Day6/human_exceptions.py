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