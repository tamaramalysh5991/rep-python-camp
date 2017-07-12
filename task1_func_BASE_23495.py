"""
TODO:
    it = reverse_iter([1, 2, 3, 4])
    (so display items in reverse order)

    This realisation use yield and slicing.
"""

from collections import Iterable


def reverse_iter(iterable_varibale):
    """Generator return reverse iterable
        Args:
            iterable_varibale - object, implement the iterator protocol.
        Yields:
            Iterable starting from the end.
        Raises:
            ValueError

        Example:
            t = reverse_iter([1,2,3])
            next(t)
            3
            2
            1
            StopIteration
    """
    if iterable_varibale == []:
        raise ValueError('Iterable! is empty')
    elif isinstance(iterable_varibale, Iterable) is False:
        raise ValueError('It is not iterable!')

    for i in (iterable_varibale)[::-1]:
            yield i



"""First realisation
    def rev_it(iterable):
        n = len(iterable) -1
        while n >= 0:
            yield iterable[n]
            n -=1
"""
