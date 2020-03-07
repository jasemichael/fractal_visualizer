# CS 1440 Assignment 4.1 Hints


## Experimentation

-   Use git branches liberally so you can easily retrace your steps and try
    again.
-   Generate fractal images before and after making sweeping changes so you can
    visually compare the program's output and detect mistakes.


## Generating color gradients

-   Use Python's  `colour`  module.  The `colour.Color` class makes computing a
    color gradient from one color to another very easy.
        -   `Color.range_to()` interpolates between two colors.
        -   `Color.get_hex_l()` presents a Color object as a `"#RRGGBB"` string
            which is compatible with `tkinter.PhotoImage`
-   If `import colour` causes this error:
    ```
    ModuleNotFoundError: No module named 'colour'
    ```
    You should install the `colour` package from the command line using this
    command:
    ```
    pip3 install --user colour
    ```
    If that fails, you may need to run this command as an Administrator (esp.
    if you originally installed Python "for all users").
    ```
    pip3 install colour
    ```


## Configuration file format

-   Process this file one line at a time, the same as we've done all semester long
-   Split lines into two pieces on the delimiter 
    -   Convert each line to lowercase as you read it
    -   Build up a dictionary one lowercase key at a time
-   Some numeric values must be integers while others are floats
    -   Use `float()` instead of `int()` to make floats from strings
    -   `complex(real, imag)` converts two real numbers into a complex number value


## Image quality

More detailed images can be obtained by specifying a large number of iterations
in the fractal configuration file.  However, the effect is lost when the
difference between two adjacent colors is slight.

The solution is to interpolate between more than two colors, preferably sharply
contrasting colors. The color gradients produced from your  `GradientFactory`
class can be made to interpolate over a list of colors of your choosing.


## Abstract classes

Python provides a standard library called `abc` (short for *Abstract Base
Class*) which is widely used to define abstract classes that cannot be
instantiated.  For our simple needs, `abc` does the exact same thing as
constructors that raise `NotImplementedError` by employing advanced Python
language features whose explanations are outside of the scope of this class.

I'm not saying that `abc` is bad or that you shouldn't ever use it; I am saying
that I do not encourage you to use `abc` for this assignment because it adds
complexity without benefit.  This assignment is complex enough already.

Relying on a module that you do not understand is a hallmark of cargo cult
programming.  If you insist on using `abc` anyway, you are on your own when you
run into problems.
