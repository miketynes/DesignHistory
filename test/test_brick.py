import unittest
from copy import deepcopy

import brick


class TestBrick(unittest.TestCase):

    def setUp(self):
        self.b = brick.Brick('42')
        self.pos = [1, 2, 3]
        self.b.position = deepcopy(self.pos)

        self.rot = [3, 4, 5]
        self.b.orientation = deepcopy(self.rot)

    def test_position(self):
        """Test the position getter and setter"""
        self.assertEqual(self.b.position, self.pos)

    def test_orientation(self):
        """Test the orientation getter and setter"""
        self.assertEqual(self.b.orientation, self.rot)

if __name__ == '__main__':
    unittest.main()
