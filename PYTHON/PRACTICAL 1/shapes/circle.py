import math

def area(radius):
    return math.pi * radius * radius

def perimeter(radius):
    return 2 * math.pi * radius



import math
from shapes.point import Point

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius



from shapes.point import Point