import pygame, random
from block import Coin
from img_process import load_img

class Enemy(pygame.sprite.Sprite):
    def __init__(self, path, pos):
        super().__init__()
        self.index = 0
        self.speed = random.randint(6, 10)
        self.animation_list = load_img(path, False, (48, 48))
        self.image = self.animation_list[self.index]
        self.rect = self.image.get_rect(topleft=pos)
    
    def animation(self):
        self.index += 0.10
        if self.index >= len(self.animation_list):
            self.index = 0
        self.image = self.animation_list[int(self.index)]
    
    def update(self):
        self.animation()
        self.rect.x -= self.speed

class Fly_coin(Coin):
    def __init__(self, pos, size, type):
        super().__init__(pos, size, type)
    
    def update(self):
        self.animation()
        self.rect.x -= 22