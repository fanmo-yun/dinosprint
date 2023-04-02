import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, size, pos, color, font, text):
        super().__init__()
        self.color = color
        self.f = font.render(text, True, (0, 0, 0))
        self.image = pygame.Surface(size)
        self.image.fill(self.color)
        self.image.blit(self.f, self.f.get_rect(center=(size[0]/2, size[1]/2)))
        self.rect = self.image.get_rect(topleft=pos)

class Level_block(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill((0, 191, 255))
        self.rect = self.image.get_rect(center=pos)

class Chose_icon(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("./assets/character/sprites/head/Dinohead.png").convert_alpha(), (45, 24))
        self.rect = self.image.get_rect(center=pos)
    
    def update(self, pos):
        self.rect = self.image.get_rect(center=pos)