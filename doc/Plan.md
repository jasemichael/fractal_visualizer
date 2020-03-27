# Plan
## Requirements
### Code Smells
#### julia_fractal.py
Line 18, global vars are used
```    
    global grad
    global win
```
should be passed in as function paramaters.

Line 9, parameter name z is confusing
```
def getColorFromGradient(z):
```
should be a name that is understood

Line 21, there are more than 76 colors in gradient and the loop iterates through 78
```
# Here 76 refers to the number of colors in the gradient
    for i in range(78):
```
comments should be accurate as well as loop

Line 25, code is never reached
```
return grad[i]  # The sequence is unbounded
z += z + c
```
delete the expression after return

Line 27, todo should explicitly name what to fix not the problem
```
# TODO: One of these return statements makes the program crash sometimes
```
edit line to specify what to accomplish

Line 28, code is never reached
```
return grad[77]         # Else this is a bounded sequence
return grad[78]
```
delete next return statement

Line 32, function name is too long
```
def getFractalConfigurationDataFromFractalRepositoryDictionary(dictionary, name):
```
change to something informative, yet concise

Line 33, docstring is too informative
```
"""Make sure that the fractal configuration data repository dictionary
    contains a key by the name of 'name'

    When the key 'name' is present in the fractal configuration data repository
    dictionary, return its value.

    Return False otherwise
    """
```
make it more concise

Line 44, variable is never used
```
value = dictionary[key]
```
delete variable

Line 48, function parameters are too short and uninformative
```
def makePicture(f, i, e):
```
rename parameters to something informative and understandable

Line 52, global variables are used
```
def makePicture(f, i, e):
```
pass global variables in as parameters

Line 64, global variable used
```
global WHITE
```
remove global declaration

Line 68, TODO doesn't have todo item; just some contemplative phrase about programming
```
# TODO: Sometimes I wonder whether some of my functions are trying to do
    #       too many different things... this is the correct part of the
    #       program to create a GUI window, right?
```
if todo is needed, write, else remove

Line 72, comments are adding on to previous clients comments--comments are helping explain code
```
canvas.pack()  # This seems repetitive
    canvas.pack()  # But it is how Larry wrote it
    canvas.pack()  # Larry's a smart guy.  I'm sure he has his reasons.
```
remove comments or provide insight into each comment

Line 76, variable isn't used
```
area_in_pixels = 512 * 512
```
remove the variable declaration or use it

Line 78, comments are unnecessary
```
canvas.pack()  # Does this even matter?
    # At this scale, how much length and height of the
    # imaginary plane does one pixel cover?
```
remove comments

Line 84, variable is unused
```
fraction = int(512 / 64)
```
remove variable declaration or use it

Line 94, excessive comments describing the gradients; todo isn't explicit
```
# This is the color gradient, which defines the palette that images are drawn
# in as well as limiting the number of iterations the escape-time algorithm uses
#
# TODO: It would be nice to add more or different colors to this list, but it's
# just so much work to calculate all of the in-between shades!
```
remove the code; add a todo about adding additional colors

Line 119, excessive comments describing command-line arguments; todo is implicit
```
# This dictionary contains the different views of the Julia set you can make
# with this program.
#
# For convenience I have placed these into a dictionary so you may easily
# switch between them by entering the name of the image you want to generate
# into the variable 'i'.
#
# TODO: Maybe it would be a good idea to incorporate the complex value `c` into
# this configuration dictionary instead of hardcoding it into this program?
```
remove or clarify comments; delete todo because c isn't relevent to data

Line 153, contains main code for running; redundant with mbrot_fractal
```
if __name__ == '__main__':
```
code after conditional should be used in main() module

Line 162, print statements are redundant
```
print(f"ERROR: {sys.argv[1]} is not a valid fractal")
print("Please choose one of the following:")
```
combine print statement into a single statement

Line 179, image is written twice
```
photo.write(i + ".png")
print("Wrote picture " + i + ".png")
photo.write(i + ".png")
```
delete the newest photo.write()

### mbrot_fractal.py
Line 30, variable isn't descriptive
```
z = 0
```
change variable name to thoroughly describe some value

Line 33, function name doesn't describe functionality
```def colorOfThePixel(c, gradient):```
rename function to simply describe functionality

Line 35, global variables are called and used
```
global z
z = complex(0, 0)  # z0

global MAX_ITERATIONS
global i
```
use global variables as parameters to function; remove z in global scope because z is only used in this function

Line 46, comment isn't useful in providing context; return statement is never reached
```
# XXX: one of these return statements made the program crash...
return gradient[MAX_ITERATIONS - 1]   # Indicate a bounded sequence
return gradient[MAX_ITERATIONS]
```
remove return gradient[MAX_ITERATIONS] and comment

Line 55, global variables are used
```
global gradient
global img
```
use global variables are parameters into function

Line 60, comment is interrupting and unnecessary
```
# Figure out how the boundaries of the PhotoImage relate to coordinates on
    # the imaginary plane.
```
add a todo or solve logical problem

Line 65, variable is never used
```
maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)
```
delete variable declaration

Line 72, comment poses question
```
# At this scale, how much length and height on the imaginary plane does one
    # pixel take?
```
declare functionality of code

Line 76, variables are declared buy unused
```
portion = int(512 / 64)
total_pixels = 1048576
```
delete the variable declaration

Line 87, function name doesn't simplify functionality
```
def pixelsWrittenSoFar(rows, cols):
```
add verb to function to identify function usage

Line 93, comments are long and unnecessary
```
# These are the different views of the Mandelbrot set you can make with this
# program.
#
# For convenience I have placed these into a dictionary so you may easily
# switch between them by entering the name of the image you want to generate
# into the variable 'image'.
```
Reduce clutter or remove overall

Line 138, main() isn't regulating control
```
if __name__ == '__main__':
```
move code into main()

Line 146, print statements are redundant
```
        print(f"ERROR: {sys.argv[1]} is not a valid fractal")
        print("Please choose one of the following:")
```
combine statements into a single print statement

## Design
### main.py
Contains main() function. Regulates control of program.
### Config.py

### Gradient.py
### ImagePainter.py
### Julia.py
### Mandelbrot.py

## Implementation
## Verification/Validation
### Integration Test
### Unit Tests