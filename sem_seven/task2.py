"""Task bout Road"""


class Road:

    # Defining the init function
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    # Defining the measurement function - mass
    def measurement_mass(self):
        return self._length * self._width


# Defining the second class - Calculation
class Calculation(Road):

    # Defining the init function
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume


# Checking if everything runs
result = Calculation(25, 10000, 125)
print(result.measurement_mass())
