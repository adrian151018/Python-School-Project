import pygame
#check
class Bike(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.moving_sprites = []  # Sprites for when the bike is moving
        self.jumping_sprites = []  # Sprites for when the bike is jumping

        # Load moving sprites
        self.moving_sprites.append(pygame.transform.scale2x(pygame.image.load("sportbike1.png")))
        self.moving_sprites.append(pygame.transform.scale2x(pygame.image.load("sportbike2.png")))

        # Load jumping sprites
        self.jumping_sprites.append(pygame.transform.scale2x(pygame.image.load("jump1.png")))
        #self.jumping_sprites.append(pygame.transform.scale2x(pygame.image.load("jumpbike2.png")))

        self.current_sprite = 0
        self.is_jumping = False
        self.image = self.moving_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def update(self, speed):
        if not self.is_jumping:
            # Bike is moving
            self.current_sprite += speed
            if self.current_sprite >= len(self.moving_sprites):
                self.current_sprite = 0
            self.image = self.moving_sprites[int(self.current_sprite)]
        else:
            # Bike is jumping
            self.current_sprite += speed
            if self.current_sprite >= len(self.jumping_sprites):
                self.current_sprite = 0
                self.is_jumping = False
            self.image = self.jumping_sprites[int(self.current_sprite)]