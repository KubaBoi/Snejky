"""
uchovava seznam vertexu meshe
spocita prunik vertexu s druhym objektem a vrati idelani pozici meshe

"""

from Engine.vertex import Vertex
from Engine.vector import Vector
from Engine.force import Force

import math
import time

class MeshCollider:
    def __init__(self, parent):
        self.parent = parent #mesh, ktere nalezi        

    #nalezne vsechny vertexy meshe
    def updateVertices(self):
        self.Vertices = []
        for face in self.parent.Faces:
            for vert in face.V:
                isDone = False
                for vertex in self.Vertices:
                    if (vertex.vertex.Position.equals(vert.Position)):
                        isDone = True
                        vertex.addFace(face)
                if (isDone == False):
                    self.Vertices.append(CollisionVertex(vert, self.parent.parent))

    #je volana pokud kolizni koule objektu koliduji
    #v - vektor pohybu
    def collision(self, comp, v):
        self.updateVertices()
        self.foundCollidableVertices(comp)

        self.distance = v.length()
        self.collisionVector = None
        for vertex in self.collidableVertices:
            for c in comp:
                self.getCollisionVector(vertex,
                                        vertex.vertex.Position.addVectorReturn(v),
                                        c.mesh, v)

        for vertex in self.collidableVerticesOther:
            self.getCollisionVector(vertex,
                                    vertex.vertex.Position.addVectorReturn(v),
                                    self.parent, v)
            
        if (self.collisionVector == None):
            return v, None, False
        
        return (self.collisionVector.vertex, self.collisionVector.object,
                True)

    #nalezne vertexy, ktere jsou v kolizni kouli druheho objektu
    #pouziva CollisionVertex
    def foundCollidableVertices(self, comp):
        self.collidableVertices = []
        for vert in self.Vertices:
            for c in comp:
                if (vert.vertex.Position.pointLen(c.Position) <= c.mesh.radius):
                    self.collidableVertices.append(vert)

        self.collidableVerticesOther = [] #seznam koliznich vertexu druheho objektu
        for c in comp:
            c.mesh.collider.updateVertices()
            for vert in c.mesh.collider.Vertices:
                if (vert.vertex.Position.pointLen(self.parent.Position) <= self.parent.radius):
                    self.collidableVerticesOther.append(vert)

    #nalezne bod, ktery protina face nejblize k vertexu
    #vertex - stary bod
    #newVertex - novy bod
    def getCollisionVector(self, vertex, newVertex, mesh, v):
        fc = None
        for face in mesh.Faces:
            G = self.findG(vertex.vertex, newVertex, face)
            if (G != None): #bod pruniku protina trojuhelnik
                d = G.pointLen(vertex.vertex.Position)
                if (d < self.distance): #je nejblize
                    self.distance = d
                    fc = face
                    
        if (fc != None):
            G = self.findG(vertex.vertex, newVertex, fc)
            self.collisionVector = CollisionVertex(G.newVector(vertex.vertex.Position),
                                                               vertex.object)
                        
            if (self.collisionVector.vertex.length() == 0):
                if (self.parent.Position.pointLen(mesh.Position) <
                    self.parent.Position.addVectorReturn(v).pointLen(mesh.Position)):
                    self.collisionVector = CollisionVertex(v, vertex.object)
                else:
                    pass #self.collisionVector.vertex.speak("coll: ")


    #vrati bod, ve kterem se protina primka s face rovinou
    #vertex - bod pred posunem (kamera)
    #newVertex - bod po posunu (sledovany vertex)
    def findG(self, vertex, newVertex, face):
        c1 = newVertex.x
        c2 = newVertex.y
        c3 = newVertex.z

        u = face.V[0].Position.newVector(face.V[1].Position)
        u1 = u.x
        u2 = u.y
        u3 = u.z

        r = face.V[2].Position.newVector(face.V[1].Position)
        r1 = r.x
        r2 = r.y
        r3 = r.z
        
        s1 = face.V[0].Position.x
        s2 = face.V[0].Position.y
        s3 = face.V[0].Position.z

        g1 = vertex.Position.x - c1
        g2 = vertex.Position.y - c2
        g3 = vertex.Position.z - c3

        #miluju matlab
        try:
            t = (-(c1*r2*u3 - c1*r3*u2 - c2*r1*u3 + c2*r3*u1 + c3*r1*u2 - c3*r2*u1
                   + r1*s2*u3 - r1*s3*u2 - r2*s1*u3 + r2*s3*u1 + r3*s1*u2 - r3*s2*u1)/
                 (g1*r2*u3 - g1*r3*u2 - g2*r1*u3 + g2*r3*u1 + g3*r1*u2 - g3*r2*u1))
        except:
            t = 0

        G = Vector(c1 + t*g1,c2 + t*g2,c3 + t*g3)
        #delky trojuhelniku
        a = face.V[0].Position.pointLen(face.V[1].Position)
        b = face.V[0].Position.pointLen(face.V[2].Position)
        c = face.V[1].Position.pointLen(face.V[2].Position)

        #bod nalezi trojuhelniku
        if (G.pointLen(face.V[0].Position) <= a and
            G.pointLen(face.V[0].Position) <= b and
            G.pointLen(face.V[0].Position) <= c and
            G.pointLen(face.V[1].Position) <= a and
            G.pointLen(face.V[1].Position) <= b and
            G.pointLen(face.V[1].Position) <= c and
            G.pointLen(face.V[2].Position) <= a and
            G.pointLen(face.V[2].Position) <= b and
            G.pointLen(face.V[2].Position) <= c):
            return G
        

        return None

class CollisionVertex:
    def __init__(self, vertex, obj):
        self.vertex = vertex
        self.faces = []
        self.object = obj

    def addFace(self, face):
        self.faces.append(face)
