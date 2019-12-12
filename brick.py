"""Implements the BARE minimum for the code I needed to write to manage history/undo/redo. It does NOT
handle snapping bricks together by pegs/tubes. Other code, (Danah's and Austin's) should handle something like that.

This is just what I needed to get my own code running because I didn't have theirs in time. If we all coded reasonable
swapping their code into here should be trivial.
"""

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
