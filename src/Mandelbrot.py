#!/bin/env python3

# Mandelbrot Set Visualizer

import sys
from tkinter import Tk, Canvas, PhotoImage, mainloop


# This color gradient contains 100 color steps.
gradient = [
        '#ffe4b5', '#ffe5b2', '#ffe7ae', '#ffe9ab', '#ffeaa8', '#ffeda4',
        '#ffefa1', '#fff29e', '#fff49a', '#fff797', '#fffb94', '#fffe90',
        '#fcff8d', '#f8ff8a', '#f4ff86', '#f0ff83', '#ebff80', '#e7ff7c',
        '#e2ff79', '#ddff76', '#d7ff72', '#d2ff6f', '#ccff6c', '#c6ff68',
        '#bfff65', '#b9ff62', '#b2ff5e', '#abff5b', '#a4ff58', '#9dff54',
        '#95ff51', '#8dff4e', '#85ff4a', '#7dff47', '#75ff44', '#6cff40',
        '#63ff3d', '#5aff3a', '#51ff36', '#47ff33', '#3eff30', '#34ff2c',
        '#2aff29', '#26ff2c', '#22ff30', '#1fff34', '#1cff38', '#18ff3d',
        '#15ff42', '#11ff47', '#0eff4c', '#0bff51', '#07ff57', '#04ff5d',
        '#01ff63', '#00fc69', '#00f970', '#00f677', '#00f27d', '#00ef83',
        '#00ec89', '#00e88e', '#00e594', '#00e299', '#00de9e', '#00dba3',
        '#00d8a7', '#00d4ab', '#00d1af', '#00ceb3', '#00cab7', '#00c7ba',
        '#00c4be', '#00c0c0', '#00b7bd', '#00adba', '#00a4b6', '#009cb3',
        '#0093b0', '#008bac', '#0082a9', '#007ba6', '#0073a2', '#006b9f',
        '#00649c', '#005d98', '#005695', '#004f92', '#00498e', '#00438b',
        '#003d88', '#003784', '#003181', '#002c7e', '#00277a', '#002277',
        ]

MAX_ITERATIONS = len(gradient)
z = 0


def colorOfThePixel(c, gradient):
    """Return the color of the current pixel within the Mandelbrot set"""
    global z
    z = complex(0, 0)  # z0

    global MAX_ITERATIONS
    global i

    for i in range(MAX_ITERATIONS):
        z = z * z + c  # Get z1, z2, ...
        if abs(z) > 2:
            z = 2.0
            return gradient[i]  # The sequence is unbounded
    # XXX: one of these return statements made the program crash...
    return gradient[MAX_ITERATIONS - 1]   # Indicate a bounded sequence
    return gradient[MAX_ITERATIONS]


def paint(fractals, imagename):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    This code creates an image which is 640x640 pixels in size."""

    global gradient
    global img

    fractal = fractals[imagename]

    # Figure out how the boundaries of the PhotoImage relate to coordinates on
    # the imaginary plane.
    minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)
    maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)
    miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)
    maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)

    # Display the image on the screen
    canvas = Canvas(window, width=512, height=512, bg='#ffffff')
    canvas.pack()
    canvas.create_image((256, 256), image=img, state="normal")

    # At this scale, how much length and height on the imaginary plane does one
    # pixel take?
    pixelsize = abs(maxx - minx) / 512

    portion = int(512 / 64)
    total_pixels = 1048576
    for row in range(512, 0, -1):
        for col in range(512):
            x = minx + col * pixelsize
            y = miny + row * pixelsize
            color = colorOfThePixel(complex(x, y), gradient)
            img.put(color, (col, 512 - row))
        window.update()  # display a row of pixels


def pixelsWrittenSoFar(rows, cols):
    pixels = rows * cols
    print(f"{pixels} pixels have been output so far")
    return pixels


# These are the different views of the Mandelbrot set you can make with this
# program.
#
# For convenience I have placed these into a dictionary so you may easily
# switch between them by entering the name of the image you want to generate
# into the variable 'image'.
images = {
        'fullmandelbrot': {
            'centerX': -0.6,
            'centerY': 0.0,
            'axisLen': 2.5,
            },

        'spiral0': {
            'centerX': -0.761335372924805,
            'centerY': 0.0835704803466797,
            'axisLen': 0.004978179931102462,
            },

        'spiral1': {
            'centerX': -0.747,
            'centerY': 0.1075,
            'axisLen': 0.002,
            },

        'seahorse': {
            'centerX': -0.745,
            'centerY': 0.105,
            'axisLen': 0.01,
            },

        'elephants': {
            'centerX':  0.30820836067024604,
            'centerY':  0.030620936230004017,
            'axisLen':  0.03,
            },

        'leaf': {
            'centerX': -1.543577002,
            'centerY': -0.000058690069,
            'axisLen':  0.000051248888,
            },
        }


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the name of a fractal as an argument")
        for i in images:
            print(f"\t{i}")
        sys.exit(1)

    elif sys.argv[1] not in images:
        print(f"ERROR: {sys.argv[1]} is not a valid fractal")
        print("Please choose one of the following:")
        for i in images:
            print(f"\t{i}")
        sys.exit(1)

    else:
        image = sys.argv[1]


    # Set up the GUI so that we can paint the fractal image on the screen
    window = Tk()
    img = PhotoImage(width=512, height=512)
    paint(images, image)

    # Save the image as a PNG
    img.write(f"{image}.png")
    print(f"Wrote image {image}.png")

    # Call tkinter.mainloop so the GUI remains open
    mainloop()
