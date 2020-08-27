from traceback import format_exc
import pygame
from pygame import surfarray
from pygame.locals import*
import time
from PIL import Image, ImageDraw
from Video.makeVideo import MakeVideo

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

color = (255, 0, 120)
screen.fill((color))
running = True

sc = Screen(width, height, color)

clock = pygame.time.Clock()

camera = Camera(None, 0, 0, -20, width/2, height/2)

engine = Engine(sc, camera, Light(1, 1, 1))
camera.engine = engine

cube = Cube(engine, 0, -5, 0, 1, "rainbow", False)

engine.addComponent(cube)

bc = Image.open("Snejky\\background_test.png")
pixels = bc.convert("RGB").load()

mk = MakeVideo()
up = True

frameNumber = 0
fps = 60
seconds = 1
finalFrameNumber = seconds*fps

times = 0

tim = time.time()
while running:
    tm = time.time()
    if (up):
        cube.Position.y += 0.5
    else:
        cube.Position.y -= 0.5

    if (cube.Position.y >= 5): up = False
    if (cube.Position.y <= -5): up = True
    
    try:
        engine.Update()
        engine.Draw()
    except Exception as e:
        print(repr(e))
        print(format_exc())
        running = False

    frame = sc.drawGreenScreen(pixels)   
    #surfarray.blit_array(screen, frame)
    #pygame.display.flip()

    frameNumber += 1
    running = mk.recordFrame(frame, frameNumber, finalFrameNumber, fps)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    l = time.time()-tm
    times += l
    print(str(frameNumber) + "/" + str(finalFrameNumber) + " - " + str(frameNumber/(finalFrameNumber/100)) + "%")
    print("Time for actual frame: " + str(l) + " s")
    average = times / frameNumber
    print("Average time for frame: " + str(average) + " s")
    estimatedTime = finalFrameNumber*average - times
    print("Estimated time: ")
    print("  " + str(estimatedTime) + " s")
    print("  " + str(estimatedTime/60) + " min")
    print("  " + str((estimatedTime/60)/60) + " hod")

    print("Time: ")
    print("  " + str(times) + " s")
    print("  " + str(times/60) + " min")
    print("  " + str((times/60)/60) + " hod")
    print("-----------------------------------------")

pygame.quit()

print("Time: " + str(time.time() - tim) + " s")
print("Frames: " + str(frameNumber))

