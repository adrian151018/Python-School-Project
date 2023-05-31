import pygame
import math


pygame.init()

class Bike(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load("sportbike1.png"))
        self.sprites.append(pygame.image.load("sportbike2.png"))
        self.currentsprite = 0
        self.image = self.sprites[self.currentsprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def update(self, speed):
        self.currentsprite += speed
        if self.currentsprite >= len(self.sprites):
            self.currentsprite = 0
        self.image = self.sprites[int(self.currentsprite)]

WIDTH, HEIGHT = 1000, 500
FPS = 60
SCROLL = 0
window = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load("jungle.png").convert_alpha()
window.blit(background, (0, 0))
background_width = background.get_width()
tiles = math.ceil(WIDTH / background_width + 1)
clock = pygame.time.Clock()
movingsprites = pygame.sprite.Group()
bike = Bike(0, 370)
movingsprites.add(bike)
movingsprites.draw(window)
moving = False

running = True
while(running):
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moving = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving = False
        
    if moving:
        for i in range(0, tiles):
            window.blit(background, (i * background_width + SCROLL, 0))
        SCROLL -= 3
        if abs(SCROLL) > background_width:
            SCROLL = 0
        movingsprites.draw(window)
        movingsprites.update(0.1)
    pygame.display.update()

pygame.quit()