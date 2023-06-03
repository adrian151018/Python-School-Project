import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, imagefile, x, y):
        super().__init__()
        self.image = pygame.transform.scale2x(pygame.image.load(imagefile).convert_alpha())
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def update_pos(self, x):
        self.rect.x = x