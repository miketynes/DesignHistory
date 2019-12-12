import unittest

import design_interface
from test.test_designspace_ABC import TestDesignSpaceABC

from designspace import design

class TestDesignInterface(TestDesignSpaceABC):

    def test_add(self):
        design_interface.add(self.b1, self.pos1, self.rot1)
        self.assertEqual(design.bricks[0], self.b1)

    def test_move_undo_redo(self):
        design_interface.add(self.b1, self.pos1, self.rot1)
        design_interface.move(self.b1, self.pos2, self.rot2)
        self.assertEqual(design.bricks[0].position, self.pos2)
        self.assertEqual(design.bricks[0].orientation, self.rot2)

        design_interface.undo()
        self.assertEqual(design.bricks[0].position, self.pos1)
        self.assertEqual(design.bricks[0].orientation, self.rot1)

        design_interface.redo()
        self.assertEqual(design.bricks[0].position, self.pos2)
        self.assertEqual(design.bricks[0].orientation, self.rot2)

    def test_delete(self):
        design_interface.add(self.b1, self.pos1, self.rot1)
        design_interface.delete(self.b1)
        self.assertEqual(len(design), 0)


if __name__ == '__main__':
    unittest.main()
