class LambertianMaterial:
    def __init__(self, color):
        self.color = color

    def colorFor(self, hit, scene):
        # Support only one light for now
        lightRay = scene.lights[0].rayto(hit.point)
        dot = hit.normal.dot(lightRay)

        return self.color.mult(dot).asTuple()