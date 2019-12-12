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

    def test_hash(self):
        """Test the brick __hash__ method"""

        # first check that it works at all
        self.assertIsInstance(hash(self.b), int)

        # then check that it is the same as long as all attributes are the same
        # I don't see why this wouldn't be true, but we should test it!

        x = brick.Brick('42')
        y = brick.Brick('42')
        self.assertEqual(hash(x), hash(y))

        x.position = self.pos
        x.orientation = self.rot

        y.position = self.pos
        self.assertNotEqual(hash(x), hash(y))  # but also make sure they don't hash to the same value when different
        y.orientation = self.rot
        self.assertEqual(hash(x), hash(y))

        # check that hash equality is preserved when operations are applied to bricks over time
        # again, not sure why this wouldn't happen, but this was part of my proof to myself that this worked
        orientation_1_hash = hash(y)
        y.orientation = [1, 1, 1]
        y.orientation = self.rot
        self.assertEqual(orientation_1_hash, hash(y))


if __name__ == '__main__':
    unittest.main()
