
class Brick:

    def __init__(self, uid):
        self.UID = uid

        self._x = None
        self._y = None
        self._z = None

        self._alpha = None
        self._beta = None
        self._gamma = None

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
