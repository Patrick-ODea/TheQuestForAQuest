import pygame
import constants
import platforms
import enemies


class Level():
    # levels
    def __init__(self, player):
        self.platform_list = None
        self.enemy_list = None
        self.background = None

        self.world_shift = 0
        self.level_limit = -3200
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    def update(self):
        self.platform_list.update()


    def draw(self, screen):
        screen.fill(constants.WHITE)
        screen.blit(self.background, (self.world_shift // 3, 0))

        self.platform_list.draw(screen)


    def shift_world(self, shift_x):
        self.world_shift += shift_x

        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x


class Level_01(Level):
    def __init__(self, player):
        Level.__init__(self, player)

        self.background = pygame.image.load("images\\background0.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -3200


        # Grabbing platform sprites from platform.py and places them in the level. In this case Building level 01
        level = [[platforms.GRASS_LEFT, 500, 500],
                 [platforms.GRASS_MIDDLE, 570, 500],
                 [platforms.GRASS_RIGHT, 640, 500],
                 [platforms.STONE_PLATFORM_LEFT, 770, 500],
                 [platforms.STONE_PLATFORM_MIDDLE, 840, 500],
                 [platforms.STONE_PLATFORM_MIDDLE, 910, 500],
                 [platforms.STONE_PLATFORM_RIGHT, 980, 500],
                 [platforms.STONE_PLATFORM_LEFT, 870, 400],
                 [platforms.STONE_PLATFORM_MIDDLE, 940, 400],
                 [platforms.STONE_PLATFORM_MIDDLE, 1010, 400],
                 [platforms.STONE_PLATFORM_RIGHT, 1070, 400],
                 [platforms.STONE_PLATFORM_LEFT, 900, 300],
                 [platforms.STONE_PLATFORM_MIDDLE, 970, 300],
                 [platforms.STONE_PLATFORM_MIDDLE, 1040, 300],
                 [platforms.STONE_PLATFORM_RIGHT, 1100, 300],
                 [platforms.WALL_SECTION, 1600, 530],
                 [platforms.WALL_SECTION, 1600, 460],
                 [platforms.WALL_SECTION, 1600, 390]

                 ]

        # This for loop takes the platforms in the level array ands object and location to list.
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        foe = enemies.Grue(600, 400, self)
        self.enemy_list.add(foe)
        foe = enemies.Grue(2000, 400, self)
        self.enemy_list.add(foe)


class Level_02(Level):
    def __init__(self, player):
        Level.__init__(self, player)

        self.background = pygame.image.load("images\\swamp1024.png").convert()
        self.level_limit = -4000

        level = [[platforms.GRASS_LEFT, 500, 500],
                 [platforms.GRASS_MIDDLE, 570, 500],
                 [platforms.GRASS_RIGHT, 640, 500],

                 ]
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        foe = enemies.Grue(400, 400, self)
        self.enemy_list.add(foe)
