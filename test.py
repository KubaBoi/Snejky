import pygame
pygame.init()

width = 1280
height = 720
screen = pygame.display.set_mode((width, height))

color = (255, 255, 255)
screen.fill((color))

while True:

    pygame.draw.polygon(screen, (255,0,0), [
        (0, 0), (50, 50), (0, 50)        
    ])

    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    pygame.time.Clock().tick(60)

pygame.quit()