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
| designcontroller.py |  `designcontroller.DesignController` executes the commands from commands.py, maintains undo/redo history, and provides `undo` and `redo` methods which are global to the design space state. 
| design_interface.py | A thin wrapper to designcontroller.py which hides information for the user (i.e. other teams on the project).                                                                                                                      |


You should read the modules and their assocuated tests in this order.

The test modules are all self explanatory, with the exception of `test_design_space_ABC`, which just houses a common `setUp` method for multiple test
suites (*ergo* it is not a *true* ABC, but its easily recognizable as abstract). 

## Installation and Usage
To install and run this code, you only need a python3 interpreter. I ran all of my tests in python3.6.9 running on Ubuntu18.02.

It has no dependencies as it is mostly just a high-level design demo.

To run the tests, **from the project's root directory** run `python -m unittest discover test`. 

## API Reference
