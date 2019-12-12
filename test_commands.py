import unittest

from brick import Brick
from test_designspace_ABC import TestDesignSpaceABC
from commands import *
import designspace

design = designspace.design


class TestCommands(TestDesignSpaceABC):

    def setUp(self):
        super().setUp()
        self.add = AddBrickToDesign(self.b1, self.pos1, self.rot1)
        self.move1 = MoveBrickInDesign(self.b1, self.pos2, self.rot2)
        self.move2 = MoveBrickInDesign(self.b2, self.pos2, self.rot2)
        self.delete = DeleteBrickFromDesign(self.b1)

    def test_add(self):

        # test that self.add acts just like design.add
        self.add.execute()
        self.assertEqual(self.design[0], self.b1)
        with self.assertRaises(ValueError):
            self.add.execute()

        # check undo method
        self.add.undo()
        self.assertEqual(len(self.design), 0)

    def test_move(self):

        # test that self.move acts just like design.move
        self.add.execute()
        self.move1.execute()
        self.assertEqual(self.b1.position, self.pos2)
        self.assertEqual(self.b1.orientation, self.rot2)
        with self.assertRaises(ValueError):
            self.move2.execute()

        # check undo method
        self.move1.undo()
        self.assertEqual(self.b1.position, self.pos1)
        self.assertEqual(self.b1.orientation, self.rot1)

    def test_delete(self):

        # test that self.delete works just like design.delete
        self.add.execute()
        self.delete.execute()
        self.assertEqual(len(self.design), 0)

        # test undo
        self.delete.undo()
        self.assertEqual(self.design[0], self.b1)