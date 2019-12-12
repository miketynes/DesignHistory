import unittest

import design_controller
from commands import *
from test_designspace_ABC import TestDesignSpaceABC


class TestCommandManager(TestDesignSpaceABC):

    def setUp(self):
        super().setUp()

        self.controller = design_controller.DesignController()

        self.add = AddBrickToDesign(self.b1, self.pos1, self.rot1)
        self.move1 = MoveBrickInDesign(self.b1, self.pos2, self.rot2)
        self.move2 = MoveBrickInDesign(self.b2, self.pos2, self.rot2)
        self.delete = DeleteBrickFromDesign(self.b1)


    def test_do(self):
        self.controller.do(self.add)
        self.assertEqual(self.design[0].position, self.pos1)
        self.assertEqual(self.design[0].orientation, self.rot1)

    def test_undo_redo_depth_1(self):

        # first two 'do's work correctly
        self.controller.do(self.add)
        self.controller.do(self.move1)
        self.assertEqual(self.design[0].position, self.pos2)
        self.assertEqual(self.design[0].orientation, self.rot2)

        # first undo works correctly
        self.controller.undo()
        self.assertEqual(self.design[0].position, self.pos1)
        self.assertEqual(self.design[0].orientation, self.rot1)

        # second undo works correctly
        self.controller.undo()
        self.assertEqual(len(self.design), 0)

        # first redo works correctly
        self.controller.redo()
        self.assertEqual(self.design[0].position, self.pos1)
        self.assertEqual(self.design[0].orientation, self.rot1)

        # second redo works correctly
        self.controller.redo()
        self.assertEqual(self.design[0].position, self.pos2)
        self.assertEqual(self.design[0].orientation, self.rot2)

    def test_undo_redo_depth_2(self):
        self.controller.do(self.add)
        self.controller.do(self.move1)

        # undo first two moves
        self.controller.undo(2)
        self.assertEqual(len(self.design), 0)

        # redo them
        self.controller.redo(2)
        self.assertEqual(self.design[0].position, self.pos2)
        self.assertEqual(self.design[0].orientation, self.rot2)


    def test_undo_stack_error(self):
        self.controller.do(self.add)
        self.assertRaises(design_controller.EmptyUndoStackError, self.controller.undo, 2)

    def test_redo_stack_error(self):
        self.controller.do(self.add)
        self.assertRaises(design_controller.EmptyRedoStackError, self.controller.redo)
        self.controller.undo()
        self.controller.do(self.add)
        self.assertRaises(design_controller.EmptyRedoStackError, self.controller.redo)


if __name__ == '__main__':
    unittest.main()
