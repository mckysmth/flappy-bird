import pygame
from pygame.locals import *

class Text:
    def __init__(self, text, size):
        self.fontSize = size
        self.font = str(text)

        self.ganeFont = pygame.font.Font("flappy font/Apple Symbols.ttf",self.fontSize)

    def draw(self, screen, pos):
        surface = self.ganeFont.render(self.font, True, (255, 255, 255))
        rect = surface.get_rect(center = pos)
        screen.blit(surface, rect)

    def updateText(self, text):
        self.font = str(text)


        