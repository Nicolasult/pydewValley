import pygame
from settings import *
from support import import_folder
from sprites import Generic
from random import randint

class Drop(Generic):
    def __init__(self, surf, pos, moving, groups, z):

        # general setup
        super().__init__(pos, surf, groups, z)
        self.lifetime = randint(400, 500)
        self.start_time = pygame.time.get_ticks()

        # moving
        self.moving = moving
        if self.moving == True:
            self.pos = pygame.math.Vector2(self.rect.topleft)
            self.direction = pygame.math.Vector2(-2, 4)
            self.speed = randint(200, 250)

    def update(self, dt):
        # movement
        if self.moving:
            self.pos += self.direction + self.speed * dt
            self.rect.topleft = (round(self.pos.x), round(self.pos.y))

        

class Rain:
    def __init__(self, all_sprites):
        self.all_sprites = all_sprites
        self.rain_drops = import_folder("graphics/rain/drops/")
        self.rain_floor = import_folder("graphics/rain/floor/")
        self.floor_w, self.floor_h = pygame.image.load("graphics/workd/ground.png").get_size()

    def create_floor(self):
        Drop()

    def create_drops(self):

    def update(self):
        self.create_floor()
        self.create_drops()