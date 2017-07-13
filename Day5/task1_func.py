from collections import Iterable


def reverse_iter(iterable):
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
    if isinstance(iterable, Iterable) is False:
        raise AttributeError('It is not iterable!')

    if len(iterable) == 0:
        raise ValueError('Iterable is empty')

    for i in iterable[::-1]:
            yield i
