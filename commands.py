"""Implement the Command Pattern around designspace.design add, move, and delete

My understanding of the Command Pattern is greatly endebted to chapter 10 of this book:
https://www.packtpub.com/application-development/mastering-python-design-patterns-second-edition

All classes have three methods: __init__, execute(), and undo(). They maintain enough information
to successfully undo themselves. They are not documented inline, as they are very short and clear.
"""

import designspace
design = designspace.design


class AddBrickToDesign:

    def __init__(self, brick, position, orientation):
        self.brick = brick
        self.position = position
        self.orientation = orientation

    def execute(self):
        design.add(self.brick, self.position, self.orientation)

    def undo(self):
        design.delete(self.brick)


class MoveBrickInDesign:

    def __init__(self, brick, position, orientation):

        self.brick = brick

        # from locations are set at execute time
        self.from_pos = None
        self.from_rot = None

        self.to_pos = position
        self.to_rot = orientation

    def execute(self):
        # save old positions immediately before moving
        self.from_pos = self.brick.position
        self.from_rot = self.brick.orientation
        design.move(self.brick, self.to_pos, self.to_rot)

    def undo(self):
        design.move(self.brick, self.from_pos, self.from_rot)


class DeleteBrickFromDesign:

    def __init__(self, brick):
        self.brick = brick
        self.from_pos = brick.position
        self.from_rot = brick.orientation

    def execute(self):
        design.delete(self.brick)

    def undo(self):
        design.add(self.brick, self.from_pos, self.from_rot)
