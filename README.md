# CS 1440 Assignment 4: Refactoring & Design Patterns


## 4.0: Refactoring
* [Instructions](doc/Instructions-4.0.md)
* [Hints](doc/Hints-4.0.md)
* [Rubric](doc/Rubric-4.0.md)


## 4.1: Design Patterns
* [Instructions](doc/Instructions-4.1.md)
* [Hints](doc/Hints-4.1.md)
* [Rubric](doc/Rubric-4.1.md)


## Overview

Our firm has been contracted to help a mathematician take his amazing
one-million dollar idea to market.  Our client specializes in the field of
complex dynamics, which, frankly, is well above my pay grade, but so is
programming to him.  He has a passion for mathematics education and wants to
take his programs to the K-12 system to teach middle and high-school students
all about the beauty of complex numbers and repeated, tedious calculations.  I
didn't have the heart to tell him that there are already dozens of websites
doing what he wants to do for free; if his inability to use Google keeps us in
steady work, who am I to set him straight?

He has created two prototype programs intended for high school math students.
He quickly realized that creating user-friendly software is perhaps more
difficult than understanding complex dynamics.  This is where we come in.

Our contract is to adapt his programs into a complete *Programming Systems
Product*.  We must also make it usable by non-programmers, which means that
instead of controlling the program by changing hard-coded data within the
source code it must accept configuration files from the command-line and
adjust its runtime behavior accordingly.

Now, I realize that asking a user to create configuration files and run a
program from the command-line is no longer considered user-friendly in the
21st century.  We have two teams working on this project: one team will be
creating a GUI which is what the students will ultimately interact with.  This
GUI will drive the core program that you will create.  Your responsibility is
to make sure that your piece of the Program System adheres to the
configuration file format that the GUI team has defined, as well as the
command-line interface they are expecting.



## Running the starter code

These programs given have a simple command line syntax:

    python src/mbrot_fractal.py [FRACTAL_NAME]
    python src/julia_fractal.py [FRACTAL_NAME]

`FRACTAL_NAME` is the name of a fractal image this program is capable of
producing.  When you run either program without an argument it will list names
of images it can draw and exits.

If you use PyCharm you should create **Run configurations** to launch the
program with various arguments.



## Interactive Mandelbrot Viewer Demo

It is not strictly necessary for you to understand the math behind these
fractals in order to refactor this program.  However, some of you won't feel
confident until you understand what's going on.  To this end I have provided an
interactive Mandelbrot program called [demo/interactive.py](demo/interactive.py)

*   Left-Clicking the image will paint a square using the same algorithm that
    the [src/mbrot_fractal.py](src/mbrot_fractal.py) program uses, except this
    program will print to the console the values of the Z parameter at each
    iteration as well as display the iteration count.
*   Right-Clicking the Canvas reveals the entire image at once.

By reading the demo program's source code, running it in the debugger and
reading its output may help you better understand how your program produces its
images.

**Important:** [demo/interactive.py](demo/interactive.py) is provided for your
amusement/benefit.  It is *not* a part of the assignment, and you *are not*
required to improve it or document it.
