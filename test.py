import pygame
pygame.init()

from Snejky.camera import Camera

width = 1280
height = 720
screen = pygame.display.set_mode((width, height))

color = (255, 255, 255)
screen.fill((color))

camera = Camera((0, 0, 0), width/2, height/2)

while True:

    pygame.draw.polygon(screen, (255,0,0), [
        (0, 0), (50, 50), (0, 50)        
    ])

    screen.set_at((60, 60), (0,255,0))

    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    pygame.time.Clock().tick(60)

pygame.quit()