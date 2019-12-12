"""The top-level interface to the Team Design's code (or at least to my version of Team Design's code

This more or less satisfies the API described in the team's documentation.

It is a thin wrapper around design_controller.DesignController to keep things pretty.
"""

from design_controller import DesignController
from commands import *

controller = DesignController()


def add(brick, position, orientation):
    """Add a brick to the design space

    :param brick: a brick.Brick object
    :param position: an iterable of three floats representing position in the design space
    :param orientation: an iterable of three floats representing orientation in the design space

    :raises ValueError: if the brick is already in the design space
    :returns: None
    """
    controller.do(AddBrickToDesign(brick, position, orientation))


def move(brick, position, orientation):
    """Move a brick to the design space

    :param brick: a brick.Brick object
    :param position: an iterable of three floats representing a new position in the design space
    :param orientation: an iterable of three floats representing a new orientation in the design space

    :raises ValueError: if the brick is not in the design space
    :returns: None
    """
    controller.do(MoveBrickInDesign(brick, position, orientation))


def delete(brick):
    """Remove a brick from the design space

    :param brick: a brick.Brick object

    :raises ValueError: if the brick is not in the design space
    :returns: None
    """
    controller.do(DeleteBrickFromDesign(brick))


def undo(n=1):
    """Undo the past n changes to the design space.

    History only tracks add/move/delete moves.
    TODO: integrate this with team POV

    :param n: the number of changes to undo
    :raises: design_controller.EmptyUndoStackError if out of moves to undo
    :returns None:
    """
    controller.undo(n)


def redo(n=1):
    """Undo the redo n undos in the design space.

    Redo stack is dropped as soon as new moves are made.

    History only tracks add/move/delete moves.
    TODO: integrate this with team POV

    :param n: the number of changes to redo
    :raises: design_controller.EmptyUndoStackError if out of moves to redo
    :returns None:
    """
    controller.redo(n)
