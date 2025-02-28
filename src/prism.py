from math import pi

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    def surface_area(self):
      return 2 * (pi * self.radius**2) + (2 * pi * self.radius * self.height)


class SquarePrism(Cylinder):
    def __init__(self, width, height):
        super().__init__(None, height)
        self.width = width
    def surface_area(self):
        return 2 * (self.width ** 2) + (4 * self.width * self.height)

c = Cylinder(1, 2)
print(c.surface_area())

sp = SquarePrism(1, 2)
print(sp.surface_area())
