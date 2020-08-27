import pygame
from pygame.locals import*

from Engine.component import Component
from Engine.face import Face
from Engine.vertex import Vertex
from Engine.vector import Vector

class GameScreen:
    def __init__(self, engine):
        self.engine = engine
        self.Components = []
        self.RigidBodies = []

    def Update(self):
        for comp in self.Components:
            comp.Update()
            if (comp.mesh != None):
                comp.mesh.updateMesh(self.engine.camera)

    def Draw(self, screen):
        for comp in self.Components:
            comp.Draw(screen)
            if (comp.mesh != None):
                comp.mesh.drawFaces(screen, self.engine.camera)

    def addComponent(self, Component):
        self.Components.append(Component)
        if (Component.mesh != None):
            self.addRigidBody(Component)

    def removeComponent(self, Component):
        if (Component in self.Components):
            self.Components.remove(Component)
            if (Component.mesh != None):
                self.removeRigidBody(Component)

    def addRigidBody(self, Component):
        self.RigidBodies.append(Component)

    def removeRigidBody(self, Component):
        self.RigidBodies.remove(Component)
        



