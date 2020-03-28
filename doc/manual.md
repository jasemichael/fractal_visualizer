# Manual
This fractal program is very simple to use in creating Julia and Mandelbrot sets. 
To use, be sure to have the latest installation of Python as well as a bash terminal. Visit python.org/downloads for installation.
Open the terminal by clicking the terminal app icon and make sure the fractal program installation is located in the current directory.
Type 'ls' in the terminal and verify that the current directory contains a directory called 'src' within the listed files.
If the 'src' directory isn't within the current directory, change your current directory to the correct directory with 'cd directory_with_src'
where directory_with_src is the directory that contains the 'src' or move the 'src' directory into your currect directory. 
To run the program, type 'src/python main.py fractal' where fractal is the type of image you want generated. 
Fractal options are available by typing 'src/python main.py'. Fractals include:
'fullmandelbrot', 'spiral0', 'spiral1', 'seahorse', 'elephants', 'leaf', 'fulljulia', 'hourglass', and 'lakes'.
Once the command is executed, the program will begin to generate the fractal, pixel by pixel. 
The program will continue generating the image, until the image is complete. Afterwards, the image is saved into the same directory.
The program ends when the user closes the window.