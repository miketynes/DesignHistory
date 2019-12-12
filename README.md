# DesignHistory
Design Space History Demo

Here I have written my code for my final assignment in Fordham's CISC 6100--software engineering. 

The project is supposed to be a team project, but due to some lapses in communication and availability alighment, I ended up re-coding 
portions of the assignment given to other teammates here. 

For the program modules, working from low-level to high-level modules, we have

| Module             | Description                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------------------|
| brick.py           |  The simplest design unit.   A brick has an ID, a position and an orientation.                                         |
| designspace.py     |  A singleton container for bricks to live inside of.   Supports add, move, and delete operations.                      |
| commands.py        |  A command-pattern wrapper to the interface to designspace.DesignSpace.    This allows operations to be neatly undone. |
| command_manager.py |  A controller object which executes the commands from commands.py.   This maintains and manages undo/redo history.     |


You should read the modules and their assocuated tests in this order.

The test modules are all self explanatory, with the exception of `test_design_space_ABC`, which just houses a common `setUp` method for multiple test
suites (*ergo* it is not a *true* ABC, but its easily recognizable as abstract). 

## Installation and Usage
To install and run this code, you only need a python3 interpreter. I ran all of my tests in python3.6.9 running on Ubuntu18.02.

It has no dependencies as it is mostly just a high-level design demo.

To run the tests, **from the project's root directory** run `python -m unittest discover test`. 

## API Reference

The API used here will differ from that in my team documentaiton. This is because I chose to use the command pattern to implement the design space's
move, add, and delete functionalities. Had we had time to discuss this both within my team and across the class teams, this would have
made it into our API reference. Alas, it did not. 

Further, using the command objects directly still may be abstracted far enough away from the actual design space code to use as our API, because the command 
objects need to be executed by the `CommandManager` to for history to be maintained. Currently in my code, one passes a `Command` obect
directly to the  `CommandManager`, which then executes the command and ...
