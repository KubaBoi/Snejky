"""
trida trojuhelniku slozenych ze 3 vertexu
"""

import math

from Engine.vertex import Vertex
from Engine.vector import Vector
from Engine.camera import Camera

class Face:
    def __init__(self, vectors, color=(255, 0, 255), bothSides=False):
        self.v = vectors #vektory vedouci od stredu mesh k bodum
        self.V = [] #body definujici face

        while (len(self.v) < 2):
            self.v.append(Vector(0,0,0))
        
        self.color = color
        self.bothSides = bothSides

        self.rFase = 0
        self.tempColor = (0,0,0)

    #aktualizuje informace face
    def updateFace(self, mesh, camera, light):
        self.updateVertices(mesh)
        self.getCenter()
        #self.setMaxDistance(camera)
        self.setCenterDistance(camera)
        #self.setAverageDistance(camera)
        self.setColor(light, mesh)
        self.setRenderability(camera, mesh)

    #spocte polohu vertexu posunutim stredu domaci meshe o vektor
    def updateVertices(self, mesh):
        self.V = []
        for i in range(0, len(self.v)):
            vector = self.v[i].addVectorReturn(mesh.Position)

            self.V.append(Vertex(vector.x, vector.y, vector.z))

    def setAverageDistance(self, camera):
        s = 0
        for i in range(0, len(self.V)):
            s += self.V[i].Position.pointLen(camera.Position)

        self.distance = s/(len(self.V)-1)

    def setCenterDistance(self, camera):
        self.distance = self.center.pointLen(camera.Position)
        
    def setMaxDistance(self, camera):
        self.distance = self.V[0].Position.pointLen(camera.Position)
        if (self.distance < self.V[1].Position.pointLen(camera.Position)):
            self.distance = self.V[1].Position.pointLen(camera.Position)
        if (self.distance < self.V[2].Position.pointLen(camera.Position)):
            self.distance = self.V[2].Position.pointLen(camera.Position)

    def setRenderability(self, camera, mesh):
        n = self.getDirection(mesh)
        #vektor od bodu teziste ke kamere
        t = camera.Position.newVector(self.center)

        angle = n.angle(t)

        if ((angle <= math.pi/2 or self.bothSides)
            and self.isInFrontOfCamera(camera)):
            self.render = True
        else:
            self.render = False

    #vrati true, pokud je face pred kamerou
    #false pokud je za kamerou a nema se vykreslovat
    #pokud alespon jeden z vertexu je blize ke konci vektoru pohledu
    #tak se face vykresli
    def isInFrontOfCamera(self, camera):
        for vert in self.V:
            a = vert.Position.pointLen(camera.S)
            ac = vert.Position.pointLen(camera.Position)
            if (a <= ac): return True

        return False
        

    #spocte teziste trojuhelniku
    def getCenter(self):
        if (len(self.V) >= 3):
            S1 = Vector((self.V[0].Position.x + self.V[1].Position.x)/2,
                        (self.V[0].Position.y + self.V[1].Position.y)/2,
                        (self.V[0].Position.z + self.V[1].Position.z)/2)

            S2 = Vector((self.V[0].Position.x + self.V[2].Position.x)/2,
                        (self.V[0].Position.y + self.V[2].Position.y)/2,
                        (self.V[0].Position.z + self.V[2].Position.z)/2)

            v = S1.newVector(self.V[2].Position)
            u = S2.newVector(self.V[2].Position)

            #matlab
            try:
                t = ((S1.y*u.z - S1.z*u.y - S2.y*u.z + S2.z*u.y)
                     /(u.y*v.z - u.z*v.y))
            except:
                t = 0

            self.center = Vector(S1.x + t*v.x,
                                 S1.y + t*v.y,
                                 S2.z + t*v.z)


    #upravi barvu face podle uhlu svetla
    def setColor(self, light, mesh):
        if (self.color == "rainbow"):
            self.rainbow()
            self.actColor = self.tempColor
        else:
            self.actColor = self.color
            
        n = self.getDirection(mesh)

        angle = n.angle(light.Vector)

        brightness = 100

        if (angle == 0):
            #ve stinu
            n = n.norm()
            l = light.Vector.norm()
            if (n.x != l.x or n.y != l.y or n.z != l.z):
                change = brightness
            else:
                change = 0
        else:
            change = (angle/math.pi)*brightness
        if (self.color != None):
            R = int(self.actColor[0] - change)
            G = int(self.actColor[1] - change)
            B = int(self.actColor[2] - change)

            if R < 0: R = 0
            if R > 255: R = 255
            if G < 0: G = 0
            if G > 255: G = 255
            if B < 0: B = 0
            if B > 255: B = 255

            self.actColor = (R, G, B)

    def getDirection(self, mesh):
        if (len(self.V) >= 3):
            #smerove vektory roviny face
            v = self.V[1].Position.newVector(self.V[0].Position)
            u = self.V[2].Position.newVector(self.V[0].Position)

            #normalovy vektor k rovine face
            n = Vector(u.y*v.z - v.y*u.z,
                       u.z*v.x - v.z*u.x,
                       u.x*v.y - v.x*u.y)

            #vektor od bodu teziste do stredu meshe
            a = mesh.Position.newVector(self.center)

            if (n.angle(a) <= math.pi/2):
                n = n.reverseVector()

            return n
        else:
            return Vector(0,0,0)

    def rainbow(self):
        step = 3
        if (self.rFase == 0):
            self.tempColor = (255,0,0)
            self.rFase += 1
        elif (self.rFase == 1):
            self.tempColor = (255,self.tempColor[1]+step,0)
            if (self.tempColor[1] >= 255):
                self.tempColor = (255,255,0)
                self.rFase += 1
                
        elif (self.rFase == 2):
            self.tempColor = (self.tempColor[0]-step,255,0)
            if (self.tempColor[0] <= 0):
                self.tempColor = (0,255,0)
                self.rFase += 1
                
        elif (self.rFase == 3):
            self.tempColor = (0,255,self.tempColor[2]+step)
            if (self.tempColor[2] >= 255):
                self.tempColor = (0,255,255)
                self.rFase += 1
                
        elif (self.rFase == 4):
            self.tempColor = (0,self.tempColor[1]-step,255)
            if (self.tempColor[1] <= 0):
                self.tempColor = (0,0,255)
                self.rFase += 1
                
        elif (self.rFase == 5):
            self.tempColor = (self.tempColor[0]+step,0,255)
            if (self.tempColor[0] >= 255):
                self.tempColor = (255,0,255)
                self.rFase += 1
                
        elif (self.rFase == 6):
            self.tempColor = (255,0,self.tempColor[2]-step)
            if (self.tempColor[2] <= 0):
                self.tempColor = (255,0,0)
                self.rFase += 1
                
        elif (self.rFase == 7):
            self.rFase = 0
        
