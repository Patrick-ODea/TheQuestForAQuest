# If you would like to help email me at Patrick.ODea@aol.com or please get a hold of me on github.
# Any advices of suggestions welcome.
import pygame
import constants
import levels
import gameStartScreen



from player import Player, ShootArrow
from enemies import Enemy


def main():

    gameStartScreen.start_screen()

    # Main Program
    pygame.init()

    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("The Quest")
    pygame.display.set_icon((pygame.image.load('images\\odiehq.png')))
    music = pygame.mixer.Sound('sounds\\little town - orchestral.ogg')

    # Create the Player
    player = Player()
    enemy = Enemy()


    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01(player))
    level_list.append(levels.Level_02(player))

    # Set the current level
    current_level_number = 0
    current_level = level_list[current_level_number]

    # Create a sprite group with all active sprites
    active_sprite_list = pygame.sprite.Group()
    attack_sprite_list = pygame.sprite.Group()



    # Set Players starting level (current_level_number) Starting x and y position. Then add player tp active sprites.
    player.level = current_level
    player.rect.x = 340
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)
    enemy_sprite_list = level_list[current_level_number].enemy_list



    # Loop until the user clicks the close button.
    done = False

    clock = pygame.time.Clock()
    music.play(10)



    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

            # KEYBOARD COMMANDS TO USE PLAYER.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_SPACE:
                    player.attack("Y")

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
                if event.key == pygame.K_SPACE:
                    if player.counter >= 8:
                        arrow = ShootArrow(player.rect.x, player.rect.y, player.direction, player.level)
                        attack_sprite_list.add(arrow)
                        print(arrow.rect)
                    player.attack("N")
                    player.counter = 0

        # Update the player.
        active_sprite_list.update()
        enemy_sprite_list.update()
        attack_sprite_list.update()

        # Update items in the level
        current_level.update()


        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)
            if current_position >= 120 and current_level_number == 0:
                player.stop()
            elif current_position >= 120 and current_level_number > 0:
                player.stop()

    # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_number < len(level_list) - 1:
                current_level_number += 1
                current_level = level_list[current_level_number]
                player.level = current_level
                enemy.level = current_level


        # Drawing Codes #######################################################################
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        enemy_sprite_list.draw(screen)
        attack_sprite_list.draw(screen)

        # #################################################################################

        # Clock set to 60 fps
        clock.tick(60)

        # update display
        pygame.display.flip()

    # Quit
    pygame.quit()


if __name__ == "__main__":
    main()