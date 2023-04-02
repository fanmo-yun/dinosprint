import pygame
from character import Dino_player
from setting import screen_height, screen_width
from data_process import create_ground_block, create_other_block
from img_process import load_background_img
from data_process import csv_parser

class Level:
    def __init__(self, screen, data):
        self.screen = screen
        self.separatrix1 = 2
        self.separatrix2 = 8
        self.hurt_sound = pygame.mixer.Sound("./assets/sound/hurt.mp3")
        self.background = load_background_img()
        self.scroll_area = 200
        self.offsetx = 0
        self.score = 0
        self.dead = 0
        
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Dino_player((100, 400)))
        
        self.ground_sprites = create_ground_block(csv_parser(data["ground"]))

        self.ground_front_sprites = create_ground_block(csv_parser(data["ground_front"]))

        self.grass_sprites = create_other_block(csv_parser(data["grass"]), "grass")

        self.sign_sprites = create_other_block(csv_parser(data["sign"]), "sign")

        self.water_sprites = create_other_block(csv_parser(data["water"]), "water")

        self.flag_sprites = create_other_block(csv_parser(data["flag"]), "flag")

        self.crate_sprites = create_other_block(csv_parser(data["crate"]), "crate")

        self.cloud_sprites = create_other_block(csv_parser(data["cloud"]), "cloud")

        self.stab_sprites = create_other_block(csv_parser(data["stab"]), "stab")

        self.barrier_sprites = create_other_block(csv_parser(data["barrier"]), "barrier")

        self.coin_sprites = create_other_block(csv_parser(data["coin"]), "coin")
    
    def scroll_screen(self):
        player = self.player.sprite

        if player.rect.centerx <= screen_width / 3 and player.move_val.x < 0 and player.Lshift == False:
            self.offsetx = 6
            player.speed = 0
        elif player.rect.centerx <= screen_width / 3 and player.move_val.x < 0 and player.Lshift:
            self.offsetx = 12
            player.speed = 0
        elif player.rect.centerx >= screen_width - (screen_width / 3) and player.move_val.x > 0 and player.Lshift == False:
            self.offsetx = -6
            player.speed = 0
        elif player.rect.centerx >= screen_width - (screen_width / 3) and player.move_val.x > 0 and player.Lshift:
            self.offsetx = -12
            player.speed = 0
        else:
            self.offsetx = 0
            player.speed = 6
    
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

    def collisionx(self):
        player = self.player.sprite
        player.rect.x += player.move_val.x * player.speed
        
        for block_sprites in self.ground_sprites.sprites() + self.crate_sprites.sprites() + self.barrier_sprites.sprites():
            if block_sprites.rect.colliderect(player.rect):
                if player.move_val.x < 0:
                    player.rect.left = block_sprites.rect.right
                elif player.move_val.x > 0:
                    player.rect.right = block_sprites.rect.left
    
    def collisiony(self):
        player = self.player.sprite
        player.falling_down()
        
        for block_sprites in self.ground_sprites.sprites() + self.crate_sprites.sprites():
            if block_sprites.rect.colliderect(player.rect):
                if player.move_val.y > 0:
                    player.rect.bottom = block_sprites.rect.top
                    player.move_val.y = 0
                    player.on_ground = True
                    player.ishurt = False
                elif player.move_val.y < 0:
                    player.rect.top = block_sprites.rect.bottom
                    player.move_val.y = 0
        
        if player.on_ground and player.move_val.y < 0 or player.move_val.y > 1:
            player.on_ground = False

    def dead_or_win(self, restart_game, continue_game):
        player = self.player.sprite
        for sprites in self.water_sprites.sprites() + self.stab_sprites.sprites():
            if sprites.rect.colliderect(player.rect):
                self.hurt_sound.play()
                player.health -= 1
                player.move_val.y = -10
                player.ishurt = True
                break
        
        for sprites in self.flag_sprites.sprites():
            if sprites.rect.colliderect(player.rect):
                self.remove_all()
                continue_game()
                break
                
        if player.health <= 0 or player.rect.y > screen_height:
            self.dead += 1
            self.hurt_sound.play()
            restart_game()
            self.recovery_block()
            player.rect.topleft = (100, 400)
            player.health = 100
    
    def get_score(self):
        player = self.player.sprite
        
        for coin in self.coin_sprites.sprites():
            if coin.rect.colliderect(player.rect):
                self.score += coin.type
                self.coin_sprites.remove(coin)

    def recovery_block(self):
        all_sprites = self.cloud_sprites.sprites() + \
        self.crate_sprites.sprites() + \
        self.flag_sprites.sprites() + \
        self.grass_sprites.sprites() + \
        self.ground_front_sprites.sprites() + \
        self.ground_sprites.sprites() + \
        self.sign_sprites.sprites() + \
        self.stab_sprites.sprites() + \
        self.water_sprites.sprites() + \
        self.coin_sprites.sprites() + \
        self.barrier_sprites.sprites()
        
        for sprite in all_sprites:
            sprite.recovery_pos()

    def remove_all(self):
        self.player.empty()
        
        self.flag_sprites.empty()
        self.cloud_sprites.empty()
        self.crate_sprites.empty()
        self.grass_sprites.empty()
        self.ground_front_sprites.empty()
        self.ground_sprites.empty()
        self.sign_sprites.empty()
        self.stab_sprites.empty()
        self.water_sprites.empty()
        self.coin_sprites.empty()
        self.barrier_sprites.empty()

    def run(self, restart_level, continue_level):
        self.barrier_sprites.update(self.offsetx)
        self.barrier_sprites.draw(self.screen)
        
        self.background_draw()
        
        self.ground_sprites.update(self.offsetx)
        self.ground_sprites.draw(self.screen)
        
        self.ground_front_sprites.update(self.offsetx)
        self.ground_front_sprites.draw(self.screen)
                
        self.grass_sprites.update(self.offsetx)
        self.grass_sprites.draw(self.screen)
        
        self.water_sprites.update(self.offsetx)
        self.water_sprites.draw(self.screen)

        self.coin_sprites.update(self.offsetx)
        self.coin_sprites.draw(self.screen)
        self.get_score()
        
        self.stab_sprites.update(self.offsetx)
        self.stab_sprites.draw(self.screen)
        
        self.sign_sprites.update(self.offsetx)
        self.sign_sprites.draw(self.screen)
        
        self.flag_sprites.update(self.offsetx)
        self.flag_sprites.draw(self.screen)
        
        self.crate_sprites.update(self.offsetx)
        self.crate_sprites.draw(self.screen)
        
        self.cloud_sprites.update(self.offsetx)
        self.cloud_sprites.draw(self.screen)
        
        self.player.sprite.get_move()
        self.player.sprite.get_now_status()
        self.player.sprite.sprites_animation()
        self.scroll_screen()
        self.collisionx()
        self.collisiony()
        self.player.sprite.update_health(self.screen)
        self.player.sprite.update_icon(self.screen, self.score)
        self.dead_or_win(restart_level, continue_level)
        self.player.draw(self.screen)

