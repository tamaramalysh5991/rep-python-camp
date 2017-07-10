"""Implement state-aware integers() generator.

        def integers():
        i = 1
        while True:
            yield i
            i = i + 1

    desired outcome:

            i1 = integers()
            next(i1)
            1
            next(i1)
            2
            next(i1)
            3
            i2 = integers()
            next(i2)
            4
"""

def integers():
    if not hasattr(integers, 'identifier'):
        def count():
            counter = 1
            while True:
                yield counter
                counter += 1
        integers.identifier = count()
    return integers.identifier