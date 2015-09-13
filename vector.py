from collections import namedtuple
import math


class Vector(namedtuple('Vector', 'x y z')):

    def dot(self, other):
        return self[0] * other[0] + self[1] * other[1] + self[2] * other[2]

    def norm(self):
        return math.sqrt(math.pow(self[0], 2) + math.pow(self[1], 2) + math.pow(self[2], 2))

    def sub(self, other):
        return self.__class__(self[0] - other[0], self[1] - other[1], self[2] - other[2])

    def add(self, other):
        return self.__class__(self[0] + other[0], self[1] + other[1], self[2] + other[2])

    def cross(self, other):
        c1 = self[1] * other[2] - self[2] * other[1]
        c2 = self[2] * other[0] - self[0] * other[2]
        c3 = self[0] * other[1] - self[1] * other[0]
        return self.__class__(c1, c2, c3)

    def div(self, scalar):
        return self.__class__(self[0] / scalar, self[1] / scalar, self[2] / scalar)

    def mult(self, scalar):
        return self.__class__(self[0] * scalar, self[1] * scalar, self[2] * scalar)

    def normalized(self):
        return self.div(self.norm())

    def neg(self):
        return self.__class__(0, 0, 0).sub(self)


class Pixel(namedtuple('Pixel', 'x y')):
    pass


class Color(namedtuple('Color', 'r g b'), Vector):

    def asTuple(self):
        return round(self.r), round(self.g), round(self.b), 1
