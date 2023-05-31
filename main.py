import pygame
import math

WIDTH, HEIGHT = 1000, 500
FPS = 60
window = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load("jungle.png").convert_alpha()
background_width = background.get_width()
tiles = math.ceil(WIDTH / background_width + 1)
SCROLL = 0



clock = pygame.time.Clock()
running = True
while(running):
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    for i in range(0, tiles):
        window.blit(background, (i * background_width + SCROLL, 0))

    SCROLL -= 5

    if abs(SCROLL) > background_width:
        SCROLL = 0

    pygame.display.update()

pygame.quit()