
class Brick:
    """A very simple Brick class"""

    def __init__(self, id):
        self.id = id

        self._x = None
        self._y = None
        self._z = None

        self._alpha = None
        self._beta = None
        self._gamma = None

    def __hash__(self):
        """Make bricks hashable


        Just the hash of the stringified list of stringified properties.
        This should be collision free... right?
        """
        return hash(', '.join(map(str, [self.id, self._x, self._y, self._z, self._alpha, self._beta, self._gamma])))

    @property
    def position(self):
        return [self._x, self._y, self._z]

    @position.setter
    def position(self, position):
        self._x, self._y, self._z = position

    @property
    def orientation(self):
        return [self._alpha, self._beta, self._gamma]

    @orientation.setter
    def orientation(self, orientation):
        self._alpha, self._beta, self._gamma = orientation
