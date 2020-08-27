import pygame
from pygame.locals import*
import math
import time

from Engine.component import Component
from Engine.vertex import Vertex
from Engine.vector import Vector
from Engine.force import Force

from Engine.meshes.edge import Edge

class Object3D(Component):
    def __init__(self, engine, x, y, z, mesh=None, rigidBody=False):
        Component.__init__(self, engine, mesh, rigidBody)
        self.Position = Vector(x, y, z)
        
        self.rigidBody = rigidBody
        self.v = Vector(0, 0, 0) #pohybovy vektor telesa
        self.t = 0
        self.deltaTime = 0
        self.forces = []
        self.solid = True

        self.screen = None

    def Update(self):
        keys = pygame.key.get_pressed()
        if (keys[K_l]):
            self.addForce(Force(0.1,0.1,0))
        if (keys[K_j]):
            self.addForce(Force(-0.1,0.1,0))
        if (keys[K_k]):
            self.addForce(Force(0,1,0))
            self.t = 0

        
        self.physics()

        #self.mesh.Position.speak("mesh: ")
        #self.Position.speak("object: ")
        
        self.mesh.Position = self.Position
        #self.v.speak("smerovy vektor: ")
        
    def Draw(self, screen):
        end = self.Position.addVectorReturn(self.v)
        edge = Edge(self.engine, Vertex(self.Position.x,
                                        self.Position.y,
                                        self.Position.z),
                    Vertex(end.x, end.y, end.z))
        #edge.drawEdge(screen)

    def physics(self):
        if (self.rigidBody):
            self.deltaTime = time.time() - self.engine.oldTime
            
            self.v = Vector(0,0,0)
            self.applyForces()

            self.checkCollisions()
            
            self.gravity()
            
            self.Position.addVector(self.v)
            #print(len(self.forces))
            #self.v.speak("smer: ")
            
    def gravity(self):
        self.t += self.deltaTime
        #self.v.y -= 0.981*self.t
        #self.v.y -= self.t
        answer = self.mesh.checkCollisions(self, Vector(0,-self.t,0))
        if (not answer[0] and self.v.y <= 0):
            self.v.y -= self.t
        else:
            self.t = 0

    def applyForces(self):
        for force in self.forces:
            add = force.update(self.deltaTime)
            if (add.length() > 0):
                self.v.addVector(add)
            else:
                self.removeForce(force)
            
    def addForce(self, force):
        self.forces.append(force)

    def removeForce(self, force):
        self.forces.remove(force)

    def removeAllForces(self):
        while (len(self.forces) > 0):
            self.removeForce(self.forces[0])
        self.t = 0

    def checkCollisions(self):
        if (self.mesh != None):
            answer = self.mesh.checkCollisions(self, self.v)
            self.v = answer[1]
            if (self.Position.y <= -100):
                self.t = 0
                self.Position.y = -10
            if (answer[0]):
                self.removeAllForces()
                self.addForce(answer[2])
        
