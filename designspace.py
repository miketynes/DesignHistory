"""A stubbed out version of the Design space.


"""

import logging
logging.basicConfig(filename='designspace.log')


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

    def __getitem__(self, i):
        return self.bricks[i]

    def reset(self):
        logging.info('Resetting designSpace to empty')
        self.bricks = []

    def add(self, brick, position, orientation):

        if brick in self:
            raise ValueError(f'Brick {brick.id} is already in design space')

        brick.position = position
        brick.orientation = orientation
        self.bricks.append(brick)

        logging.info(f'Added brick {brick.id} to point {position} with rot {orientation}')

    def move(self, brick, position, orientation):

        if brick not in self:
            raise ValueError(f'Brick {brick.id} is not in design space')

        brick.position = position
        brick.orientation = orientation

        logging.info(f'Moved brick {brick.id}  to point {position} with rot {orientation}')

    def delete(self, brick):

        if brick not in self:
            raise ValueError(f'Brick {brick.id} is not in design space')

        self.bricks.remove(brick)
        logging.info(f'Removed brick {brick.id}')

    def __hash__(self):
        """Make the whole design space hashable

        This exists so that we can compare states of the design space before and after operations
        that should cancel one another, i.e. so that we can test the undo operation.
        By using the hash, we can do this in a memory efficient way, rather than comparing the actual states.
        (which, for large designs, would be very costly to save over time)
        """
        return hash(', '.join([str(hash(brick)) for brick in self]))


design = DesignSpace()
