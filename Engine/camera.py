import pygame
from pygame.locals import*
import math

from Engine.object3D import Object3D
from Engine.vertex import Vertex
from Engine.vector import Vector

class Camera(Object3D):
    def __init__(self, engine, x, y, z, w, h):
        Object3D.__init__(self, engine, x, y, z)
        self.x = w #poloha na obrazovce
        self.y = h #poloha na obrazovce
        
        self.speed = 0.1
        self.viewAngle = math.pi
        self.maxView = 1000
        self.far = 1
        self.f = Vector(0, 0, self.far)
        self.u = Vector(0, self.far, 0)
        self.r = Vector(self.far, 0, 0)
        self.S = self.Position #predek

        self.rotX = 0
        self.rotY = 0
        
    def Update(self):
        self.Input()
        self.S = Vector(self.Position.x + self.f.x,
                        self.Position.y + self.f.y,
                        self.Position.z + self.f.z,)
        self.B = Vector(self.Position.x - self.f.x,
                        self.Position.y - self.f.y,
                        self.Position.z - self.f.z,)
        #self.Position.speak("kamera: ")
            


    def Input(self):
        self.Rotate(pygame.mouse.get_pressed())
        self.Keys(pygame.key.get_pressed())
        self.setView(pygame.key.get_pressed())
            
    def Keys(self, keys):
        if (keys[K_w]):
            self.Position.addVector(self.f.multipleVector(self.speed))
        elif (keys[K_s]):
            self.Position.addVector(
                self.f.multipleVector(self.speed).reverseVector())
        if (keys[K_d]):
            self.Position.addVector(self.r.multipleVector(self.speed))
        elif (keys[K_a]):
            self.Position.addVector(
                self.r.multipleVector(self.speed).reverseVector())
        if (keys[K_SPACE]):
            self.Position.addVector(self.u.multipleVector(self.speed))
        elif (keys[K_LSHIFT]):
            self.Position.addVector(
                self.u.multipleVector(self.speed).reverseVector())

        if (keys[K_q]): #snizeni rychlosti
            if (self.speed - 0.1 > 0):
                self.speed -= 0.1
                print("speed: " + str(self.speed))
        elif (keys[K_e]): #zvyseni rychlosti
            self.speed += 0.1
            print("speed: " + str(self.speed))
        elif (keys[K_r]): #reset rychlosti
            self.speed = 0.1
            print("speed: " + str(self.speed))

        if (keys[K_g]): #reset kamery
            self.Position = Vector(0,0,0)
            self.f = Vector(0, 0, self.far)
            self.u = Vector(0, self.far, 0)
            self.r = Vector(self.far, 0, 0)

            self.rotX = 0
            self.rotY = 0

            
    def Rotate(self, event):
        if (len(event) == 0):
            pygame.mouse.set_visible(True)

        xy = pygame.mouse.get_rel()
        x = 0
        y = 0
        if (event[0]): #leve tlacitko
            self.x = self.x
        elif (event[2]): #prave tlacitko
            #pygame.mouse.set_visible(False)
            x = xy[0]/2
            y = xy[1]/2
                
            

        self.rotX += x*(math.pi/180)/2
        self.rotY -= y*(math.pi/180)/2

        x = math.sin(self.rotX)
        y = math.sin(self.rotY)
        z = math.cos(self.rotX)
        self.f = Vector(x, y, z)
        
        x = math.sin(self.rotX + math.pi/2)
        z = math.cos(self.rotX + math.pi/2)
        self.r = Vector(x, 0, z)

        self.u = Vector(self.f.y*self.r.z - self.r.y*self.f.z,
                        self.f.z*self.r.x - self.r.z*self.f.x,
                        self.f.x*self.r.y - self.r.x*self.f.y)

    def setView(self, keys):
        if (keys[K_2] or keys[K_KP2]):#zepredu
            self.Position = Vector(6, 5, -17)
            self.rotX = 0
            self.rotY = 0
        if (keys[K_6] or keys[K_KP6]):#zprava
            self.Position = Vector(29, 5, 6)
            self.rotX = 3*math.pi/2
            self.rotY = 0
        if (keys[K_8] or keys[K_KP8]):#zezadu
            self.Position = Vector(6, 5, 29)
            self.rotX = math.pi
            self.rotY = 0
        if (keys[K_4] or keys[K_KP4]):#zleva
            self.Position = Vector(-17, 5, 6)
            self.rotX = math.pi/2
            self.rotY = 0

        

            
        


