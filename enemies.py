import pygame
import constants

from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.x_velocity = 0
        self.y_velocity = 0

        self.walking_frames_right = []
        self.walking_frames_left = []
        self.still_image = None

        self.counter = 0
        self.direction = "S"
        self.level = None
        self.image = None


class Grue(Enemy):

    def __init__(self, x, y, level):
        Enemy.__init__(self)

        self.x_velocity = -2
        self.y_velocity = 0

        sprite_sheet = SpriteSheet('images\\GrueBloodyGrin.png')

        image = sprite_sheet.get_image(0, 0, 55, 70)
        self.walking_frames_right.append(image)
        image = sprite_sheet.get_image(0, 70, 55, 70)
        self.walking_frames_left.append(image)
        self.still_image = sprite_sheet.get_image(60, 70, 55, 70)

        self.image = self.still_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.level = level

    def update(self):

        self.gravity()

        # x vector movement and collision detection
        self.rect.x += self.x_velocity
        if self.x_velocity > 0:
            self.image = self.walking_frames_right[0]
        if self.x_velocity < 0:
            self.image = self.walking_frames_left[0]
        if (self.rect.x - self.level.world_shift) >= (self.level.level_limit * -1):
            self.x_velocity *= -1
        if (self.rect.x - self.level.world_shift) <= 0:
            self.x_velocity *= -1

        surfaces_hit = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for surface in surfaces_hit:
            self.x_velocity *= -1

        # Y vector movement and collision detection
        self.rect.y += self.y_velocity

        surfaces_hit = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for surface in surfaces_hit:
            if self.y_velocity > 0:
                self.rect.bottom = surface.rect.top
            elif self.y_velocity < 0:
                self.rect.top = surface.rect.bottom

            self.y_velocity = 0

    def gravity(self):
        if self.y_velocity == 0:
            self.y_velocity = 1
        else:
            self.y_velocity += .35

        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.y_velocity >= 0:
            self.y_velocity = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height





