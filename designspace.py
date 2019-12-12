"""A stubbed out version of the Design space.


"""

VERBOSE = True


class Singleton(type):
    """https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DesignSpace(metaclass=Singleton):

    def __init__(self):
        self.bricks = []

    def __iter__(self):
        for brick in self.bricks:
            yield brick

    def __len__(self):
        return len(self.bricks)

    def __contains__(self, key):
        return key in self.bricks

    def add(self, brick, position, orientation):

        if brick in self:
            raise ValueError(f'Brick {brick.id} is already in design space')

        brick.position = position
        brick.orientation = orientation
        self.bricks.append(brick)

        logmsg =    f'Added brick {brick.id} to point {position} with rot {orientation}'
        if VERBOSE:
            print(logmsg)

    def move(self, brick, position, orientation):

        if brick not in self:
            raise ValueError(f'Brick {brick.id} is not in design space')

        brick.position = position
        brick.orientation = orientation

        logmsg = f'Moved brick {brick.id}  to point {position} with rot {orientation}'
        if VERBOSE:
            print(logmsg)

    def delete(self, brick):

        if brick not in self:
            raise ValueError(f'Brick {brick.id} is not in design space')
        logmsg = f'Removed brick {brick.id}'
        if VERBOSE:
            print(logmsg)

    def __hash__(self):
        """Make the whole design space hashable

        This is so we can easily compare the states of the design space before and after changes
        """
        return hash(', '.join([str(hash(brick)) for brick in self]))


design = DesignSpace()
