class integer:

    def rev_it(iterable): #eeeeeeeeee
        n = len(iterable) -1
        while n >= 0:
            yield iterable[n]
            n -=1

from collections import Iterable


def reverse_iter(iterable):
    if iterable is None:
        raise Exception("It's empty")
    elif isinstance(iterable, Iterable) is False:
        raise Exception("It's not itrable")
    """Generator return reverse instance collections"""
    for i in iterable[::-1]:
        yield i
