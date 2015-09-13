from scene import Scene
from sphere import Sphere
from vector import *
from settings import Settings
from camera import Camera
from light import *
import itertools
from PIL import Image, ImageDraw
from lambertianMaterial import LambertianMaterial


im = Image.new('RGBA', (Settings.screenX, Settings.screenY), (128, 128 ,128 ,0))
ctx = ImageDraw.Draw(im)

camera = Camera(Vector(0, 0, 0), Vector(1, 0, 0), Vector(0, 0, 1))

scene = Scene()
scene.surfaces.append(Sphere(Vector(10, 0, 0), 3, LambertianMaterial(Color(255, 0, 0))))
scene.surfaces.append(Sphere(Vector(10, 7, 0), 3, LambertianMaterial(Color(0, 255, 0))))
scene.lights.append(PointLight(Vector(0, 0, 3), 1))

for (x, y) in itertools.product(range(0, Settings.screenX), range(0, Settings.screenY)):
    pixel = Pixel(x, y)
    ray = camera.rayToPixel(pixel)
    for surface in scene.surfaces:
        hit = surface.hit(ray, 0, 10000)
        if hit is not None:
            ctx.point([(pixel.x, pixel.y)], hit.color(scene))

im.show()
