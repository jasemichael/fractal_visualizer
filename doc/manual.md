# Manual
This fractal program is very simple to use in creating a variety of fractal sets. 
To use, be sure to have the latest installation of Python as well as a bash terminal. Visit python.org/downloads for installation.
Open the terminal by clicking the terminal app icon and make sure the fractal program installation is located in the current directory.
Type 'ls' in the terminal and verify that the current directory contains a directory called 'src' within the listed files.
If the 'src' directory isn't within the current directory, change your current directory to the correct directory with 'cd directory_with_src'
where directory_with_src is the directory that contains the 'src' or move the 'src' directory into your currect directory. 
To run the program, type 'src/python main.py [FRACTAL_CONFIG [GRADIENT_CLASS]]' where FRACTAL_CONFIG is the file which contains the data for the image you want generated. 
GRADIENT_CLASS is the name of the gradient from which the colors are used. Currently supported gradients are "BlackWhite", "RedYellow", and "BlueGreen".
Fractal options are available by viewing the data directory.
'fullmandelbrot', 'spiral0', 'spiral1', 'seahorse', 'elephants', 'leaf', 'fulljulia', 'hourglass', and 'lakes' are some examples.
Once the command is executed, the program will begin to generate the fractal, pixel by pixel. 
The program will continue generating the image, until the image is complete. Afterwards, the image is saved into the same directory.
The program ends when the user closes the window.