from surface import Surface
import math
import vector


class Sphere(Surface):
    def __init__(self, center, radius):
        super().__init__()
        self.center = center
        self.radius = radius

    def hit(self, ray, t0, t1):
        a = ray.direction.dot(ray.direction)
        b = ray.origin.sub(self.center).mult(2).dot(ray.direction)
        c1 = ray.origin.sub(self.center)
        c = c1.dot(c1) - self.radius * self.radius

        discriminant = math.pow(b, 2) - 4 * a * c
        if discriminant < 0:
            return None

        tPlus = (-b + math.sqrt(discriminant)) / (2 * a)
        tMin = (-b - math.sqrt(discriminant)) / (2 * a)

        if t0 < tMin < t1:
            t = tMin
        elif t0 < tPlus < t1:
            t = tPlus
        else:
            return None

        return t
