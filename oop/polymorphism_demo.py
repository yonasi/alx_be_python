import math

class Shape:

    def area(self):
        raise NotImplementedError("area method not implenented")
    

class Rectangle(Shape):
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
