# See http://code.activestate.com/recipes/52308-the-simple-but-handy-collector-of-a-bunch-of-named/?in=user-97991

class Bunch:
        def __init__(self, **kwds):
                    self.__dict__.update(kwds)
