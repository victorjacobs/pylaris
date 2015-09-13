class Hit:

    def __init__(self, ray, surface, point, normal):
        self.point = point
        self.ray = ray
        self.surface = surface
        self.normal = normal

    def color(self, scene):
        return self.surface.colorFor(self, scene)
