from menu import *
from level import *
from level_leisure import *
from data import level_1, level_3
from character import *

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.start_menu = Start_Menu(screen)
        self.chose_menu = Chose_Menu(screen)
        self.win_menu = Win_menu(screen)
        self.level1 = Level(screen, level_1)
        self.level2 = Level2(screen)
        self.level3 = Level3(screen, level_3)
        self.level4 = Level4(screen)
    
    def run_game(self):
        if self.start_menu.isstart == False:
            self.start_menu.run()
        elif self.start_menu.isstart and self.chose_menu.isstart == False:
            self.chose_menu.run()
        elif self.chose_menu.win:
            self.win_menu.run(
                [self.level1.dead, self.level2.dead, self.level3.dead, self.level4.dead],
                [self.level1.score, self.level2.score, self.level3.score, self.level4.score]
            )
        elif self.chose_menu.now_level == 0 and self.chose_menu.isstart:
            self.level1.run(self.chose_menu.restart_game, self.chose_menu.continue_level)
        elif self.chose_menu.now_level == 1 and self.chose_menu.isstart:
            self.level2.run(self.chose_menu.restart_game, self.chose_menu.continue_level)
        elif self.chose_menu.now_level == 2 and self.chose_menu.isstart:
            self.level3.run(self.chose_menu.restart_game, self.chose_menu.continue_level)
        elif self.chose_menu.now_level == 3 and self.chose_menu.isstart:
            self.level4.run(self.chose_menu.restart_game, self.chose_menu.change_win)