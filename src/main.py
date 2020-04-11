import sys, ImagePainter, FractalFactory, GradientFactory

def run():
    if len(sys.argv) < 2:
        print("FractalFactory: Creating default fractal\nGradientFactory: Creating default color gradient")
    elif len(sys.argv) < 3:
        print("GradientFactory: Creating default color gradient")
    d = {}
    file = open(sys.argv[1])
    for line in file:
        if line[0] != "#":
            line = line.split(': ')
            d[line[0].lower()] = line[1].strip("\n").lower()
    fractal = FractalFactory.makeFractal(fractal=d['type'])
    gradient = GradientFactory.makeGradient(sys.argv[2])
    ImagePainter.draw(d, fractal, gradient, sys.argv[1])



if __name__ == '__main__':
    run()