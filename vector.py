from collections import namedtuple
import math


class Vector(namedtuple('Vector', 'x y z')):

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def norm(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2))

    def sub(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def cross(self, other):
        c1 = self.y * other.z - self.z * other.y
        c2 = self.z * other.x - self.x * other.z
        c3 = self.x * other.y - self.y * other.x
        return Vector(c1, c2, c3)

    def div(self, scalar):
        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)

    def mult(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def normalized(self):
        return self.div(self.norm())

    def neg(self):
        return Vector(0, 0, 0).sub(self)


class Pixel(namedtuple('Pixel', 'x y')):
    pass