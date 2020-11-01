import pygame
from pygame.locals import *
import random

class Pipe:
    def __init__(self, hieghts):
        hieght = random.choice(hieghts)

        self.surface = pygame.image.load("assets/pipe-green.png").convert()


        self.bottomSurface = pygame.transform.scale2x(self.surface)
        self.bottomRect = self.bottomSurface.get_rect(midtop = (700, hieght))

        self.topSurface = pygame.transform.flip(self.bottomSurface, False, True)
        self.topRect = self.topSurface.get_rect(midbottom = (700, hieght - 300))

        



    def draw(self, screen):
        screen.blit(self.bottomSurface, self.bottomRect)

        screen.blit(self.topSurface, self.topRect)

    def advance(self):
        self.bottomRect.centerx -= 5

        self.topRect.centerx -= 5

    def hasCollided(self, rect):
        return (self.topRect.colliderect(rect) or self.bottomRect.colliderect(rect))
        