class Level3(Level):
    def __init__(self, screen, data):
        super().__init__(screen, data)
        self.tree_sprites = create_other_block(csv_parser(data["tree"]), "tree")
    
    def remove_all(self):
        self.tree_sprites.empty()
        return super().remove_all()

    def recovery_block(self):
        all_sprites = self.cloud_sprites.sprites() + \
        self.crate_sprites.sprites() + \
        self.flag_sprites.sprites() + \
        self.grass_sprites.sprites() + \
        self.ground_front_sprites.sprites() + \
        self.ground_sprites.sprites() + \
        self.sign_sprites.sprites() + \
        self.stab_sprites.sprites() + \
        self.water_sprites.sprites() + \
        self.coin_sprites.sprites() + \
        self.barrier_sprites.sprites() + \
        self.tree_sprites.sprites()
        
        for sprite in all_sprites:
            sprite.recovery_pos()
    
    def run(self, restart_level, continue_level):
        self.barrier_sprites.update(self.offsetx)
        self.barrier_sprites.draw(self.screen)
        
        self.background_draw()
        
        self.ground_sprites.update(self.offsetx)
        self.ground_sprites.draw(self.screen)
        
        self.ground_front_sprites.update(self.offsetx)
        self.ground_front_sprites.draw(self.screen)
                
        self.grass_sprites.update(self.offsetx)
        self.grass_sprites.draw(self.screen)
        
        self.water_sprites.update(self.offsetx)
        self.water_sprites.draw(self.screen)

        self.coin_sprites.update(self.offsetx)
        self.coin_sprites.draw(self.screen)
        self.get_score()
        
        self.stab_sprites.update(self.offsetx)
        self.stab_sprites.draw(self.screen)
        
        self.sign_sprites.update(self.offsetx)
        self.sign_sprites.draw(self.screen)
        
        self.flag_sprites.update(self.offsetx)
        self.flag_sprites.draw(self.screen)
        
        self.crate_sprites.update(self.offsetx)
        self.crate_sprites.draw(self.screen)
        
        self.cloud_sprites.update(self.offsetx)
        self.cloud_sprites.draw(self.screen)
        
        self.tree_sprites.update(self.offsetx)
        self.tree_sprites.draw(self.screen)
        
        self.player.sprite.get_move()
        self.player.sprite.get_now_status()
        self.player.sprite.sprites_animation()
        self.scroll_screen()
        self.collisionx()
        self.collisiony()
        self.player.sprite.update_health(self.screen)
        self.player.sprite.update_icon(self.screen, self.score)
        self.dead_or_win(restart_level, continue_level)
        self.player.draw(self.screen)