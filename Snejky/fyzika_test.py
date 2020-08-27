"""
testovani fyziky
DuhovyBoxik kazdych nekolik vterin vygeneruje nahodnou silu, kterou
zapusobi sam na sebe
Boxiky maji kolem sebe 4 velike kostky, aby nevylitavaly pryc z obrazovky
"""


from traceback import format_exc
import pygame
from pygame import surfarray
from pygame.locals import*
import time
import random

from Engine.engine import Engine
from Engine.screen import Screen

from Engine.vector import Vector
from Engine.camera import Camera
from Engine.vertex import Vertex
from Engine.light import Light
from Engine.force import Force

from Engine.meshes.axis import Axis
from Engine.meshes.cube import Cube
from Engine.meshes.car import Car
from Engine.meshes.penguin import Penguin
from Engine.meshes.pyramid import Pyramid
from Engine.meshes.edge import Edge
from duhovejBoxik import DuhovyBoxik
from creature import Creature

pygame.init()

#full screen
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

width = 1280
height = 720
screen = pygame.display.set_mode((width, height))

white = (255, 255, 255)
screen.fill((white))
running = True

sc = Screen(width, height)

clock = pygame.time.Clock()

camera = Camera(None, 0, 0, -100, width/2, height/2)

engine = Engine(sc, camera, Light(1, 1, 1))
camera.engine = engine

engine.addComponent(Axis(engine, 1000))

#nastavenim hodnoty promenne col se zviditelni hranicni kostky
col = (145,20,200)
#engine.addComponent(Cube(engine, -50,0,0,30,col))
#engine.addComponent(Cube(engine, 50,0,0,30,col))
engine.addComponent(Cube(engine, 0,-50,0,30,col))
#engine.addComponent(Cube(engine, 0,50,0,30,col))

engine.addComponent(Pyramid(engine,0,20,0,1,1,"rainbow",True))
for i in range(0, 10):
    #cb = DuhovyBoxik(engine,i*3-10,20,0,1,"rainbow", True)
    cb = Creature(engine,0,i*6+40,0,(255,0,255))
    engine.addComponent(cb)
    for face in cb.mesh.Faces:
        face.rFaze = random.randrange(0, 8)
    #engine.addComponent(Car(engine,10,i*10+20,0,"rainbow",True))

fps = 0
ticks = 0
while running:
    tm = time.time()
    try:
        engine.Update()
        engine.Draw()
    except Exception as e:
        print(repr(e))
        print(format_exc())
        running = False
    #print(sc.objHeap.count)
    sc.createScreen(screen)
       
    #surfarray.blit_array(screen, sc.drawScreen())
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    ticks += 1
    fps += time.time()-tm
    #print(c)

    if (fps >= 1):
        fps = 0
        print("fps: " + str(ticks))
        ticks = 0

    #clock.tick(60)

pygame.quit()
