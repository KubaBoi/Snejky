import pygame

from Engine.vector import Vector
#from Engine.camera import Camera
from Engine.vertex import Vertex
#from Engine.face import Face
from Engine.screen import Screen
from Engine.component import Component

class Edge(Component):
    def __init__(self, engine, v1, v2):
        self.V1 = v1
        self.V2 = v2

        Component.__init__(self, engine) 

    def Update(self):
        pass
    def drawEdge(self, screen):
        v1 = self.V1
        v2 = self.V2
        #if (self.isInFrontOfCamera(self.engine.camera)):
        screen.draw([v1.drawVertex(self.engine.camera),
                    v2.drawVertex(self.engine.camera)],
                    0, (0,0,0), False)

    def isInFrontOfCamera(self, camera):
        a = self.V1.Position.pointLen(camera.S)
        ac = self.V1.Position.pointLen(camera.Position)
        if (a <= ac): return True

        b = self.V2.Position.pointLen(camera.S)
        bc = self.V2.Position.pointLen(camera.Position)
        if (b <= bc): return True

        return False
