#import libs
import pygame
from pygame.transform import scale
import sys

#import system files
from spraites import Button

#Inits
pygame.init()

#Configs
width, height = 640, 480
fps = 60

#Other
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
objects = pygame.sprite.Group()
font = pygame.font.SysFont("04b03", 30)
game_state = "start"#start, game, end
resurses_locate = "resurses/"

#Some def`s
def start():
    global game_state
    #Will run game
    game_state = "game"

#Create game objects
but1 = Button(30, 30, pygame.image.load(resurses_locate+"start_button.png"), (640, 480), 'START', start)
objects.add(but1)
menu_fone = scale(pygame.image.load(resurses_locate+"menu.png"), (640, 480))
game_fone = scale(pygame.image.load(resurses_locate+"game.png"), (640, 480))
green_5 = [scale(pygame.image.load(resurses_locate+"5_green_up.png"), (640, 480)), scale(pygame.image.load(resurses_locate+"5_green_down.png"), (640, 480))]

# Game loop.
while True:
    print(game_state)
    if game_state == "start":
        screen.blit(menu_fone, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for object in objects:
            object.process(screen)

    elif game_state == "game":
        screen.blit(game_fone, (0, 0))
        for object in objects:
            object.process(screen)
            object.kill()
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    pygame.display.flip()
    fpsClock.tick(fps)