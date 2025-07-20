import pygame
from settings import *

class Transition:
    def __init__(self, reset, player):
        
        # setup
        self.display_surface = pygame.display.get_surface()
        self.resrt = reset
        self.player = player

        # overlay image
        self.image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.color = 255
        self.speed = -2
    
    def play(self):
        self.color += self.speed
        self.image.fill((self.color, self.color, self.color))
        self.display_surface.blit(self.image, (0, 0))