from Engine.vector import Vector
from Engine.camera import Camera
from Engine.vertex import Vertex
from Engine.mesh import Mesh
from Engine.face import Face
from Engine.object3D import Object3D
from Engine.meshes.cube import Cube
from Engine.force import Force

import random

class Creature(Cube):
    def __init__(self, engine, x, y, z, color=(255,0,0)):
        Cube.__init__(self, engine, x, y, z, 1, color, True)
        self.day = 0
        self.tick = 0
        self.maxTick = 2

    def Update(self):
        Cube.Update(self)
        #if (self.day >= 120): #cely den

        if (self.tick >= self.maxTick):
            self.mesh.changeColor((0,255,0))
            

        self.tick += self.deltaTime   
        self.checkPosition()

    def Draw(self, screen):
        Cube.Draw(self, screen)

    def checkPosition(self):
        if (self.Position.x <= -1000):
            self.removeAll()
            self.Position = Vector(0,20,0)
        if (self.Position.y <= -1000):
            self.t = 0
            self.removeAll()
            self.Position = Vector(0,20,0)
        if (self.Position.x >= 1000):
            self.removeAll()
            self.Position = Vector(0,20,0)
        if (self.Position.y >= 1000):
            self.removeAll()
            self.Position = Vector(0,20,0)

    def removeAll(self):
        Object3D.removeAllForces(self)
