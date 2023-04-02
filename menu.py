import pygame, sys
from ui import Button, Level_block, Chose_icon
from data import rainbow_rgb, levels_pos
from setting import screen_height, screen_width
from img_process import load_background_img, load_start_menu_cha

class Start_Menu:
    def __init__(self, screen):
        self.Button_create()
        self.background = load_background_img()
        self.title_dino, self.chose1, self.chose2 = load_start_menu_cha()
        
        self.screen = screen
        self.rainbow_index = 0
        self.separatrix = 6
        self.isstart = False
        self.index = 0
    
    def game_title(self):
        self.rainbow_index += 0.08
        if self.rainbow_index >= len(rainbow_rgb):
            self.rainbow_index = 0
        self.text = pygame.font.Font("./assets/font/fonts/ttf/JetBrainsMono-Bold.ttf", 40) \
                .render("DinoSprint", True, rainbow_rgb[int(self.rainbow_index)])
        self.made_by = pygame.font.Font("./assets/font/fonts/ttf/JetBrainsMono-Bold.ttf", 20) \
                .render("Powered by pygame", True, (255,255,255))

    def Button_create(self):
        self.button = pygame.sprite.Group()
        self.button.add(
            Button((105, 35), (574, 330), (0,255,0), pygame.font.Font("./assets/font/fonts/ttf/JetBrainsMono-Bold.ttf", 20), "start"), 
            Button((105, 35), (574, 390), (0,255,0), pygame.font.Font("./assets/font/fonts/ttf/JetBrainsMono-Bold.ttf", 20), "exit")
        )
    
    def mouse_click(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        
        if self.button.sprites()[0].rect.collidepoint(mouse_pos[0], mouse_pos[1]):
            self.screen.blit(self.chose1, (520, 330))
            if mouse_click[0]:
                self.isstart = True
        
        if self.button.sprites()[1].rect.collidepoint(mouse_pos[0], mouse_pos[1]):
            self.screen.blit(self.chose2, (520, 390))
            if mouse_click[0]:
                sys.exit(0)
                    
    def background_draw(self):
        for i in range(0, int(screen_width / 48)):
            for j in range(0, int(screen_height / 48)):
                if j < self.separatrix:
                    self.screen.blit(self.background[1], (i * 48, j * 48))
                elif j == self.separatrix:
                    self.screen.blit(self.background[2], (i * 48, j * 48))
                else:
                    self.screen.blit(self.background[3], (i * 48, j * 48))
    
    def title_dino_draw(self):
        self.index += 0.15
        if self.index >= len(self.title_dino):
            self.index = 0
        self.screen.blit(self.title_dino[int(self.index)], (609, 230))
    
    def run(self):
        self.game_title()
        self.background_draw()
        self.screen.blit(self.text, (507, 150))
        self.screen.blit(self.made_by, (10, screen_height - 30))
        self.title_dino_draw()
        self.button.draw(self.screen)
        self.mouse_click()

class Chose_Menu:
    def __init__(self, screen):
        self.screen = screen
        self.now_level = 0
        self.dead_count = 0
        self.separatrix1 = 0
        self.separatrix2 = 11
        self.win = False
        self.isstart = False
        self.get_time = True
        self.cooldown = 500
        
        self.set_icon()
        self.create_text()
        self.set_level_block()
        self.background = load_background_img()
        
    def set_level_block(self):
        self.level_block = pygame.sprite.Group()
        for level in levels_pos:
            self.level_block.add(Level_block(level, (180, 100)))
            
    def set_icon(self):
        self.icon = pygame.sprite.GroupSingle()
        self.icon.add(Chose_icon(levels_pos[self.now_level]))
    
    def background_draw(self):
        for i in range(0, int(screen_width / 48)):
            for j in range(0, int(screen_height / 48)):
                if j == self.separatrix1:
                    self.screen.blit(self.background[0], (i * 48, j * 48))
                elif j > self.separatrix1 and j < self.separatrix2:
                    self.screen.blit(self.background[1], (i * 48, j * 48))
                elif j == self.separatrix2:
                    self.screen.blit(self.background[2], (i * 48, j * 48))
                else:
                    self.screen.blit(self.background[3], (i * 48, j * 48))
    
    def lines_draw(self):
        lines_path = []
        for level in levels_pos:
            lines_path.append(level)
        pygame.draw.lines(self.screen, (255,165,0), False, lines_path, 6)
    
    def create_text(self):
        self.texts = pygame.font.Font("./assets/font/fonts/ttf/JetBrainsMono-BoldItalic.ttf", 50).render("LEVELS", True, (0,0,0))
        self.texts_rect = self.texts.get_rect(center=(screen_width / 2, screen_height - 650))
    
    def start_game(self):
        if self.get_time:
            self.last = pygame.time.get_ticks()
            self.get_time = False
            
        now = pygame.time.get_ticks()
        if now - self.last >= self.cooldown and self.isstart == False:
            self.last = now
            self.isstart = True

    def restart_game(self):
        self.isstart = False
        self.get_time = True
        self.dead_counts()
        self.start_game()
    
    def dead_counts(self):
        self.dead_count += 1
        
    def continue_level(self):
        self.isstart = False
        self.get_time = True
        self.now_level += 1
        self.start_game()
    
    def change_win(self):
        self.win = True
                        
    def run(self):
        self.background_draw()
        self.screen.blit(self.texts, self.texts_rect)
        self.lines_draw()
        self.level_block.draw(self.screen)
        self.icon.draw(self.screen)
        self.icon.update(levels_pos[self.now_level])
        self.start_game()
    
class Win_menu:
    def __init__(self, screen):
        self.screen = screen
        self.iscount = True
        self.separatrix1 = 0
        self.separatrix2 = 11
        self.sum_dead = 0
        self.sum_score = 0
        self.background = load_background_img()
        self.create_text()
    
    def background_draw(self):
        for i in range(0, int(screen_width / 48)):
            for j in range(0, int(screen_height / 48)):
                if j == self.separatrix1:
                    self.screen.blit(self.background[0], (i * 48, j * 48))
                elif j > self.separatrix1 and j < self.separatrix2:
                    self.screen.blit(self.background[1], (i * 48, j * 48))
                elif j == self.separatrix2:
                    self.screen.blit(self.background[2], (i * 48, j * 48))
                else:
                    self.screen.blit(self.background[3], (i * 48, j * 48))
    
    def create_text(self):
        self.text1 = pygame.font.Font("./assets/font/fonts/ttf/JetBrainsMono-BoldItalic.ttf", 40).render("Thanks for playing", True, (0,0,0))
        self.text1_rect = self.text1.get_rect(center=(screen_width/2, screen_height/2 - 200))

    def sum_mun(self, dead_count, all_score):
        if self.iscount:
            for count in dead_count:
                self.sum_dead += count
            for count in all_score:
                self.sum_score += count
            self.iscount = False

    def run(self, dead_count, all_score):
        self.background_draw()
        self.screen.blit(self.text1, self.text1_rect)
        self.sum_mun(dead_count, all_score)
        self.screen.blit(pygame.font.Font("./assets/font/fonts/ttf/JetBrainsMono-Bold.ttf", 20).render(f"Dead_count: {self.sum_dead}", True, (0,0,0)), (screen_width/2 - 90, screen_height/2 - 100))
        self.screen.blit(pygame.font.Font("./assets/font/fonts/ttf/JetBrainsMono-Bold.ttf", 20).render(f"Score: {self.sum_score}", True, (0,0,0)), (screen_width/2 - 90, screen_height/2 - 50))
