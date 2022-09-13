from traceback import format_exc
import pygame
from pygame import surfarray
from pygame.locals import*
import time


pygame.init()

#full screen
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

width = 1280
height = 720
screen = pygame.display.set_mode((width, height))

color = (255, 255, 255)
screen.fill((color))
running = True

sc = Screen(width, height, color)

clock = pygame.time.Clock()

camera = Camera(None, 0, 0, -20, width/2, height/2)

engine = Engine(sc, camera, Light(1, 1, 1))
camera.engine = engine

engine.addComponent(Axis(engine, 1000))

#cube = Cube(engine, 0, 0, 0, 1, "rainbow", False)
engine.addComponent(Cube(engine, 0, 0, 0, 1, "rainbow", False))
#K - pyramida poskoci nahoru
#L - pyramida poskoci "doprava"
#J - pyramida poskoci "doleva"
engine.addComponent(Pyramid(engine, 0, 10, 0, 1, -1, (255,0,0), True))
engine.addComponent(Cube(engine,0,-20,0,10, (255,255,255),False))

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
    #surfarray.blit_array(screen, sc.drawScreen())
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    l = time.time()-tm
    #print(l)

    clock.tick(60)

pygame.quit()
