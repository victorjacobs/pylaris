from vector import Vector
from settings import Settings
from ray import Ray
import math


class Camera:
    def __init__(self, position, gaze, up):
        self.up = up
        self.gaze = gaze
        self.position = position
        self.distanceToScreen = 4
        self.fov = 90

    def rayToPixel(self, pixel):
        aspectRatio = Settings.screenX / Settings.screenY

        r = self.distanceToScreen * math.tan(self.fov / 2)
        l = -r
        t = aspectRatio * l
        b = -t

        u = l + ((r - l) * (pixel.x + 0.5)) / Settings.screenX
        v = b + ((t - b) * (pixel.y + 0.5)) / Settings.screenY

        direction1 = self.w().mult(self.distanceToScreen).neg()
        direction2 = self.u().mult(u)
        direction3 = self.v().mult(v)

        direction = direction1.add(direction2.add(direction3))

        return Ray(self.position, direction.normalized())

    def w(self):
        return self.gaze.normalized().neg()

    def u(self):
        return self.up.cross(self.w()).normalized()

    def v(self):
        return self.w().cross(self.u())