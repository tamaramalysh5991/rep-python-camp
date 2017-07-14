def integers():
    """Implement state-aware integers() generator.
    An infinite number generator, from 1 to enum.
        Args:
            label (str):  The label indicates whether the function is
            called the first time or not.
        Yields:
            Generates an infinite sequence in increments of 1
        Example:
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
    if not hasattr(integers, 'label'):
        def count():
            counter = 1
            while True:
                yield counter
                counter += 1
        integers.label = count()
    return integers.label
