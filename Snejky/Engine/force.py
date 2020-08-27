from Engine.vector import Vector
import time

class Force(Vector):
    def __init__(self, x, y, z, a=1):
        Vector.__init__(self, x, y, z)
        self.actual = Vector(0,0,0)
        
        self.a = Vector(x/a, y/a, z/a)
        #self.a.speak()

        self.t = 0
        self.time = abs(a)

    #v = v0 + at
    #v0 - pocatecni rychlost (velikost prvku vektoru)
    #a - zrychleni (velikost prvku vektoru *-1)
    def update(self, deltaTime):
        self.t += deltaTime

        if (self.t <= self.time):
            self.actual.x = self.x - self.a.x*self.t
            self.actual.y = self.y - self.a.y*self.t
            self.actual.z = self.z - self.a.z*self.t
        else:
            return Vector(0,0,0)
        
        return self.actual
