import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, imagefile, x, y):
        super().__init__()
        self.image = pygame.transform.scale2x(pygame.image.load(imagefile).convert_alpha())
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update_pos(self, x):
        self.rect.x = x