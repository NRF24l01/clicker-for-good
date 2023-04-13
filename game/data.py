import pygame
from pygame.transform import scale
from PIL import Image
import socket
import struct
import hashlib

pygame.init()
font = pygame.font.SysFont('04b03', 30)

class TextInputBox(pygame.sprite.Sprite):
    def __init__(self, x, y, w, font):
        super().__init__()
        self.color = (255, 255, 255)
        self.backcolor = None
        self.pos = (x, y)
        self.width = w
        self.font = font
        self.active = False
        self.text = ""
        self.render_text()

    def render_text(self):
        t_surf = self.font.render(self.text, True, self.color, self.backcolor)
        self.image = pygame.Surface((max(self.width, t_surf.get_width()+10), t_surf.get_height()+10), pygame.SRCALPHA)
        if self.backcolor:
            self.image.fill(self.backcolor)
        self.image.blit(t_surf, (5, 5))
        pygame.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
        self.rect = self.image.get_rect(topleft = self.pos)

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and not self.active:
                self.active = self.rect.collidepoint(event.pos)
            if event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.render_text()

class Button(pygame.sprite.Sprite):
    def __init__(self, image,buttonText = "CLICK", onclickFunction=None, onePress=False):
        super().__init__()
        self.onclickFunction = onclickFunction
        self.onePress = onePress

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.image = image
        self.buttonRect = image.get_rect()

        self.buttonSurf = font.render(str(buttonText).encode('utf-8'), True, (20, 20, 20))

        self.alreadyPressed = False

    def update(self):

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

class Web():
    def __init__(self, ip = "127.0.0.1", port = 9090):
        self.ip = ip
        self.port = port

    def create_sock(self):
        self.sock = socket.socket()
        # подключаемся к 127.0.0.1:9090
        self.sock.connect((self.ip, self.port))

    def load_data(self, gamer_id, gamer_pass):
        self.create_sock()
        print(gamer_id, gamer_pass)
        ghp = hashlib.md5(gamer_pass.encode("utf-8")).hexdigest()
        recv = [gamer_id, ghp]
        send_data = '|'.join(recv)
        bsd = send_data.encode("utf-8")
        print(len(bsd), ghp)
        ln = struct.pack('<I', len(bsd))
        self.sock.send(ln)
        self.sock.send(bsd)
        self.sock.close()
