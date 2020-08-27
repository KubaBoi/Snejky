import pygame
from pygame.locals import*
import time

from Engine.gameScreen import GameScreen
from Engine.screen import Screen
from Engine.component import Component
from Engine.object3D import Object3D
from Engine.mesh import Mesh

class Engine:
    def __init__(self, screen, camera, light):
        self.screen = screen
        self.gameScreen = GameScreen(self)
        self.camera = camera
        self.light = light
        self.oldTime = time.time()

    def Update(self):
        self.camera.Update()
        self.light.Update()
        self.gameScreen.Update()

        self.oldTime = time.time()

    def Draw(self):        
        self.gameScreen.Draw(self.screen)

    def addComponent(self, Component):
        self.gameScreen.addComponent(Component)

    def removeComponent(self, Component):
        self.gameScreen.removeComponent(Component)

    def CollideRadius(self, mesh, radius, position):
        comps = []
        for Component2 in self.gameScreen.RigidBodies:
            if (Component2.mesh != mesh):
                radius2 = Component2.mesh.radius
                distance = position.pointLen(Component2.mesh.Position)
                if (radius2 + radius >= distance):
                    comps.append(Component2)
        if (len(comps) > 0):
            return True, comps
        return False, None

    def CollideHitBox(self, mesh):
        for Component2 in self.gameScreen.RigidBodies:
            if (Component2.mesh != mesh):
                if (True):
                    pass
