import Fractal

def makeFractal(fractal='julia'):
    if fractal == 'julia':
        return Fractal.Julia
    elif fractal == 'mandelbrot':
        return Fractal.Mandelbrot
    elif fractal == 'mandelbrot3':
        return Fractal.Mandelbrot3
    else:
        raise NotImplementedError("Invalid fractal request!")