import unittest

import brick


class TestBrick(unittest.TestCase):

    def test_position(self):
        """Test the position getter and setter"""
        b = brick.Brick(id='42')
        pos = [1, 2, 3]
        b.position = pos
        self.assertEqual(b.position, pos)

    def test_orientation(self):
        """Test the orientation getter and setter"""
        b = brick.Brick(id='42')
        rot = [1, 2, 3]
        b.orientation = rot
        self.assertEqual(b.orientation, rot)

    def test_hash(self):
        """Test the brick __hash__ method"""

        # first check that it works at all
        b = brick.Brick(id='42')
        self.assertIsInstance(hash(brick), int)

        # then check that it is the same as long as all attributes are the same
        # I don't see why this wouldn't be true, but we should test it!

        x = brick.Brick('42')
        y = brick.Brick('42')
        self.assertEqual(hash(x), hash(y))
        pos = [1, 2, 3]
        rot = [3, 4, 5]

        x.position = pos
        x.orientation = rot

        y.position = pos
        self.assertNotEqual(hash(x), hash(y))  # but also make sure they don't hash to the same value when different
        y.orientation = rot
        self.assertEqual(hash(x), hash(y))

        # check that hash equality is preserved when operations are applied to bricks over time
        b.orientation = [1, 2, 3]
        orientation_1_hash = hash(b)
        b.orientation = [3, 4, 5]
        b.orientation = [1, 2, 3]
        self.assertEqual(orientation_1_hash, hash(b))


if __name__ == '__main__':
    unittest.main()
