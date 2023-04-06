import pygame
from pygame.transform import scale

pygame.init()
font = pygame.font.SysFont('04b03', 30)

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, image,buttonText = "CLICK", onclickFunction=None, onePress=False):
        super().__init__()
        self.x = x
        self.y = y
        self.onclickFunction = onclickFunction
        self.onePress = onePress

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.image = image
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

    def update(self, screen):

        mousePos = pygame.mouse.get_pos()

        if self.buttonRect.collidepoint(mousePos):
            pass

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                pass

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False


    def draw(self, screen):
        screen.blit(self.image, self.buttonRect)

class Clicker_Button(Button):
    def __init__(self,x,y,image):
        super().__init__()