import math
import pygame
from pygame.locals import*

from Snejky.vector import Vector

class Camera:
    def __init__(self, position: tuple, w: int, h: int):
        self.position = position
        self.x = w #poloha na obrazovce
        self.y = h #poloha na obrazovce
        
        self.speed = 0.1
        self.viewAngle = math.pi
        self.maxView = 1000
        self.far = 1
        self.f = (0, self.far, 0)
        self.u = (0, 0, self.far)
        self.r = (self.far, 0, 0)
        self.S = self.position #predek

        self.rotX = 0
        self.rotY = 0
        
    def update(self):
        self.input()
        self.S = Vector.add(self.position, self.f)
        self.B = Vector.sub(self.position, self.f)
        #self.position.speak("kamera: ")

    def input(self):
        self.rotate(pygame.mouse.get_pressed())
        self.keys(pygame.key.get_pressed())
        self.set_view(pygame.key.get_pressed())
            
    def keys(self, keys):
        if (keys[K_w]):
            self.position = Vector.add(self.position, Vector.scale(self.f, self.speed))
        elif (keys[K_s]):
            self.position = Vector.add(self.position, 
                Vector.reverse(Vector.scale(self.f, self.speed)))
        if (keys[K_d]):
            self.position = Vector.add(self.position, Vector.scale(self.r, self.speed))
        elif (keys[K_a]):
            self.position = Vector.add(self.position, 
                Vector.reverse(Vector.scale(self.r, self.speed)))
        if (keys[K_SPACE]):
            self.position = Vector.add(self.position, Vector.scale(self.u, self.speed))
        elif (keys[K_LSHIFT]):
            self.position = Vector.add(self.position, 
                Vector.reverse(Vector.scale(self.u, self.speed)))

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
            self.position = (0,0,0)
            self.f = (0, 0, self.far)
            self.u = (0, self.far, 0)
            self.r = (self.far, 0, 0)

            self.rotX = 0
            self.rotY = 0

            
    def rotate(self, event):
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
        self.f = (x, y, z)
        
        x = math.sin(self.rotX + math.pi/2)
        z = math.cos(self.rotX + math.pi/2)
        self.r = (x, 0, z)

        self.u = (self.f.y*self.r.z - self.r.y*self.f.z,
                        self.f.z*self.r.x - self.r.z*self.f.x,
                        self.f.x*self.r.y - self.r.x*self.f.y)

    def set_view(self, keys):
        if (keys[K_2] or keys[K_KP2]):#zepredu
            self.position = (6, 5, -17)
            self.rotX = 0
            self.rotY = 0
        if (keys[K_6] or keys[K_KP6]):#zprava
            self.position = (29, 5, 6)
            self.rotX = 3*math.pi/2
            self.rotY = 0
        if (keys[K_8] or keys[K_KP8]):#zezadu
            self.position = (6, 5, 29)
            self.rotX = math.pi
            self.rotY = 0
        if (keys[K_4] or keys[K_KP4]):#zleva
            self.position = (-17, 5, 6)
            self.rotX = math.pi/2
            self.rotY = 0