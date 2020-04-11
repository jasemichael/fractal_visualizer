import colour

class Gradient:
    def __init__(self):
        raise NotImplementedError("Concrete subclass of Gradient must implement __init__")

    def getColor(self):
        raise NotImplementedError("Concrete subclass of Gradient must implement getColor() method")

class BlackWhite(Gradient):
    def __init__(self, n):
        self.getColor(n)

    def getColor(self, n):
        black = colour.Color("black")
        white = colour.Color("white")
        gradient = list(black.range_to(white, 96))
        return gradient[n]

class BlueGreen(Gradient):
    def __init__(self, n):
        self.getColor(n)

    def getColor(self, n):
        blue = colour.Color("blue")
        green = colour.Color("green")
        gradient = list(blue.range_to(green, 96))
        return gradient[n]

class RedYellow(Gradient):
    def __init__(self, n):
        self.getColor(n)

    def getColor(self, n):
        red = colour.Color("red")
        yellow = colour.Color("yellow")
        gradient = list(red.range_to(yellow, 96))
        return gradient[n]