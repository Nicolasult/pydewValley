import pygame
from settings import *

class SoilLayer:
    def __init__(self, all_sprites):
        
        # sprite groups
        self.all_sprites = all_sprites
        self.soil_sprites = pygame.sprite.Group()

        # graphics
        self.soil_surf = pygame.image.load("graphics/soil/o.png").convert_alpha()