import sys, Config, Gradient, ImagePainter

def checkArgs(configs):
    if len(sys.argv) < 2:
        print("Please provide the name of a fractal as an argument")
        for config in configs:
            print(f"\t{config}")
        sys.exit(1)

    elif sys.argv[1] not in configs:
        print(f"ERROR: {sys.argv[1]} is not a valid fractal\nPlease choose one of the following:")
        for config in configs:
            print(f"\t{config}")
        sys.exit(1)

def run(configs):
    fractalType = configs[sys.argv[1]]['type']
    gradient = Gradient.getGradient()
    ImagePainter.draw(configs, sys.argv[1], fractalType, gradient)

def main(configs):
    checkArgs(configs)
    run(configs)


if __name__ == '__main__':
    main(Config.getConfigs())
