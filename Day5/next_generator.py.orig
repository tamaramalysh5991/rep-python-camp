import types


class IntegerGenerator:
    """ class just return increment integer IterIncrement.index"""

    def __iter__(self):
        return  self

    def integer(self):
        i = 1
        while True:
            yield i
            i = i + 1

    def integer_next(self):
        old_int = self.integer
        self.integer = self.integer_next
        def int_more():
            yield old_int + 1

        #self.integer = iter(types.MethodType(int_more, self))

    integer = integer_next

    def __next__(self):
        return next(self.integer_next())


class IntegerGenerator:
    """ class just return increment integer IterIncrement.index"""
    def __iter__(self):
        return self

    def integer(self):
        i = 1
        while True:
            print('fff') #
            yield i
            i = i + 1

    def integer_next(self):
        old_int = self.integer
        def int_more():
            yield old_int + 1

        self.integer = types.MethodType(int_more, self)

    def __next__(self):
        return next(self.integer())
