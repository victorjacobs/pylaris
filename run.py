from scene import Scene
from sphere import Sphere
from vector import Vector
from vector import Pixel
from settings import Settings
from camera import Camera
import itertools
from PIL import Image, ImageDraw


im = Image.new('RGBA', (Settings.screenX, Settings.screenY), (255,255,255,0))
ctx = ImageDraw.Draw(im)

camera = Camera(Vector(0, 0, 0), Vector(1, 0, 0), Vector(0, 0, 1))

scene = Scene()
scene.surfaces.append(Sphere(Vector(10, 0, 0), 3))

for (x, y) in itertools.product(range(0, Settings.screenX), range(0, Settings.screenY)):
    pixel = Pixel(x, y)
    ray = camera.rayToPixel(pixel)
    for surface in scene.surfaces:
        if surface.hit(ray, 0, 10000) is not None:
            ctx.point([(pixel.x, pixel.y)], (100, 100, 100, 1))

im.show()
