import pygame
from pygame.locals import *

class Bird:
    def __init__(self):
        self.downFlap = pygame.transform.scale2x(pygame.image.load("assets/bluebird-downflap.png").convert_alpha())
        self.midFlap = pygame.transform.scale2x(pygame.image.load("assets/bluebird-midflap.png").convert_alpha())
        self.upFlap = pygame.transform.scale2x(pygame.image.load("assets/bluebird-upflap.png").convert_alpha())

        self.frames = [self.downFlap, self.midFlap, self.upFlap]

        self.frameIndex = 0

        self.surface = self.frames[self.frameIndex]
        self.rect = self.surface.get_rect(center = (100, 512))
        
        self.movement = 0

    def draw(self, screen):
        rotatedSurface = pygame.transform.rotozoom(self.surface, -self.movement * 3, 1)
        screen.blit(rotatedSurface, self.rect)

    def advance(self, gravity):
        self.movement += gravity
        self.rect.centery += self.movement

    def flap(self):
        self.movement = 0
        self.movement -= 12

    def hasCollided(self, screen):
        return (self.rect.top <= -100 or self.rect.bottom >= 1025)
    
    def nextFrame(self):
        if self.frameIndex < 2:
            self.frameIndex += 1       
        else:
            self.frameIndex = 0  

        self.surface = self.frames[self.frameIndex]
        self.rect = self.surface.get_rect(center = (100, self.rect.centery))

