import pygame, random
from img_process import load_background_img
from setting import screen_width ,screen_height, block_size
from block import Bullet
from character import Plane
from enemy import *

class Level2:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.dead = 0
        self.separatrix1 = 2
        self.separatrix2 = 8
        self.get_time = True
        self.iscontinue = False
        self.cooldown = 21000
        self.background = load_background_img()
        self.hurt_sound = pygame.mixer.Sound("./assets/sound/hurt.mp3")
        self.jump_sound = pygame.mixer.Sound("./assets/sound/jump.mp3")
        self.player = pygame.sprite.GroupSingle()
        self.enemys = pygame.sprite.Group()
        self.flycoins = pygame.sprite.GroupSingle()
        self.player.add(Plane((200, 300)))
        self.start_enemy()

    def start_enemy(self):
        self.enemys.empty()
        for _ in range(2):
            self.enemys.add(Enemy("./assets/block/Characters/bird", (screen_width, random.randint(10, screen_height - 10) )))
        self.flycoins.add(Fly_coin((screen_width, random.randint(30, screen_height - 30)), block_size, 1))
    
    def create_other_enemy(self):
        self.enemys.add(Enemy("./assets/block/Characters/bird", (screen_width, random.randint(10, screen_height - 10) )))

    def create_coin(self):
        self.flycoins.add(Fly_coin((screen_width, random.randint(30, screen_height - 30)), block_size, 1))

    def background_draw(self):
        for i in range(0, int(screen_width / 48)):
            for j in range(0, int(screen_height / 48)):
                if j < self.separatrix1:
                    self.screen.blit(self.background[4], (i * 48, j * 48))
                elif j == self.separatrix1:
                    self.screen.blit(self.background[0], (i * 48, j * 48))
                elif j > self.separatrix1 and j < self.separatrix2:
                    self.screen.blit(self.background[1], (i * 48, j * 48))
                elif j == self.separatrix2:
                    self.screen.blit(self.background[2], (i * 48, j * 48))
                else:
                    self.screen.blit(self.background[3], (i * 48, j * 48))
    
    def timer(self):
        if self.get_time:
            self.last = pygame.time.get_ticks()
            self.get_time = False
        
        self.now = pygame.time.get_ticks()
        if self.now - self.last >= self.cooldown and self.iscontinue == False:
            self.last = self.now
            self.iscontinue = True
    
    def win_or_dead(self, restart_game, continue_game):
        player = self.player.sprite
        
        player.update_icon(self.screen, self.score)
        
        if self.iscontinue:
            self.remove_all()
            continue_game()
        
        if player.rect.topleft[1] > screen_height or player.rect.bottomleft[1] < 0:
            self.dead += 1
            self.hurt_sound.play()
            self.restart_level(restart_game)
        
        for sprite in self.enemys.sprites():
            if sprite.rect.colliderect(player.rect):
                self.dead += 1
                self.hurt_sound.play()
                self.restart_level(restart_game)
                break
            elif sprite.rect.x <= 0:
                self.enemys.remove(sprite)
                self.create_other_enemy()
                break
        
        for sprite in self.flycoins.sprites():
            if sprite.rect.colliderect(player.rect):
                self.score += sprite.type
                self.flycoins.remove(sprite)
                self.create_coin()
                break
            elif sprite.rect.x <= 0:
                self.flycoins.remove(sprite)
                self.create_coin()
                break
    
    def player_move(self):
        player = self.player.sprite
        mouse = pygame.mouse.get_pressed()
        if mouse[0] and player.click:
            player.click = False
            player.move_val.y = player.small_jump
            self.jump_sound.play()
        elif mouse[2] and player.click:
            player.click = False
            player.move_val.y = player.big_jump
            self.jump_sound.play()
        
        if not(mouse[0] or mouse[2]) and player.click == False:
            player.click = True
            
    def text(self):
        time = (self.cooldown - (self.now - self.last)) / 1000
        self.screen.blit(pygame.font.Font("./assets/font/fonts/ttf/JetBrainsMono-Bold.ttf", 30).render(f"Hold for {int(time)} Sec", True, (0,0,0)), (20, 11))
    
    def restart_level(self, restart_game):
        player = self.player.sprite
        player.rect.topleft = (200, 300)
        player.move_val.y = 0
        self.score = 0
        restart_game()
        self.start_enemy()
        self.get_time = True
    
    def remove_all(self):
        self.enemys.empty()
        self.flycoins.empty()
        self.player.empty()
    
    def run(self, restart_level, continue_level):
        self.timer()
        self.background_draw()
        
        self.enemys.update()
        self.enemys.draw(self.screen)
        
        self.flycoins.update()
        self.flycoins.draw(self.screen)
        
        self.player_move()
        self.player.update()
        self.player.draw(self.screen)
        
        self.win_or_dead(restart_level, continue_level)
        self.text()

class Level4(Level2):
    def __init__(self, screen):
        super().__init__(screen)
        self.bullets = pygame.sprite.Group()
    
    def start_enemy(self):
        self.enemys.empty()
        for _ in range(25):
            self.enemys.add(Enemy("./assets/block/Characters/bird", (screen_width, random.randint(10, screen_height - 10) )))
        self.flycoins.add(Fly_coin((screen_width, random.randint(30, screen_height - 30)), block_size, 1))
    
    def collision(self):
        pygame.sprite.groupcollide(self.bullets, self.enemys, True, True)
        
        if len(self.enemys.sprites()) != 25:
            self.score += 1
            self.create_other_enemy()
        
        for bullet in self.bullets.sprites():
            if bullet.rect.x >= screen_width:
                self.bullets.remove(bullet)
    
    def remove_all(self):
        self.bullets.empty()
        self.enemys.empty()
        self.flycoins.empty()
        self.player.empty()
    
    def player_move(self):
        player = self.player.sprite
        
        mouse_pos = pygame.mouse.get_pos()
        player.rect.center = mouse_pos
        
        mouse_click = pygame.mouse.get_pressed()
        if mouse_click[0] and player.click and len(self.bullets.sprites()) < 3:
            self.bullets.add(Bullet(self.player.sprite.rect.center))
            player.click = False
        
        if not mouse_click[0] and player.click == False:
            player.click = True
    
    def win_or_dead(self, restart_game, win_game):
        player = self.player.sprite
        
        player.update_icon(self.screen, self.score)
        
        if self.iscontinue:
            self.remove_all()
            win_game()
        
        if player.rect.topleft[1] > screen_height or player.rect.bottomleft[1] < 0:
            self.dead += 1
            self.hurt_sound.play()
            self.restart_level(restart_game)
        
        for sprite in self.enemys.sprites():
            if sprite.rect.colliderect(player.rect):
                self.hurt_sound.play()
                self.dead += 1
                self.restart_level(restart_game)
                break
            elif sprite.rect.x <= 0:
                self.enemys.remove(sprite)
                self.create_other_enemy()
                break
        
        for sprite in self.flycoins.sprites():
            if sprite.rect.colliderect(player.rect):
                self.score += sprite.type
                self.flycoins.remove(sprite)
                self.create_coin()
                break
            elif sprite.rect.x <= 0:
                self.flycoins.remove(sprite)
                self.create_coin()
                break
    
    def run(self, restart_level, win):
        self.timer()
        self.background_draw()
        
        self.collision()
        self.enemys.update()
        self.enemys.draw(self.screen)
        
        self.flycoins.update()
        self.flycoins.draw(self.screen)
        
        self.bullets.update()
        self.bullets.draw(self.screen)
        
        self.player_move()
        self.player.draw(self.screen)
        
        self.win_or_dead(restart_level, win)
        self.text()