from collections import Iterable

<<<<<<< HEAD

def reverse_iter(iterable):
=======
# TODO: Don't make grammar errors when you name the attributes, arguments
def reverse_iter(iterable_varibale):
>>>>>>> master
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
<<<<<<< HEAD
    if isinstance(iterable, Iterable) is False:
        raise AttributeError('It is not iterable!')
=======

    # TODO: use len(iterable) for such comparisons
    if iterable_varibale == []:
        raise ValueError('Iterable! is empty')
    elif isinstance(iterable_varibale, Iterable) is False:
        raise ValueError('It is not iterable!')

    # TODO: parenthesis are not needed here
    for i in (iterable_varibale)[::-1]:
            yield i

>>>>>>> master

    if len(iterable) == 0:
        raise ValueError('Iterable is empty')

    for i in iterable[::-1]:
            yield i
