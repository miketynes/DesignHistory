# DesignHistory
Design Space History Demo

Here I have written my code for my final assignment in Fordham's CISC 6100--software engineering. 

The project is supposed to be a team project, but due to some lapses in communication and availability alighment, I ended up re-coding 
portions of the assignment given to other teammates here. 

For the program modules, working from low-level to high-level modules, we have

| Module              | Description                                                                                                                                                                                                                        |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| brick.py            |  `brick.Brick` is the simplest design unit.   A brick has an ID, a position and an orientation.                                                                                                                                                     |
| designspace.py      |  `designspace.design` is singleton container for bricks to live inside of.   Supports add, move, and delete operations.                                                                                                                                  |
| commands.py         |  Provides three command pattern wrappers to `designspace.design`: `AddBrickToDesign`, `MoveBrickInDesign`, and `DeleteBrickFromDesign`. These allow operations to be neatly undone                                                                                                            |
| designcontroller.py |  `designcontroller.DesignController` executes the commands from `commands.py`, maintains undo/redo history, and provides `undo` and `redo` methods which operate globally over the design space's state.
| design_interface.py | A thin wrapper to designcontroller.py which hides information for the user (i.e. other teams on the project).                                                                                                                      |


You should read the modules and their assocuated tests in this order.

The test modules are all self explanatory, with the exception of `test_design_space_ABC`, which just houses a common `setUp` method for multiple test
suites (*ergo* it is not a *true* ABC, but its easily recognizable as abstract). 

## Installation and Usage
To install and run this code, you only need a `python3` interpreter. I ran all of my tests in `python3.6.9` running on Ubuntu18.02.

It has no dependencies as it is mostly just a high-level design demo.

To clone the code, just run `git clone http://www.github.com/miketynes/DesignHistory` from whatever directory you want my code to haunt forever. 

To run the tests, **from the project's root directory** run `python -m unittest discover test`. 

## API reference

**Note:** All methods return `None` so return type is ommitted. Additionally, all methods are documented at greater detail inline. A good next step would be to automate documentation generation with a tool like [sphinx](http://www.sphinx-doc.org/en/master/)

| Method Name                                           |              | Details                                                                                     | Overview                                               |
|-------------------------------------------------------|--------------|---------------------------------------------------------------------------------------------|--------------------------------------------------------|
| `design_interface.add(brick, position, orientation)`  |              |                                                                                             | Add a brick to the design space                        |
|                                                       | `parameters` |  `brick`: a brick object   `position`: a list of 3 floats `orientation`: a list of 3 floats |                                                        |
|                                                       | `raises`     | `ValueError`: if you try to add a brick more than once                                      |                                                        |
| `design_interface.move(brick, position, orientation)` |              |                                                                                             | Move a brick to a new location in the design space     |
|                                                       | `parameters` | `brick`: a brick object   `position`: a list of 3 floats `orientation`: a list of 3 floats  |                                                        |
|                                                       | `raises `    | `ValueError`: if you try to move a brick that isn't in the design yet                       |                                                        |
| `design_interface.delete(brick)`                      |              |                                                                                             | Remove a brick from the design                         |
|                                                       | `parameters` | `brick`: a brick object                                                                     |                                                        |
|                                                       | `raises`     | `ValueError`: if you try to delete a brick that isn't in the design                         |                                                        |
| `design_interface.undo(n)`                            |              |                                                                                             | Undo the past `n` changes to the design space          |
|                                                       | `parameters` | `n` an integer: the number of elements of the undo stack to undo. Default = 1.              |                                                        |
|                                                       | `raises`     | `EmptyUndoStackError` if you try to undo more items than are in the undo stack              |                                                        |
| `design_interface.redo(n)`                            |              |                                                                                             |                                                        |
|                                                       | `parameters` | `n` an integer: the number of elements of the redo stack to redo. Default = 1.              | Redo the past `n` undo operations in the design space. |
|                                                       | `raises`     | `EmptyRedoStackError` if you try to redo more items than are in the undo stack              |                                                        |
