import pygame

class SimpleBlock(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.origin_pos = pos
        self.image = pygame.Surface((size, size)).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
    
    def recovery_pos(self):
        if self.rect.x < self.origin_pos[0]:
            rec_pos = self.origin_pos[0] - self.rect.x
            self.rect.x += rec_pos
        elif self.rect.x > self.origin_pos[0]:
            rec_pos = self.rect.x - self.origin_pos[0]
            self.rect.x -= rec_pos

    def update(self, shift):
        self.rect.x += shift

class Block(SimpleBlock):
    def __init__(self, pos, size, entity):
        super().__init__(pos, size)
        self.image = pygame.transform.scale(pygame.image.load(entity), (size, size))

class Diamond(Block):
    def __init__(self, pos, size, entity, type):
        super().__init__(pos, size, entity)
        self.type = type
        
class Coin(SimpleBlock):
    def __init__(self, pos, size, type):
        super().__init__(pos, size)
        self.animation_list = [
            pygame.transform.scale(pygame.image.load("./assets/block/Tiles/coin/tile_0151.png"), (size, size)),
            pygame.transform.scale(pygame.image.load("./assets/block/Tiles/coin/tile_0152.png"), (size, size))
        ]
        self.type = type
        self.index = 0
        self.image = self.animation_list[self.index]

    def animation(self):
        self.index += 0.05
        if self.index >= len(self.animation_list):
            self.index = 0
        self.image = self.animation_list[int(self.index)]
    
    def update(self, shift):
        self.animation()
        self.rect.x += shift

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("./assets/plane/bullet.png")
        self.rect = self.image.get_rect(center=pos)
    
    def update(self):
        self.rect.x += 15