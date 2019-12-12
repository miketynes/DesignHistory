"""A stubbed out version of the DesignSpace object. Implemented as a True Singleton.

All methods are stubs and write to logs after performing the minimum of operations required for me to test
my methods which depend on this class existing.

It does NOT do anything like collision detection. I left that to the rest of my team, and our code has not
been integrated yet. Hopefully we all followed our own documentation closely enough that we could easily
merge our codebases.

I did not expect to be stubbing *my own team's* code, but here we are...
"""

import logging
logging.basicConfig(filename='designspace.log')


class Singleton(type):
    """
    I must admit that I don't fully understand how this does what it does.

    All I know is that my test_designspace.py code reveals that this does, in fact, work.

    There is an interesting discussion which I lifted this little class from here:
    https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python

    TODO: read the discussion linked above more closely and understand it's implications
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DesignSpace(metaclass=Singleton):

    def __init__(self):
        """A list-like singleton that keeps track of bricks in the design space. Supports brick adding, moving, and deleting"""
        self.bricks = []

    def __iter__(self):
        """It's iterable!"""
        for brick in self.bricks:
            yield brick

    def __len__(self):
        """It has a length!"""
        return len(self.bricks)

    def __contains__(self, key):
        """You can check if stuff is in it!"""
        return key in self.bricks

    def __getitem__(self, i):
        """You can get stuff from it!"""
        return self.bricks[i]

    def reset(self):
        """You can drop its contents pretty easily! (seems dangerous...)"""
        logging.info('Resetting designSpace to empty')
        self.bricks = []

    def add(self, brick, position, orientation):
        """Add a brick to the design space

        :param brick: a brick.Brick object
        :param position: an iterable of three floats representing position in the design space
        :param orientation: an iterable of three floats representing orientation in the design space

        :raises ValueError: if the brick is already in the design space
        :returns: None
        """
        if brick in self:
            raise ValueError(f'Brick {brick.id} is already in design space')

        brick.position = position
        brick.orientation = orientation
        self.bricks.append(brick)

        logging.info(f'Added brick {brick.id} to point {position} with rot {orientation}')

    def move(self, brick, position, orientation):
        """Move a brick to the design space

        :param brick: a brick.Brick object
        :param position: an iterable of three floats representing a new position in the design space
        :param orientation: an iterable of three floats representing a new orientation in the design space

        :raises ValueError: if the brick is not in the design space
        :returns: None
        """

        if brick not in self:
            raise ValueError(f'Brick {brick.id} is not in design space')

        brick.position = position
        brick.orientation = orientation

        logging.info(f'Moved brick {brick.id}  to point {position} with rot {orientation}')

    def delete(self, brick):
        """Remove a brick from the design space

        :param brick: a brick.Brick object

        :raises ValueError: if the brick is not in the design space
        :returns: None
        """
        if brick not in self:
            raise ValueError(f'Brick {brick.id} is not in design space')

        self.bricks.remove(brick)
        logging.info(f'Removed brick {brick.id}')


design = DesignSpace()
