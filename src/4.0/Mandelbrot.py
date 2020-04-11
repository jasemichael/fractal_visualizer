#!/bin/env python3

# Mandelbrot Set Visualizer

def getMandelbrotPixelColor(c, gradient):
    """Return the color of the current pixel within the Mandelbrot set"""
    z = complex(0, 0)  # z0
    for i in range(len(gradient)):
        z = z * z + c  # Get z1, z2, ...
        if abs(z) > 2:
            z = 2.0
            return gradient[i]  # The sequence is unbounded
    return gradient[len(gradient) - 1]   # Indicate a bounded sequence