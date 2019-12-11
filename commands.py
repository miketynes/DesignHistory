import designspace
design = designspace.DesignSpace()


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
        self.from_pos = brick.position
        self.from_rot = brick.orientation

        self.to_pos = position
        self.to_rot = orientation

    def execute(self):
        design.move(self.brick, self.to_pos, self.to_rot)

    def undo(self):
        design.move(self.brick, self.from_pos, self.from_rot)


class DeleteBrickFromDesign:

    def __init__(self, brick):
        self.brick = brick
        self.from_pos = brick.position
        self.from_rot = brick.orientation

    def execute(self):
        design.add(self.brick, self.from_pos, self.from_rot)
