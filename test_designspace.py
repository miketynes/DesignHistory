import unittest

from brick import Brick
import designspace




class TestDesign(unittest.TestCase):


    def setUp(self):
        self.design = designspace.DesignSpace()

        self.b1 = Brick('42')
        self.b2 = Brick('42')

        self.pos1 = [1, 2, 3]
        self.pos2 = [4, 5, 6]

        self.rot1 = [7, 8, 9]
        self.rot2 = [10, 11, 12]

    def test_singletonness(self):
        """Make sure that this module's design and the one built in designspace are the same

        i.e. make sure that the designspace.DesignSpace object is really a singleton
        """
        self.assertIs(self.design, designspace.design)


    def test_add(self):
        self.design.add(self.b1, self.pos1, self.rot1)
        self.assertIs(self.design[0], self.b1)
        with self.assertRaises(ValueError):
            self.design.add(self.b1, self.pos1, self.rot1)

    def test_move(self):
        self.design.add(self.b1, self.pos1, self.rot1)
        self.design.move(self.b1, self.pos2, self.rot2)
        self.assertEqual(self.design[0].position, self.pos2)
        self.assertEqual(self.design[0].orientation, self.rot2)
        with self.assertRaises(ValueError):
            self.design.move(self.b2, self.pos1, self.rot2)

    def test_delete(self):
        pass


if __name__ == '__main__':
    unittest.main()
