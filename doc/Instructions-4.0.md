# CS 1440 Assignment 4.0 Instructions

## Overview

You have been assigned to a high-priority project at DuckieCorp to convert a
client's prototype program into a well-factored Programming Systems Product
complete with design and user documentation.  You will work on this project
over two sprints.

Our client wants DuckieCorp to add new features to his starter code.  While
this starter code does not contain any obvious bugs, in its current state it is
not easy to improve upon.  To be perfectly frank, this code is a bit of a mess,
and the client knows it.  Before we can deliver them we must first address the
non-functional aspects of the code base.

In this sprint you will refactor this program into a cleaner, more pliant code
base while keeping the *original functionality intact*.  It is important at
this stage to resist the urge to improve this program's functionality or
performance.

Pure refactoring is about *preserving* existing functionality, even if that
functionality is incorrect.  In the next sprint (Assignment 4.1) you will
complete this project by enhancing the system with new capabilities.

_This is not a hint for you to go looking for some cleverly-hidden bug; there
are no easter-eggs.  Refactor the starter code under the assumption that it
works correctly._  


## Objectives

*   Understanding code written by others
    *   Practice reading messy code
    *   Study official documentation
*   Create a Programming System
    *   Organize procedural code into modules
    *   Run and maintain Unit Tests
    *   Use integration tests to avoid introducing new bugs
*   Create a Programming Product
    *   Write user-oriented documentation
    *   Draft a UML class diagram describing the system's architecture
*   Refactoring
    *   Identify "code smells": programming anti-patterns
    *   Factor out redundant code
    *   Split monolithic code into neat, clean modules
*   Leverage 3rd party libraries to create a fun and visually appealing program


## Submission Instructions

You will be working in this repository for two sprints.  Tag the final commit
of this sprint `Assn4.0`.  This tag must be *exactly* the string `Assn4.0`, not
`Assn4`, nor `assn4`, nor `ASSN4`, nor `Assign4`.
Push this tag to GitLab before the due date.  

The `Assn4.0` tag tells the graders which commit to grade for this submission.
This way you may continue to work in this repository and we won't interpret
your Assignment 4.1 commits as late submissions.


## Requirements

### Identify code smells

Begin by cloning and studying the starter code.  Catalogue code smells you
encounter in the *Requirements* section of your Software Development Plan.
State the offending filename and line number.  Quote a sample of source code in
Markdown by writing it in between triple-backquotes ```` ``` ````, like this:

~~~
This passage found in the file src/Frobz.py at line 42 is overly complex:

```
if a == True or bool(a):
    b = a
else:
    b = not a

