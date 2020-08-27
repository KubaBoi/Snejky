import math

from Engine.vector import Vector

class Light:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.Vector = Vector(x, y, z)
        self.angle = 0

    def Update(self):
        #self.angle += 0.01
        self.x = math.sin(self.angle)
        self.z = math.cos(self.angle)
        self.Vector = Vector(self.x, self.y, self.z)
