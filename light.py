class PointLight:
    def __init__(self, position, intensity):
        self.intensity = intensity
        self.position = position

    def rayto(self, point):
        return self.position.sub(point).normalized()