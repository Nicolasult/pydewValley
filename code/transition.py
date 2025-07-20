import pygame
from settings import *

class Transition:
    def __init__(self, reset, player):
        
        # setup
        self.display_surface = pygame.display.get_surface()
        self.resrt = reset
        self.player = player