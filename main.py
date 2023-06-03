import pygame
import math
import random
from obstacles import Obstacle
from character import Bike

pygame.init()

# setting up window
WIDTH, HEIGHT = 1000, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Adrian's game")

# setting up background image
background = pygame.image.load("mountains.png").convert_alpha()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background_rect = background.get_rect()

window.blit(background, (0, 0))
background_width = background.get_width()
tiles = math.ceil(WIDTH / background_width + 2)
SCROLL = 0

# setting up clock and FPS
FPS = 60
clock = pygame.time.Clock()

# making a Bike object which would be our "character"
movingbike = pygame.sprite.Group()
bike = Bike(30, 275)
movingbike.add(bike)
movingbike.draw(window)
moving = False
jumping = False
GRAVITY = 1
JUMP_HEIGHT = 20
JUMP_SPEED = JUMP_HEIGHT

# making obstacles
obstacles = pygame.sprite.Group()
log1 = Obstacle("log.png", random.randrange(300, WIDTH), 330)
obstacles.add(log1)

# main loop
running = True
while running:
    clock.tick(FPS)
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moving = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving = False
        if event.type == pygame.KEYDOWN and not jumping:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                jumping = True

    # checking for pressed arrow key and
    # starting background and "character" animation
    if moving:
        for i in range(0, tiles):
            window.blit(background, (i * background_width + SCROLL, 0))
            obstacles.draw(window)
            log1.update_pos(i * background_width + SCROLL)

        SCROLL -= 7
        if abs(SCROLL) > background_width:
            SCROLL = 0

        movingbike.draw(window)
        movingbike.update(0.3)

    # checking for pressed space or arrow up
    # and starting jumping mechanics
    if jumping:
        bike.rect.y -= JUMP_SPEED
        JUMP_SPEED -= GRAVITY
        if JUMP_SPEED < -JUMP_HEIGHT:
            jumping = False
            JUMP_SPEED = JUMP_HEIGHT

    # updating the display
    pygame.display.update()

pygame.quit()