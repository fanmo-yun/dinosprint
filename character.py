import pygame
from img_process import load_img

class Dino_player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.animations = {'idle':[], 'walk':[], 'hurt':[], 'jump':[], 'down': []}
        self.animations_flip = {'idle':[], 'walk':[], 'hurt':[], 'jump':[], 'down': []}
        self.health_icon = pygame.transform.scale(pygame.image.load("./assets/block/Tiles/health/tile_0044.png"), (36,36))
        self.coin_icon = pygame.transform.scale(pygame.image.load("./assets/block/Tiles/coin/tile_0151.png"), (36,36))
        self.jump_sound = pygame.mixer.Sound("./assets/sound/jump.mp3")
        self.load_sprites()
        
        self.speed = 6
        self.health = 100
        self.fall_down = 0.8
        self.animation_index = 0
        self.animation_speed = 0.10
        self.jump_speed = 15
        self.animation_status = 'idle'
        self.move_val = pygame.Vector2(0, 0)
        
        self.ishurt = False
        self.Lshift = False
        self.on_ground = False
        self.facing_right = True
        
        self.image = self.animations['idle'][0]
        self.rect = self.image.get_rect(topleft = pos)
        
    def load_sprites(self):
        path = "./assets/character/sprites/"
        for keys in self.animations.keys():
            new_path = path + keys
            self.animations[keys] = load_img(new_path, False, (30, 36))
        
        for keys in self.animations_flip.keys():
            new_path = path + keys
            self.animations_flip[keys] = load_img(new_path, True, (30, 36))
            
    def sprites_animation(self):
        if self.facing_right:
            now_animations = self.animations[self.animation_status]
            
            self.animation_index += self.animation_speed
            if self.animation_index >= len(now_animations):
                self.animation_index = 0
            self.image = now_animations[int(self.animation_index)]
        else:
            now_animations = self.animations_flip[self.animation_status]
            
            self.animation_index += self.animation_speed
            if self.animation_index >= len(now_animations):
                self.animation_index = 0
            self.image = now_animations[int(self.animation_index)]
    
    def get_now_status(self):
        if self.ishurt == False:
            if self.move_val.y < 0:
                self.animation_status = 'jump'
            elif self.move_val.y > 1:
                self.animation_status = 'down'
            elif self.move_val.x != 0 and self.Lshift == False:
                self.animation_status = 'walk'
                self.animation_speed = 0.10
            elif self.move_val.x != 0 and self.Lshift:
                self.animation_status = 'walk'
                self.animation_speed = 0.20
            else:
                self.animation_status = 'idle'
                self.animation_speed = 0.10
        else:
            self.animation_status = 'hurt'
    
    def get_move(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LSHIFT] and keys[pygame.K_a]:
            self.move_val.x = -2
            self.Lshift = True
            self.facing_right = False
        elif keys[pygame.K_LSHIFT] and keys[pygame.K_d]:
            self.move_val.x = 2
            self.Lshift = True
            self.facing_right = True
        elif keys[pygame.K_a]:
            self.move_val.x = -1
            self.Lshift = False
            self.facing_right = False
        elif keys[pygame.K_d]:
            self.move_val.x = 1
            self.Lshift = False
            self.facing_right = True
        else:
            self.move_val.x = 0
            self.Lshift = False
        
        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump_sound.play()
            self.move_val.y = -self.jump_speed
    
    def update_health(self, screen):
        screen.blit(self.health_icon, (12, 12))
        screen.blit(pygame.font.Font("./assets/font/fonts/ttf/JetBrainsMono-Bold.ttf", 30).render(str(self.health), True, (0,0,0)), (50, 11))
    
    def update_icon(self, screen, number):
        screen.blit(self.coin_icon, (12, 45))
        screen.blit(pygame.font.Font("./assets/font/fonts/ttf/JetBrainsMono-Bold.ttf", 30).render(str(number), True, (0,0,0)), (50, 45))
    
    def falling_down(self):
        self.move_val.y += self.fall_down
        self.rect.y += self.move_val.y
        
class Plane(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.click = True
        self.fall_down = 0.8
        self.small_jump = -14
        self.big_jump = -18
        self.move_val = pygame.Vector2(0, 0)
        self.image = pygame.transform.scale(pygame.image.load("./assets/plane/blueplane.png"), (74, 59))
        self.coin_icon = pygame.transform.scale(pygame.image.load("./assets/block/Tiles/coin/tile_0151.png"), (36,36))
        self.rect = self.image.get_rect(topleft = pos)
    
    def update_icon(self, screen, number):
        screen.blit(self.coin_icon, (12, 45))
        screen.blit(pygame.font.Font("./assets/font/fonts/ttf/JetBrainsMono-Bold.ttf", 30).render(str(number), True, (0,0,0)), (50, 45))
    
    def falling_down(self):
        self.move_val.y += self.fall_down
        self.rect.y += self.move_val.y
    
    def update(self):
        self.falling_down()