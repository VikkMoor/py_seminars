"""Task bout Road class.
Implement a public method for calculating the mass of asphalt required for pavement.
Use the formula: (length) * (width) * (mass of asphalt to cover one square
meters of the road with depth of asphalt = 1 cm) * number of depth of asphalt pavement (in meters)"""


class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width, weight, depth):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.depth = depth

    def mass(self):
        lens = self._length
        wid = self._width
        w = self.weight
        dep = self.depth
        all_mass = lens * wid * w * dep
        return print(
            f"Масса асфальта\n {lens}м * {wid}м * {w}кг * {dep}м = {round(all_mass)}кг = {round(all_mass / 1000)}т")


r = Road(20, 5000, 25, 0.05)
r.mass()
