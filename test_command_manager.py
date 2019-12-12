import unittest

import command_manager
from commands import *
from test_designspace_ABC import TestDesignSpaceABC


class TestCommandManager(TestDesignSpaceABC):

    def setUp(self):
        super().setUp()

        self.manager = command_manager.CommandManager()

        self.add = AddBrickToDesign(self.b1, self.pos1, self.rot1)
        self.move1 = MoveBrickInDesign(self.b1, self.pos2, self.rot2)
        self.move2 = MoveBrickInDesign(self.b2, self.pos2, self.rot2)
        self.delete = DeleteBrickFromDesign(self.b1)


    def test_do(self):
        self.manager.do(self.add)
        self.assertEqual(self.design[0].position, self.pos1)
        self.assertEqual(self.design[0].orientation, self.rot1)

    def test_undo_redo_depth_1(self):

        # first two 'do's work correctly
        self.manager.do(self.add)
        self.manager.do(self.move1)
        self.assertEqual(self.design[0].position, self.pos2)
        self.assertEqual(self.design[0].orientation, self.rot2)

        # first undo works correctly
        self.manager.undo()
        self.assertEqual(self.design[0].position, self.pos1)
        self.assertEqual(self.design[0].orientation, self.rot1)

        # second undo works correctly
        self.manager.undo()
        self.assertEqual(len(self.design), 0)

        # first redo works correctly
        self.manager.redo()
        self.assertEqual(self.design[0].position, self.pos1)
        self.assertEqual(self.design[0].orientation, self.rot1)

        # second redo works correctly
        self.manager.redo()
        self.assertEqual(self.design[0].position, self.pos2)
        self.assertEqual(self.design[0].orientation, self.rot2)

    def test_undo_redo_depth_2(self):
        self.manager.do(self.add)
        self.manager.do(self.move1)

        # undo first two moves
        self.manager.undo(2)
        self.assertEqual(len(self.design), 0)

        # redo them
        self.manager.redo(2)
        self.assertEqual(self.design[0].position, self.pos2)
        self.assertEqual(self.design[0].orientation, self.rot2)


    def test_undo_stack_error(self):
        self.manager.do(self.add)
        self.assertRaises(command_manager.EmptyUndoStackError, self.manager.undo, 2)

    def test_redo_stack_error(self):
        self.manager.do(self.add)
        self.assertRaises(command_manager.EmptyRedoStackError, self.manager.redo)
        self.manager.undo()
        self.manager.do(self.add)
        self.assertRaises(command_manager.EmptyRedoStackError, self.manager.redo)


if __name__ == '__main__':
    unittest.main()
