import pygame
from pygame.locals import *

class Floor:
    def __init__(self):
        self.surface = pygame.image.load("assets/base.png").convert()
        self.surface = pygame.transform.scale2x(self.surface)
        self.x = 0
        self.y = 900


    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))
        screen.blit(self.surface, (self.x + 576, self.y))

    def advance(self):
        self.x -= 1
        if self.x <= -576:
            self.x = 0