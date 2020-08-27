from traceback import format_exc
import pygame
from pygame import surfarray
from pygame.locals import*
import time
from PIL import Image, ImageDraw

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

pygame.init()

width = 1280
height = 720
screen = pygame.display.set_mode((width, height))

color = (255, 100, 100)
screen.fill((color))
running = True

sc = Screen(width, height, color)

clock = pygame.time.Clock()

camera = Camera(None, 0, 0, -20, width/2, height/2)

engine = Engine(sc, camera, Light(1, 1, 1))
camera.engine = engine

engine.addComponent(Cube(engine, 0, 0, 0, 1, "rainbow", False))

bc = Image.open("background_test.png")
pixels = bc.convert("RGB").load()

while running:
    tm = time.time()
    
    try:
        engine.Update()
        engine.Draw()
    except Exception as e:
        print(repr(e))
        print(format_exc())
        running = False
        
    surfarray.blit_array(screen, sc.drawGreenScreen(pixels))
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    l = time.time()-tm
    #print(l)

    clock.tick(60)

pygame.quit()

