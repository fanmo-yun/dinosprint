import os
import pygame
from data import *

def load_img(path, isflap, size):
    img_list = []
    for _, _, image_name in os.walk(path):
        for img in image_name:
            all_path = path + '/' + img
            if isflap == False:
                img_list.append(pygame.transform.scale(pygame.image.load(all_path), size))
            else:
                img_list.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(all_path), size), True, False))

    return img_list

def load_background_img():
    path = "./assets/block/Background/"
    background_img = [
        pygame.transform.scale2x(pygame.image.load(path + "background_0001.png")),
        pygame.transform.scale2x(pygame.image.load(path + "background_0002.png")),
        pygame.transform.scale2x(pygame.image.load(path + "background_0007.png")),
        pygame.transform.scale2x(pygame.image.load(path + "background_0008.png")),
        pygame.transform.scale2x(pygame.image.load(path + "background_0000.png")),
    ]
    return background_img

def load_start_menu_cha():
    img_start = []
    path = "./assets/character/sprites/walk/"
    path1 = "./assets/character/sprites/idle/Dino1.png"
    path2 = "./assets/character/sprites/hurt/Dino15.png"
    for _, _, image_name in os.walk(path):
        for image in image_name:
            img_start.append(pygame.transform.scale(pygame.image.load(path + image), (45, 54)))
    
    chose1 = pygame.transform.scale(pygame.image.load(path1), (30, 36))
    chose2 = pygame.transform.scale(pygame.image.load(path2), (30, 36))
    
    return img_start, chose1, chose2