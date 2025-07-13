import pygame
from os import listdir
from os.path import join, isfile

def import_folder(path):
    surface_list = []

    files = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith('.png')]

    files.sort()

    for file_name in files:
        full_path = join(path, file_name)
        image_surf = pygame.image.load(full_path).convert_alpha()
        surface_list.append(image_surf)

    return surface_list
