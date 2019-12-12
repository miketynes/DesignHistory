import unittest

from brick import Brick
import designspace


class TestDesignSpaceABC(unittest.TestCase):

    def setUp(self):
        """Common bricks, positions, and rotations for testing the designspace functionality from many angles"""
        self.design = designspace.DesignSpace()

        self.b1 = Brick('1')
        self.b2 = Brick('2')

        self.pos1 = [1, 2, 3]
        self.pos2 = [4, 5, 6]

        self.rot1 = [7, 8, 9]
        self.rot2 = [10, 11, 12]

    def tearDown(self):
        """Since the design is a singleton we have to reset it's state after every test"""
        self.design.reset()
