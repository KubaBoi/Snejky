"""
trida uchovava seznam faces, ten přetřídí podle vzdálenosti od kamery
a vykreslí
trida take aktualizuje informace o svych faces
pokud je bod Meshe ke kameře blíže než Center face, tak se face nevykreslí
pokud je self.mode = "faces" - vykresluji se steny
pokud je self.mode = "edges" - vykresluji se pouze hrany (kostra)

uchovava si celkovy hitbox - hranata oblast,
    ve ktere se nachazeji vsechny vertexy
"""

from Engine.vertex import Vertex
from Engine.vector import Vector
from Engine.meshes.edge import Edge
from Engine.screen import Screen
from Engine.force import Force
from Engine.meshCollider import MeshCollider

import math
import time

class Mesh:
    def __init__(self, engine, parent, x, y, z, faces):
        self.Position = Vector(x, y, z)
        self.Faces = faces
        self.mode = "faces"

        self.parent = parent
        
        self.engine = engine

        self.showHitbox = True
        self.updateFaces()
        self.updateRadius()

        self.collider = MeshCollider(self)

    def updateMesh(self, camera):
        self.distance = self.Position.pointLen(camera.Position)
        self.updateFaces()

    def updateFaces(self):
        for face in self.Faces:
            face.updateFace(self, self.engine.camera, self.engine.light)

    #vykresli vsechny steny, pokud jejich vzdalenost od kamery je mensi
    #nez vzdalenost domaci Mesh od kamery
    #face.distance <= (face.distance - self.distance) + self.distance
    def drawFaces(self, screen, camera):     
        for face in self.Faces:
            if (face.render and self.mode == "faces"):
                vertices = []
                for vert in face.V:
                    vertices.append(vert.drawVertex(camera))
                self.drawFace(screen, face, vertices)

            if (self.mode == "mesh"): #vykresli oboji
                A = face.A.drawVertex(camera)
                B = face.B.drawVertex(camera)
                C = face.C.drawVertex(camera)
                self.drawFace(screen, face, A, B, C)
                #screen.draw([A,B,C], face.distance, (0,0,0), False)
        #self.drawRadius(screen)


    def drawFace(self, screen, face, vertices):
        if (face.actColor != None):
            screen.draw(vertices, face.distance, face.actColor, True)
            #screen.draw(vertices, face.distance, face.actColor, False)

    def checkCollisions(self, parent, v):
        answer = self.engine.CollideRadius(self, self.radius,
                                           self.Position.addVectorReturn(v))
        
        if (answer[0]):            
            v, obj, collide = self.collider.collision(answer[1], v)

            if (collide):
                #v = Vector(v.Position.x, v.Position.y, v.Position.z)
                obj.addForce(Force(v.x/2,
                               v.y/2,
                               v.z/2))
                newForce = self.createBounce(v, obj, 0.5)
            else:
                newForce = Force(0,0,0)
            
            return collide, v, newForce

        if (answer[0]): #koliduje, ale nema zastavit objekt
            pass
        else:
            return False, v

    def createBounce(self, v, component, slow):
        deltaX = abs(component.Position.x - self.Position.x)
        deltaY = abs(component.Position.y - self.Position.y)
        deltaZ = abs(component.Position.z - self.Position.z)

        if (deltaX >= deltaY and deltaX >= deltaZ):
            return Force(v.x*-slow, v.y*slow, v.z*slow, slow)
        if (deltaY >= deltaX and deltaY >= deltaZ):
            return Force(v.x*slow, v.y*-slow, v.z*slow, slow)
        if (deltaZ >= deltaX and deltaZ >= deltaY):
            return Force(v.x*slow, v.y*slow, v.z*-slow, slow)
            
    #najde nejvzdalensejsi bod meshe a spocte jeho vzdalenost od stredu
    #najde polomer hitBoxu
    def updateRadius(self):
        self.radius = 0
        for face in self.Faces:
            for vector in face.v:
                newRadius = vector.length()
                if (newRadius > self.radius):
                    self.radius = newRadius
        

    def changeColor(self, color):
        for face in self.Faces:
            face.color = color

    #metoda, ktera prenacte steny
    def setFaces(self, faces):
        self.Faces = faces

    def drawRadius(self, screen):
        step = 40
        for i in range(0, 360, step):
            radian = i*math.pi/180
            
            x1 = self.Position.x + self.radius*math.sin(radian)
            y1 = self.Position.y + self.radius*math.cos(radian)

            radian = (i+step)*math.pi/180
            x2 = self.Position.x + self.radius*math.sin(radian)
            y2 = self.Position.y + self.radius*math.cos(radian)

            a1 = Vertex(x1,y1,self.Position.z)
            a2 = Vertex(x2,y2,self.Position.z)
            
            edge = Edge(self.engine, a1, a2).drawEdge(screen)
            
        for i in range(0, 360, step):
            radian = i*math.pi/180
            
            z1 = self.Position.z + self.radius*math.sin(radian)
            y1 = self.Position.y + self.radius*math.cos(radian)

            radian = (i+step)*math.pi/180
            z2 = self.Position.z + self.radius*math.sin(radian)
            y2 = self.Position.y + self.radius*math.cos(radian)

            a1 = Vertex(self.Position.x,y1,z1)
            a2 = Vertex(self.Position.x,y2,z2)
            
            edge = Edge(self.engine, a1, a2).drawEdge(screen)
            
        for i in range(0, 360, step):
            radian = i*math.pi/180
            
            x1 = self.Position.x + self.radius*math.sin(radian)
            z1 = self.Position.z + self.radius*math.cos(radian)

            radian = (i+step)*math.pi/180
            x2 = self.Position.x + self.radius*math.sin(radian)
            z2 = self.Position.z + self.radius*math.cos(radian)

            a1 = Vertex(x1,self.Position.y,z1)
            a2 = Vertex(x2,self.Position.y,z2)
            
            edge = Edge(self.engine, a1, a2).drawEdge(screen)
