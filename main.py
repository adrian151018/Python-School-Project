import pygame
import math
from obstacles import Obstacle
from character import Bike
from functions import get_score

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
tiles = math.ceil(WIDTH / background_width + 1)
SCROLL = 0

# setting up clock and FPS
FPS = 60
clock = pygame.time.Clock()
endprogram = False

# making a Bike object which would be our "character"
movingbike = pygame.sprite.GroupSingle()
bike = Bike(30, 275)
movingbike.add(bike)
jumping = False
moving = True
deaths = False
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
trigger_zone_x = log.rect.x
trigger_zone_y = log.rect.y
trigger_zone_width = log.rect.width
trigger_zone_height = log.rect.height + 200

def menu():
    global endprogram
    endprogram = False
    menurun = True
    window.fill((255, 255, 255))
    while menurun:
        if deaths:
            menu_text = font.render("Press any key to restart", True, (0, 0, 0))  # White color for the text
            score_text = font.render("Your Score: " + str(score), True, (0, 0, 0))
            score_text_rect = score_text.get_rect(center = (WIDTH // 2, HEIGHT // 2 + 50))
            window.blit(score_text, score_text_rect)
        else:
            menu_text = font.render("Press any key to start", True, (0, 0, 0))

        menu_text_rect = menu_text.get_rect(center = (WIDTH // 2, HEIGHT // 2 - 50))
        window.blit(menu_text, menu_text_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menurun = False
                endprogram = True
            if event.type == pygame.KEYDOWN:
                menurun = False

menu()


running = True
enabled = True
while running and not endprogram:# main loop
    clock.tick(FPS)
    for event in pygame.event.get():# event handler
        if event.type == pygame.QUIT:
            running = False
        if enabled:
            if event.type == pygame.KEYDOWN and not jumping:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    jumping = True

    for i in range(0, tiles):# Drawing the background, obstacles and bike.
        window.blit(background, (i * background_width + SCROLL, 0))
        obstacles.draw(window)
        log.update_pos(700 + SCROLL)
        log2.update_pos(1700 + SCROLL)
        trigger_zone_x += SCROLL
    movingbike.draw(window)
    get_score(window, font, score)

    if bike.rect.colliderect(log.rect):# Checking for collision between the bike's right side and the log's left side
        deaths = True
        enabled = False
        moving = False
        menu()
        score = 0
        enabled = True
        moving = True
        SCROLL = 0
        continue
    if moving:
        draw_background = True
        SCROLL -= 9
        if abs(SCROLL) > background_width:
            SCROLL = 0
        movingbike.update(0.3)

    if jumping:# Checking for pressed space or arrow up and starting jumping mechanics
        bike.rect.y -= JUMP_SPEED
        JUMP_SPEED -= GRAVITY
        if JUMP_SPEED < -JUMP_HEIGHT:
            jumping = False
            JUMP_SPEED = JUMP_HEIGHT
            if bike.rect.colliderect((trigger_zone_x, trigger_zone_y, trigger_zone_width, trigger_zone_height)):
                score += 1

    pygame.display.update()# Updating the display
pygame.quit()