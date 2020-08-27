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
screen.fill(white)
running = True

sc = Screen(width, height, (179, 229, 252))

clock = pygame.time.Clock()

camera = Camera(None, 0, 0, -400, width/2, height/2)

engine = Engine(sc, camera, Light(1, 1, 1))
camera.engine = engine

#engine.addComponent(Axis(engine, 1000))
#cube = Cube(engine, 0, 0, 0, 1, "rainbow", False)
"""engine.addComponent(DuhovyBoxik(engine, 0,0,0,1,"rainbow", True))
engine.addComponent(DuhovyBoxik(engine, 10,0,0,1,"rainbow", True))
engine.addComponent(DuhovyBoxik(engine, -20,10,0,1,"rainbow", True))"""

col = None #(145,20,200)
engine.addComponent(Cube(engine,-600,0,0,300,col))
engine.addComponent(Cube(engine,600,0,0,300,col))
engine.addComponent(Cube(engine,0,-400,0,300,(104, 159, 56)))
engine.addComponent(Cube(engine,0,0,-600,300,col))
engine.addComponent(Cube(engine,0,0,600,300,col))

engine.addComponent(Creature(engine, -20,10,0,"rainbow"))

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
        
    sc.createScreen(screen)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    ticks += 1
    fps += time.time()-tm
    #print(c)

    if (fps >= 1):
        fps = 0
        print(ticks)
        ticks = 0

    #clock.tick(60)

pygame.quit()
