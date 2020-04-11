import sys, ImagePainter, FractalFactory, GradientFactory

def run():
    if len(sys.argv) < 2:
        print("No .frac file specified.\nUsage: python src/main.py [FRACTAL_FILE [GRADIENT]]")
        sys.exit(1)
    elif len(sys.argv) < 3:
        print("FractalFactory: Creating default fractal\nGradientFactory: Creating default color gradient")
        sys.argv.append("BlackWhite")
    elif len(sys.argv) < 4:
        print("GradientFactory: Creating default color gradient")
        sys.argv.append("BlackWhite")
    d = {}
    file = open(sys.argv[1])
    for line in file:
        if line[0] != "#" and line[0] != '\n':
            line = line.split(':')
            d[line[0].lower()] = line[1].strip().lower()
    #check config values
    try:
        d['centerx'] = float(d['centerx'])
        d['centery'] = float(d['centery'])
        d['type'] = str(d['type'])
        d['axislength'] = float(d['axislength'])
        d['pixels'] = int(d['pixels'])
        d['iterations'] = int(d['iterations'])
    except:
        raise NotImplementedError("Incorrect format in fractal configuration file")

    fractal = FractalFactory.makeFractal(fractal=d['type'])
    gradient = GradientFactory.makeGradient(sys.argv[2])
    ImagePainter.draw(d, fractal, gradient, sys.argv[1])

if __name__ == '__main__':
    run()