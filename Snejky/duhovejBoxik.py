from Engine.vector import Vector
from Engine.camera import Camera
from Engine.vertex import Vertex
from Engine.mesh import Mesh
from Engine.face import Face
from Engine.object3D import Object3D
from Engine.meshes.cube import Cube
from Engine.force import Force

import random

class DuhovyBoxik(Cube):
    def __init__(self, engine, x, y, z, scale, color=None, rigidBody=False):
        Cube.__init__(self, engine, x, y, z, scale, color, rigidBody)
        self.tim = 0
        self.timeCount = 2

    def Update(self):
        Cube.Update(self)
        if (self.tim >= self.timeCount):
            self.tim = 0
            x = random.uniform(-2, 2)
            y = random.uniform(1, 2)
            z = random.uniform(-2, 2)
            Object3D.addForce(self, Force(0,y,0))
            Object3D.addForce(self, Force(x,0,0,2))
        self.tim += self.deltaTime    

        if (self.Position.x <= -1000):
            self.removeAll()
            self.Position = Vector(0,0,0)
        if (self.Position.y <= -1000):
            self.t = 0
            self.removeAll()
            self.Position = Vector(0,0,0)
        if (self.Position.x >= 1000):
            self.removeAll()
            self.Position = Vector(0,0,0)
        if (self.Position.y >= 1000):
            self.removeAll()
            self.Position = Vector(0,0,0)

    def Draw(self, screen):
        Cube.Draw(self, screen)
        
    def removeAll(self):
        Object3D.removeAllForces(self)
