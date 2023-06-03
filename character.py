import pygame

class Bike(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.transform.scale2x(pygame.image.load("sportbike1.png")))
        self.sprites.append(pygame.transform.scale2x(pygame.image.load("sportbike2.png")))
        self.currentsprite = 0
        self.image = self.sprites[self.currentsprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def update(self, speed):
        self.currentsprite += speed
        if self.currentsprite >= len(self.sprites):
            self.currentsprite = 0
        self.image = self.sprites[int(self.currentsprite)]