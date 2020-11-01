import pygame
from pygame.locals import *
import sys
from floor import Floor
from bird import Bird
from pipe import Pipe
from text import Text

class Game:
    def __init__(self):
        self.screen = None
        self.clock = None
        self.gameActive = False

        self.gravity = 0
        
        self.score = 0
        self.scoreText = None
        
        self.highScore = 0
        
        self.background = None
        self.floor = None
        self.bird = None

        self.pipes = None
        self.SPAWNPIPE = None

        self.BIRDFLAP = None

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((576,1025)) 
        self.clock = pygame.time.Clock()
        self.gameActive = True

        self.gravity = 0.25
        
        self.score = 0
        self.scoreText = Text(self.score, 40)
        
        self.highScore = 0
        self.highScoreText = Text(f'High score: {int(self.score)}', 40)

        self.background = pygame.image.load("assets/background-day.png").convert()
        self.background = pygame.transform.scale2x(self.background)

        self.floor = Floor()
        self.bird = Bird()

        self.pipes = []
        self.SPAWNPIPE = pygame.USEREVENT

        self.BIRDFLAP = pygame.USEREVENT + 1

        pygame.time.set_timer(self.SPAWNPIPE, 1200)
        pygame.time.set_timer(self.BIRDFLAP, 200)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.gameActive:
                self.bird.flap()
            if event.key == pygame.K_SPACE and not self.gameActive:
                self.gameActive = True
                self.pipes.clear()
                self.bird = Bird()
                self.score = 0

        if event.type == self.SPAWNPIPE:
            self.pipes.append(Pipe([400, 600, 800]))

        if event.type == self.BIRDFLAP:
            self.bird.nextFrame()

    def on_loop(self):
        self.floor.advance()

        self.bird.advance(self.gravity)

        if self.bird.hasCollided(self.screen):
            self.gameActive = False
    

        for pipe in self.pipes:
            pipe.advance()
            if pipe.hasCollided(self.bird.rect):
                self.gameActive = False

    def on_render(self):

        self.screen.blit(self.background, (0, 0))

        if self.gameActive:
            self.bird.draw(self.screen)

            for pipe in self.pipes:
                pipe.draw(self.screen)

            self.score += 0.01
            self.scoreText.updateText(int(self.score))
        else:
            if self.highScore < self.score:
                self.highScore = self.score
            self.highScoreText.updateText(f'High score: {int(self.highScore)}')
            self.highScoreText.draw(self.screen, (288,850))


        self.scoreText.draw(self.screen, (288,100))


            

        self.floor.draw(self.screen)

        pygame.display.update()
        self.clock.tick(120)
        
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            sys.exit()
 
        while True:
            for event in pygame.event.get():
                self.on_event(event)
            
            self.on_loop()
            self.on_render()
        self.on_cleanup()