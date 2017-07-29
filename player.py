import pygame
import constants

from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet

'''
Need work

-Need to be able to edit jump and bow shooting sound ogg file types.
-Need to pick frame for the player to be while in air
-Need to change set up so when moving left and right on a moving platform while not moving
                animation still plays walk





'''


class Player (pygame.sprite.Sprite):

    def __init__(self):
        # init  parent class
        super().__init__()

        # speed of player left/right and up/down
        self.change_x = 0
        self.change_y = 0

        # player sounds
        self.jump_sound = pygame.mixer.Sound('sounds\\jumppp11.ogg')
        self.bow_shot_sound = pygame.mixer.Sound('sounds\\bow_sound.ogg')


        # animation arrays
        self.walking_frames_left = []
        self.walking_frames_right = []

        # Attacking Image Arrays
        self.bow_attack_frames_right = []
        self.bow_attack_frames_left = []
        self.arrow = None

        self.attcking = None
        self.counter = 0
        # Which direction is the player facing
        self.direction = "R"
        self.attacking = "N"

        # list of other level objects that we can come into contact with
        self.level = None

        # Player Animation array images facing right.
        sprite_sheet = SpriteSheet('images\\robe_walking_spritesheet.png')
        image = sprite_sheet.get_image(20, 200, 45, 52)
        self.walking_frames_right.append(image)
        image = sprite_sheet.get_image(80, 200, 45, 52)
        self.walking_frames_right.append(image)
        image = sprite_sheet.get_image(140, 200, 45, 52)
        self.walking_frames_right.append(image)
        image = sprite_sheet.get_image(210, 200, 45, 52)
        self.walking_frames_right.append(image)
        image = sprite_sheet.get_image(270, 200, 45, 52)
        self.walking_frames_right.append(image)
        image = sprite_sheet.get_image(330, 200, 45, 52)
        self.walking_frames_right.append(image)
        image = sprite_sheet.get_image(400, 200, 45, 52)
        self.walking_frames_right.append(image)
        image = sprite_sheet.get_image(460, 200, 45, 52)
        self.walking_frames_right.append(image)
        image = sprite_sheet.get_image(530, 200, 45, 52)
        self.walking_frames_right.append(image)

        # now player sprite images facing left
        image = sprite_sheet.get_image(20, 200, 45, 52)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_left.append(image)
        image = sprite_sheet.get_image(80, 200, 45, 52)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_left.append(image)
        image = sprite_sheet.get_image(140, 200, 45, 52)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_left.append(image)
        image = sprite_sheet.get_image(210, 200, 45, 52)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_left.append(image)
        image = sprite_sheet.get_image(270, 200, 45, 52)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_left.append(image)
        image = sprite_sheet.get_image(330, 200, 45, 52)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_left.append(image)
        image = sprite_sheet.get_image(400, 200, 45, 52)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_left.append(image)
        image = sprite_sheet.get_image(460, 200, 45, 52)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_left.append(image)
        image = sprite_sheet.get_image(530, 200, 45, 52)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_left.append(image)

        # Attack Images Loaded
        sprite_sheet = SpriteSheet('images\\robe_bow_attack_spritesheet.png')
        image = sprite_sheet.get_image(10, 200, 45, 52)
        self.bow_attack_frames_right.append(image)
        image = sprite_sheet.get_image(78, 200, 45, 52)
        self.bow_attack_frames_right.append(image)
        image = sprite_sheet.get_image(145, 200, 45, 52)
        self.bow_attack_frames_right.append(image)
        image = sprite_sheet.get_image(205, 200, 45, 52)
        self.bow_attack_frames_right.append(image)
        image = sprite_sheet.get_image(270, 200, 45, 52)
        self.bow_attack_frames_right.append(image)
        image = sprite_sheet.get_image(340, 200, 45, 52)
        self.bow_attack_frames_right.append(image)
        image = sprite_sheet.get_image(400, 200, 55, 52)
        self.bow_attack_frames_right.append(image)
        self.bow_attack_frames_right.append(image)
        self.bow_attack_frames_right.append(image)
        self.bow_attack_frames_right.append(image)

        image = sprite_sheet.get_image(10, 200, 45, 52)
        image = pygame.transform.flip(image, True, False)
        self.bow_attack_frames_left.append(image)
        image = sprite_sheet.get_image(78, 200, 45, 52)
        image = pygame.transform.flip(image, True, False)
        self.bow_attack_frames_left.append(image)
        image = sprite_sheet.get_image(145, 200, 45, 52)
        image = pygame.transform.flip(image, True, False)
        self.bow_attack_frames_left.append(image)
        image = sprite_sheet.get_image(205, 200, 45, 52)
        image = pygame.transform.flip(image, True, False)
        self.bow_attack_frames_left.append(image)
        image = sprite_sheet.get_image(270, 200, 45, 52)
        image = pygame.transform.flip(image, True, False)
        self.bow_attack_frames_left.append(image)
        image = sprite_sheet.get_image(340, 200, 45, 52)
        image = pygame.transform.flip(image, True, False)
        self.bow_attack_frames_left.append(image)
        image = sprite_sheet.get_image(400, 200, 55, 52)
        image = pygame.transform.flip(image, True, False)
        self.bow_attack_frames_left.append(image)
        self.bow_attack_frames_left.append(image)
        self.bow_attack_frames_left.append(image)
        self.bow_attack_frames_left.append(image)

        # set starting player image and get its rectangle
        self.image = self.walking_frames_right[0]
        self.rect = self.image.get_rect()

    def update(self):

        self.calc_gravity()
        self.rect.x += self.change_x
        self.animate()
        self.collide()

    def animate(self):

        # walking animation
        position = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (position // 30) % len(self.walking_frames_right)
            self.image = self.walking_frames_right[frame]
        else:
            frame = (position // 30 % len(self.walking_frames_left))
            self.image = self.walking_frames_left[frame]
        # attack animation
        if self.attacking == "Y":
            if self.direction == "R":
                if self.counter < len(self.bow_attack_frames_right) - 1:
                    self.image = self.bow_attack_frames_right[int(self.counter // 1)]
                    print(self.counter, self.counter // 1)
                    self.counter += .25
                if self.counter == len(self.bow_attack_frames_right) - 1:
                    self.image = self.bow_attack_frames_right[int(self.counter // 1)]
            elif self.direction == "L":
                if self.counter < len(self.bow_attack_frames_left) - 1:
                    self.image = self.bow_attack_frames_left[int(self.counter // 1)]
                    self.counter += .25
                if self.counter == len(self.bow_attack_frames_left) - 1:
                    self.image = self.bow_attack_frames_left[int(self.counter // 1)]

    def collide(self):
        # if we hit something it will line up the two edges of the sprites
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

        foes = pygame.sprite.spritecollide(self, self.level.enemy_list, False)
        for foe in foes:
            pygame.quit()

    def calc_gravity(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # if its ok to jump then jump
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.jump_sound.play()
            self.change_y -= 10

    def go_left(self):
        self.change_x = -5
        self.direction = "L"

    def go_right(self):
        self.change_x = 5
        self.direction = "R"

    def stop(self):
        self.change_x = 0

    def attack(self, state):
        self.attacking = state


class ShootArrow(pygame.sprite.Sprite):

    def __init__(self, attack_x, attack_y, attack_direction, player_level):
        super().__init__()

        # shoot sound
        self.bow_shot_sound = pygame.mixer.Sound('sounds\\shoot.ogg')
        self.arrow_missed_sound = pygame.mixer.Sound('sounds\\arrowMiss.wav')
        self.arrow_kill_sound = pygame.mixer.Sound('sounds\\DeathGrue.wav')

        # Arrow Sprite
        self.level = player_level
        self.attack_sprite_group = []
        sprite_sheet = SpriteSheet('images\\WEAPON_arrow.png')
        image = sprite_sheet.get_image(790, 230, 35, 10)
        self.attack_sprite_group.append(image)
        image = pygame.transform.flip(image, True, False)
        self.attack_sprite_group.append(image)
        self.rightshot = 5
        self.leftshot = -5
        self.attack_direction = attack_direction
        self.change_y = 0
        if self.attack_direction == "R":
            self.image = self.attack_sprite_group[0]
        if self.attack_direction == "L":
            self.image = self.attack_sprite_group[1]

        self.rect = self.image.get_rect()
        self.rect.x = attack_x
        self.rect.y = attack_y + 26
        self.bow_shot_sound.play()

    def update(self):

        if self.attack_direction == "R":
            self.rect.x += self.rightshot
        if self.attack_direction == "L":
            self.rect.x += self.leftshot
        if self.rect.y >= (constants.SCREEN_HEIGHT + 5):
            self.kill()
            self.arrow_missed_sound.play()
        if self.change_y == 0:
            self.change_y = .05
        else:
            self.change_y += .01
        self.rect.top += self.change_y

        walls = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for wall in walls:
            self.kill()
            self.arrow_missed_sound.play()

        foes = pygame.sprite.spritecollide(self, self.level.enemy_list, True)
        for foe in foes:
            self.arrow_kill_sound.play()
            self.kill()

