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

class Mesh:
    def __init__(self, engine, x, y, z, faces):
        self.Position = Vector(x, y, z)
        self.Faces = faces
        self.mode = "faces"

        self.engine = engine

        self.showHitbox = True
        self.hitBox = []
        self.updateFaces()

    def updateMesh(self, camera):
        self.distance = self.Position.pointLen(camera.Position)
        self.updateFaces()

    def updateFaces(self):
        for face in self.Faces:
            face.updateFace(self, self.engine.camera, self.engine.light)
        self.updateHitbox()

    #vykresli vsechny steny, pokud jejich vzdalenost od kamery je mensi
    #nez vzdalenost domaci Mesh od kamery
    #face.distance <= (face.distance - self.distance) + self.distance
    def drawFaces(self, screen, camera):     
        for face in self.Faces:
            if (face.render and self.mode == "faces"):
                A = face.A.drawVertex(camera)
                B = face.B.drawVertex(camera)
                C = face.C.drawVertex(camera)
                self.drawFace(screen, face, A, B, C)

            if (self.mode == "mesh"): #vykresli oboji
                A = face.A.drawVertex(camera)
                B = face.B.drawVertex(camera)
                C = face.C.drawVertex(camera)
                self.drawFace(screen, face, A, B, C)
                #screen.draw([A,B,C], face.distance, (0,0,0), False)


    def drawFace(self, screen, face, A, B, C):
        if (face.actColor != None):
            screen.draw([A,B,C], face.distance+self.distance, face.actColor, True)
            #screen.draw([A,B,C], face.distance, face.actColor, False)

    def sortFaces(self):
        for i in range(0, len(self.Faces) - 1):
            j = i + 1
            tmp = self.Faces[j]
            while(j > 0 and tmp.distance > self.Faces[j-1].distance):
                self.Faces[j] = self.Faces[j-1]
                j -= 1
            self.Faces[j] = tmp

    def checkCollisions(self, parent, v):
        self.hitBox[0] = self.hitBox[0] + v.x
        self.hitBox[3] = self.hitBox[3] + v.x
        self.hitBox[1] = self.hitBox[1] + v.y
        self.hitBox[4] = self.hitBox[4] + v.y
        self.hitBox[2] = self.hitBox[2] + v.z
        self.hitBox[5] = self.hitBox[5] + v.z
        

        answer = self.engine.CollideHitBox(self)
        if (answer[0] and answer[1].solid):
            answer[1].addForce(Force(v.x,
                                     v.y,
                                     v.z))
            newForce = self.createBounce(v, answer[1], 0.1)
            self.updateHitbox()
            i = 0
            while(self.engine.CollideHitBox(self)[0] == False):
                i += 0.1
                v = v.setVectorLeng(i)
                self.hitBox[0] = self.hitBox[0] + v.x
                self.hitBox[3] = self.hitBox[3] + v.x
                self.hitBox[1] = self.hitBox[1] + v.y
                self.hitBox[4] = self.hitBox[4] + v.y
                self.hitBox[2] = self.hitBox[2] + v.z
                self.hitBox[5] = self.hitBox[5] + v.z

            v = v.setVectorLeng(i-0.1)
            
            return True, v, newForce
        if (answer[0]): #koliduje, ale nema zastavit objekt
            pass
        else:
            parent.Position = self.Position
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
    

    def drawHitbox(self, screen):
        if (self.showHitbox):
            for edge in self.hitBoxEdges:
                edge.drawEdge(screen)
        
            
        
    def updateHitbox(self):
        try:
            maxmin = [self.Position.x,
                      self.Position.y,
                      self.Position.z,
                      self.Position.x,
                      self.Position.y,
                      self.Position.z] #maxX,maxY,maxZ,minX,minY,minZ
            for face in self.Faces:
                for vertex in [face.A, face.B, face.C]:
                    if (vertex.Position.x > maxmin[0]): #nejvetsi X
                        maxmin[0] = vertex.Position.x
                    if (vertex.Position.x < maxmin[3]): #nejmensi X
                        maxmin[3] = vertex.Position.x

                    if (vertex.Position.y > maxmin[1]): #nejvetsi Y
                        maxmin[1] = vertex.Position.y
                    if (vertex.Position.y < maxmin[4]): #nejmensi Y
                        maxmin[4] = vertex.Position.y

                    if (vertex.Position.z > maxmin[2]): #nejvetsi Z
                        maxmin[2] = vertex.Position.z
                    if (vertex.Position.z < maxmin[5]): #nejmensi Z
                        maxmin[5] = vertex.Position.z

            self.hitBox = maxmin
               
            self.hitBoxEdges = []
            self.hitBoxEdges.append(Edge(self.engine,
                               Vertex(maxmin[0],maxmin[1],maxmin[2]),
                               Vertex(maxmin[3],maxmin[1],maxmin[2])))

            self.hitBoxEdges.append(Edge(self.engine,
                               Vertex(maxmin[0],maxmin[1],maxmin[2]),
                               Vertex(maxmin[0],maxmin[1],maxmin[5])))

            self.hitBoxEdges.append(Edge(self.engine,
                               Vertex(maxmin[3],maxmin[1],maxmin[5]),
                               Vertex(maxmin[0],maxmin[1],maxmin[5])))

            self.hitBoxEdges.append(Edge(self.engine,
                               Vertex(maxmin[3],maxmin[1],maxmin[2]),
                               Vertex(maxmin[3],maxmin[1],maxmin[5])))
            #down
            self.hitBoxEdges.append(Edge(self.engine,
                               Vertex(maxmin[0],maxmin[4],maxmin[2]),
                               Vertex(maxmin[3],maxmin[4],maxmin[2])))

            self.hitBoxEdges.append(Edge(self.engine,
                               Vertex(maxmin[0],maxmin[4],maxmin[2]),
                               Vertex(maxmin[0],maxmin[4],maxmin[5])))

            self.hitBoxEdges.append(Edge(self.engine,
                               Vertex(maxmin[3],maxmin[4],maxmin[5]),
                               Vertex(maxmin[0],maxmin[4],maxmin[5])))

            self.hitBoxEdges.append(Edge(self.engine,
                               Vertex(maxmin[3],maxmin[4],maxmin[2]),
                               Vertex(maxmin[3],maxmin[4],maxmin[5])))
            #between
            self.hitBoxEdges.append(Edge(self.engine,
                               Vertex(maxmin[0],maxmin[4],maxmin[2]),
                               Vertex(maxmin[0],maxmin[1],maxmin[2])))

            self.hitBoxEdges.append(Edge(self.engine,
                               Vertex(maxmin[0],maxmin[4],maxmin[5]),
                               Vertex(maxmin[0],maxmin[1],maxmin[5])))

            self.hitBoxEdges.append(Edge(self.engine,
                               Vertex(maxmin[3],maxmin[4],maxmin[2]),
                               Vertex(maxmin[3],maxmin[1],maxmin[2])))

            self.hitBoxEdges.append(Edge(self.engine,
                               Vertex(maxmin[3],maxmin[4],maxmin[5]),
                               Vertex(maxmin[3],maxmin[1],maxmin[5])))

            return maxmin
        except:
            return None


    def changeColor(self, color):
        for face in self.Faces:
            face.color = color

    #metoda, ktera prenacte steny
    def setFaces(self, faces):
        self.Faces = faces
