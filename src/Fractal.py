class Fractal:
    def __init__(self):
        raise NotImplementedError("Concrete subclass of Fractal must implement __init__")

    def count(self):
        raise NotImplementedError("Concrete subclass of Fractal must implement count() method")

class Julia(Fractal):
    def __init__(self, c_num):
        self.count(c_num)

    def count(self, c_num):
        c = complex(-1.0, 0.0)
        for i in range(96):
            c_num = c_num * c_num + c  # Get z1, z2, ...
            if abs(c_num) > 2:
                z = 2.0
                return i  # The sequence is unbounded
        return 96 - 1  # Indicate a bounded sequence

class Mandelbrot(Fractal):
    def __init__(self, c_num):
        self.count(c_num)

    def count(self, c_num):
        z = complex(0, 0)  # z0
        for i in range(96):
            z = z * z + c_num  # Get z1, z2, ...
            if abs(z) > 2:
                z = 2.0
                return i  # The sequence is unbounded
        return 96 - 1  # Indicate a bounded sequence

class Mandelbrot3(Fractal):
    def __init__(self, c_num):
        self.count(c_num)

    def count(self, c_num):
        z = complex(0, 0)  # z0
        for i in range(96):
            z = z * z * z + c_num  # Get z1, z2, ...
            if abs(z) > 2:
                z = 2.0
                return i  # The sequence is unbounded
        return 96 - 1  # Indicate a bounded sequence