import unittest

import designspace
from test_designspace_ABC import TestDesignSpaceABC

class TestDesign(TestDesignSpaceABC):

    def test_singletonness(self):
        """Make sure that this module's design and the one built in designspace are the same

        i.e. make sure that the designspace.DesignSpace object is really a singleton
        """
        self.assertIs(self.design, designspace.design)

    def test_add(self):
        """Make sure add acts as expected"""
        self.design.add(self.b1, self.pos1, self.rot1)
        self.assertIs(self.design[0], self.b1)
        with self.assertRaises(ValueError):
            # can't add a brick twice!
            self.design.add(self.b1, self.pos1, self.rot1)

    def test_move(self):
        self.design.add(self.b1, self.pos1, self.rot1)
        self.design.move(self.b1, self.pos2, self.rot2)
        self.assertEqual(self.design[0].position, self.pos2)
        self.assertEqual(self.design[0].orientation, self.rot2)
        with self.assertRaises(ValueError):
            # cant move a brick that isn't added!
            self.design.move(self.b2, self.pos1, self.rot2)

    def test_delete(self):
        self.design.add(self.b1, self.pos1, self.rot1)
        self.design.delete(self.b1)
        self.assertEqual(len(self.design), 0)
        with self.assertRaises(ValueError):
            # cant delete a brick twice!
            self.design.delete(self.b1)
            # or delete one that hasn't been added
            self.design.delete(self.b2)


if __name__ == '__main__':
    unittest.main()