return b
```

It can be replaced with a simple return statement without changing the meaning
of the program:

```
return bool(a)
```
~~~

Be on the lookout for issues which get in the way of enhancing this program:

-   Functions which do many unrelated things
-   Variables and functions which are unused
-   Variables whose names override other identifiers
-   Poorly named identifiers
-   "Magic" numbers
-   Unnecessary code that serves no useful purpose in the program
-   Redundant code that repeats an operation to no useful end
-   Dead code; statements that cannot be run due to the structure of the program
-   Operations which are spread throughout the program instead of being encapsulated in one place
-   Confusing or contradictory comments


### Factor out redundancy

You begin this sprint with two independent programs.  Finish this sprint with a
single modular program that is capable of displaying both types of fractals.

These programs share common features and much of their code is redundant.
Identify passages of code that perform essentially the same tasks and rewrite
it so that duplication is eliminated.


### Separate code into modules

You begin this sprint with two monolithic programs.  A monolithic program is a
single file which contains every line of code it needs to run (and some lines
it *doesn't* need).

Finish this sprint with a carefully organized *modular* program.  Each module
will encapsulate a certain behavior or aspect of the program and provide a
well-defined interface to the other modules. This will enable you to easily add
new functionality next sprint.

These modules  _may_  be implemented as classes now, but this isn't a
requirement for this sprint.  It is enough for each Python file to be a
collection of functions and variables. _Keep in mind that a goal in the next
sprint is to apply the Object-Oriented techniques of Inheritance and
Polymorphism to this program._

In the end your project should include these six modules _at minimum:_

0.  `main.py`  - The driver program; imports other modules, accepts
    command-line arguments and calls upon other modules to display a fractal
    on-screen and write a PNG image.  This file is the main entry point of the
    program.
1.  `Config.py`  - Contains a Python dictionary composed of fractal
    configuration data
2.  `Mandelbrot.py`  - Given a coordinate in the complex plane, return the
    iteration count of the Mandelbrot function for that point
3.  `Julia.py`  - Given a coordinate in the complex plane, return the iteration
    count of the Julia function for that point
4.  `Gradient.py`  - Contains an array `G` containing `N` colors; when the
    Mandelbrot or Julia fractal function returns an iteration count of a point
    in the complex plane, the corresponding pixel is painted `G[count]`
5.  `ImagePainter.py`  - Creates a `Tk` window and a  `PhotoImage`  object; the
    `PhotoImage`  stores the pixels and is capable of creating a PNG image file

You may create other modules as you see fit.

Mind the capitalization of these filenames.  Windows users may get away with
naming these files in lowercase but such code *will break* when run on Mac or
Linux.


### Rely on tests to ensure quality

#### Unit tests

The starter code is supplied with a few unit tests.  You are encouraged to
augment these tests as you work.  Some of these tests provided aren't helpful.
Other tests will need to be rewritten as you refactor the programs.  Use the
unit tests as your "canary in the coal mine" warning you of mistakes.

#### Integration tests

Integration testing is done by analyzing the image files left behind by the
program.  Keep samples of the output images generated by the starter code
before making any changes to it.  As you refactor the fractal algorithms your
program should *always* produce identical images.  When an output image differs
from before, you will know you have made a mistake.


### Fractal configuration information

The starter programs contain a dictionary holding parameters used by the
drawing routine to render an image of a region of the complex plane.  Each item
of this dictionary has a name which, when given on the command line, results in
that image being displayed.

When a missing or invalid argument is given to either program, the keys of this
dictionary are printed in a usage message instructing the user how to correctly
invoke the program.

Extract the contents of these dictionaries from the starter programs and unite
them in one dictionary in the `Config.py` module.  To distinguish Julia
fractals from Mandelbrot fractals add a new key/value pair to each dictionary:

```
'type': 'julia',
```

or

```
'type': 'mandelbrot',
```

This piece of information will be used by your program to determine whether to
call the Mandelbrot or Julia function to choose the color of each pixel.

You may add new fractal configurations to the configuration dictionary.  Do not
remove the configurations present in the starter code as these images are used
when grading your submission.

Next sprint this program will be made to accept the name of a fractal
configuration file from the command-line so that one does not need to hack the
source code each time they want to produce a new image.  The GUI team has
translated the hard-coded fractal configurations into the sample configuration
files you will find in the `data/` directory.  You may disregard these files in
the first sprint of this project.


### Retain the command line interface

When no argument is supplied to `main.py` all of the choices are displayed to
the user:

```
$ python main.py
Usage: main.py FRACTALNAME
Where FRACTALNAME is one of:
	fulljulia
	hourglass
	lakes
	fullmandelbrot
	spiral0
	spiral1
	seahorse
	elephants
	leaf
```

An invalid argument is reported as an error and is followed by the usage message:

```
$ python main.py moustache
ERROR: moustache is not a valid fractal
Please choose one of the following:
	fulljulia
	hourglass
	lakes
	fullmandelbrot
	spiral0
	spiral1
	seahorse
	elephants
	leaf
```


### Draft a UML class diagram describing your design

You are working alongside another DuckieCorp team who is creating a
user-friendly GUI for our client's program (_not really, just pretend with me
here_). It helps them immensely to understand how your code is organized.
Submit a UML class diagram describing the modules, their relationships, and the
key functions/methods/data members involved. You don't have to use classes in
your implementation in this stage, but be aware that they will required in the
next sprint. For purposes of this diagram, a Python module is equivalent to a
class.

Commit your UML diagram in your repository under the  `doc/`  directory. If you
made your diagram on https://draw.io, uncheck the "Transparent Background"
option when you export your UML class diagram to a PNG image.


### Write a user's manual explaining how to use your program

This won't be the final version of the program, nor is this command-line
interface be what will be delivered to our client. However, other
non-programmer employees will need to know how to use this program (Quality
Assurance testers, Client Services, Sales Demo Technicians, Technical Support)
so there is a need for well-written instructions. It should not be long;
between 1 or 2 kilobytes of plain text is plenty, no larger than 4 kilobytes,
please.

Commit your user's manual in your repository as a file named  `doc/manual.md`.
