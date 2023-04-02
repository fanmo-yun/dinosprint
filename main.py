import pygame, sys
from game import Game
from setting import *

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("DinoSprint")
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

game = Game(screen)

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    
    game.run_game()
    pygame.display.update()