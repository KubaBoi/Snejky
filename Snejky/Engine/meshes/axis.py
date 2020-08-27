import pygame
from Engine.vector import Vector
from Engine.camera import Camera
from Engine.vertex import Vertex
from Engine.mesh import Mesh
from Engine.face import Face
from Engine.component import Component
from Engine.screen import Screen
from Engine.meshes.edge import Edge

class Axis(Component):
    def __init__(self, engine, scale):
        self.scale = scale
        
        Component.__init__(self, engine)

    def drawLines(self, screen):
        nul = Vertex(0,0,0)
        
        x1 = Vertex(self.scale, 0, 0)
        x2 = Vertex(-self.scale, 0, 0)
        y1 = Vertex(0,self.scale,0)
        y2 = Vertex(0,-self.scale,0)
        z1 = Vertex(0,0,self.scale)
        z2 = Vertex(0,0,-self.scale)

        edge1 = Edge(self.engine, x1, x2).drawEdge(screen)
        edge2 = Edge(self.engine, y1, y2).drawEdge(screen)
        edge3 = Edge(self.engine, z1, z2).drawEdge(screen)
        
        """if (self.isInFrontOfCamera(self.engine.camera, x1, nul)):
            pygame.draw.lines(screen, (255,0,0), False, [x1.drawVertex(self.engine.camera),
                                                         nul.drawVertex(self.engine.camera)], 1)
        if (self.isInFrontOfCamera(self.engine.camera, nul, x2)):
            pygame.draw.lines(screen, (255,0,0), False, [nul.drawVertex(self.engine.camera),
                                                         x2.drawVertex(self.engine.camera)], 1)

        y1 = Vertex(0, self.scale, 0)
        y2 = Vertex(0, -self.scale, 0)
        if (self.isInFrontOfCamera(self.engine.camera, y1, nul)):
            pygame.draw.lines(screen, (0,255,0), False, [y1.drawVertex(self.engine.camera),
                                                         nul.drawVertex(self.engine.camera)], 1)
        if (self.isInFrontOfCamera(self.engine.camera, nul, y2)):
            pygame.draw.lines(screen, (0,255,0), False, [nul.drawVertex(self.engine.camera),
                                                         y2.drawVertex(self.engine.camera)], 1)

        z1 = Vertex(0, 0, self.scale)
        z2 = Vertex(0, 0, -self.scale)
        if (self.isInFrontOfCamera(self.engine.camera, z1, nul)):
            pygame.draw.lines(screen, (0,0,255), False, [z1.drawVertex(self.engine.camera),
                                                         nul.drawVertex(self.engine.camera)], 1)

        if (self.isInFrontOfCamera(self.engine.camera, nul, z2)):
            pygame.draw.lines(screen, (0,0,255), False, [nul.drawVertex(self.engine.camera),
                                                         z2.drawVertex(self.engine.camera)], 1)"""

    def isInFrontOfCamera(self, camera, c1, c2):
        a = c1.Position.pointLen(camera.S)
        ac = c1.Position.pointLen(camera.Position)
        if (a <= ac): return True

        b = c2.Position.pointLen(camera.S)
        bc = c2.Position.pointLen(camera.Position)
        if (b <= bc): return True

        return False
 
    def Update(self):
        pass
    def Draw(self, screen):
        self.drawLines(screen)
