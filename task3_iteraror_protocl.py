class it:
    i = 0 # start at 0 so that we get 1 when we add 1 below.
    def __init__(self):

        #self.i = 0
        pass
    #the __iter__ method will be called once by the for loop.
    #the rest of the magic happens on the object returned by this method.
    #in this case it is the object itself.
    def __iter__(self):
        return self
    #the next method will be called repeatedly by the for loop
    #without raises StopIteration.
    def __next__(self):
        it.i = it.i + 1
        return  it.i


def integers():
    if not hasattr(integers, '_PIC'):
        def count(start=1, step=1):
            n = start
            while True:
                yield n
                n += step
        integers._PIC = count()
    return integers._PIC
