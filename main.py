import pygame
import math
from obstacles import Obstacle
from character import Bike
from functions import game_over, get_score

pygame.init()

# setting up window
WIDTH, HEIGHT = 1000, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Adrian's game")
font = pygame.font.SysFont("comicsansms", 35)

# setting up background image
background = pygame.image.load("mountains.png").convert_alpha()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background_width = background.get_width()
tiles = math.ceil(WIDTH / background_width + 2)
SCROLL = 0

# setting up clock and FPS
FPS = 60
clock = pygame.time.Clock()

# making a Bike object which would be our "character"
movingbike = pygame.sprite.GroupSingle()
bike = Bike(30, 275)
movingbike.add(bike)
moving = False
jumping = False
GRAVITY = 1
JUMP_HEIGHT = 20
JUMP_SPEED = JUMP_HEIGHT
score = 0

# making obstacles
obstacles = pygame.sprite.Group()
log = Obstacle("log.png",  700, 330)
log2 = Obstacle("log.png", 1700, 330)
obstacles.add(log)
obstacles.add(log2)

# main loop
running = True
enabled = True
while running:
    clock.tick(FPS)
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if enabled:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moving = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    moving = False
            if event.type == pygame.KEYDOWN and not jumping:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    jumping = True

    # Drawing the background, obstacles and bike.
    for i in range(0, tiles):
        window.blit(background, (i * background_width + SCROLL, 0))
        obstacles.draw(window)
        log.update_pos(700 + SCROLL)
        log2.update_pos(1700 + SCROLL)
    movingbike.draw(window)
    get_score(window, font, score)

    # Checking for collision between the bike's right side and the log's left side
    if bike.rect.colliderect(log.rect):
        game_over(window, font, score)
        enabled = False
        moving = False
        jumping = False

    # Checking for pressed arrow key and changing the
    # variables responsible for the movement(scrolling effect)
    # of the background, objects and bike
    if moving:
        draw_background = True
        SCROLL -= 9
        if abs(SCROLL) > background_width:
            SCROLL = 0
        movingbike.update(0.3)

    # Checking for pressed space or arrow up
    # and starting jumping mechanics
    if jumping:
        bike.rect.y -= JUMP_SPEED
        JUMP_SPEED -= GRAVITY
        if JUMP_SPEED < -JUMP_HEIGHT:
            jumping = False
            JUMP_SPEED = JUMP_HEIGHT
            score += 1

     # Updating the display
    pygame.display.update()
pygame.quit()