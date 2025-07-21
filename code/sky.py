import pygame
from settings import *
from support import import_folder

class Rain:
    def __init__(self, all_sprites):
        self.all_sprites = all_sprites
        self.rain_drops = import_folder("graphics/rain/drops/")
        self.rain_floor = import_folder("graphics/rain/floor/")