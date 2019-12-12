"""A controller class that executes command objects defined in commands.py on the design space

Module also includes custom Exceptions related to undo history.
"""


class EmptyUndoStackError(Exception):
    pass


class EmptyRedoStackError(Exception):
    pass


class DesignController:

    def __init__(self):
        """Manage the history of the design space without explicitly recording states using command objects.

        Design for this class was heavily influenced by code found here: https://derdon.github.io/blog/implementing-an-undo-redo-manager-in-python.html

        Methods are mostly undocumented as they are considered self-documenting and are not public-facing.

        TODO: make this a true singleton by inheriting from the appropriate metaclass
        """

        self.undo_commands = []
        self.redo_commands = []

    def push_undo_command(self, command):
        self.undo_commands.append(command)

    def pop_undo_command(self):
        """Thin wrapper around list.pop that raises EmptyRedostackError"""
        try:
            last_undo_command = self.undo_commands.pop()
        except IndexError:
            raise EmptyUndoStackError()
        else:
            return last_undo_command

    def push_redo_command(self, command):
        self.redo_commands.append(command)

    def pop_redo_command(self):
        """Thin wrapper around list.pop that raises EmptyRedostackError"""
        try:
            last_redo_command = self.redo_commands.pop()
        except IndexError:
            raise EmptyRedoStackError()
        else:
            return last_redo_command

    def clear_redo_commands(self):
        self.redo_commands[:] = []

    def do(self, command):
        """Execute the command, save it, and clear the redo stack"""
        command.execute()
        self.push_undo_command(command)
        self.clear_redo_commands()

    def undo(self, n=1):
        """Undo the past n items

        :raises: EmptyUndoStackError
        """
        for _ in range(n):
            command = self.pop_undo_command()
            command.undo()
            self.push_redo_command(command)

    def redo(self, n=1):
        """Redo the past n undone items

        :raises EmptyRedoStackError:
        """
        for _ in range(n):
            command = self.pop_redo_command()
            command.execute()
            self.push_undo_command(command)
