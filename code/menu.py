import pygame
from settings import *

class Menu:
    def __init__(self, player, toggle_menu):
        # general setup
        self.player = player
        self.toggle_menu = toggle_menu
        self.display_surface = pygame.display.get_surf()
        self.font = pygame.font.Font("font/LycheeSoda.ttf", 30)