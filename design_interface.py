from design_controller import DesignController
from commands import *

controller = DesignController()


def add(brick, position, orientation):
    controller.do(AddBrickToDesign(brick, position, orientation))


def move(brick, position, orientation):
    controller.do(MoveBrickInDesign(brick, position, orientation))


def delete(brick):
    controller.do(DeleteBrickFromDesign(brick))


def undo(n=1):
    controller.undo(n)


def redo(n=1):
    controller.redo(n)
