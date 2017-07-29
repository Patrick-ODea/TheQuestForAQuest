import pygame
import constants

def start_screen():

    pygame.init()
    pygame.mixer.init()

    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("The Quest")
    pygame.display.set_icon((pygame.image.load('images\\odiehq.png')))
    music = pygame.mixer.music.load('sounds\\GrassyWorld.mp3')
    intro = True
    background = pygame.image.load('images\\fossil_cave.png')
    logo1 = pygame.image.load('images\\startmenuone.png')
    logo2 = pygame.image.load('images\\startmenuoneMouseOver.png')
    logo3 = pygame.image.load('images\\pressquestenter1.png')
    logo4 = pygame.image.load('images\\odiehqdotcomlogo.png')

    ticker = pygame.time.Clock()
    counter = 0
    # THE START SCREEN
    pygame.mixer.music.play(10)
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.stop()
                    intro = False

        screen.blit(background, (0, 0))
        screen.blit(logo1, ((constants.SCREEN_WIDTH / 2 - 155), constants.SCREEN_HEIGHT * (1/3) - 50))
        screen.blit(logo4, (20, (constants.SCREEN_HEIGHT - 120)))
        if counter > 60:
            screen.blit(logo3, ((constants.SCREEN_WIDTH / 2 - 200), constants.SCREEN_HEIGHT * (2/3) - 30))
        pygame.display.update()
        counter += 1
        ticker.tick(15)



