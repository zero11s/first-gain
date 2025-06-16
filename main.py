import pygame
import sys
from constants import *
from menu import Menu
from game import Game

# 初始化 Pygame
pygame.init()
pygame.display.set_caption("Maze Game")

# 创建菜单和游戏对象
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
menu = Menu(screen)
game = Game(screen)

# 游戏状态
game_state = "menu"

# 游戏主循环
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    if game_state == "menu":
        game_state = menu.handle_events(events)
        menu.draw()
    elif game_state == "game":
        game_state = game.update()
        game.draw()
    elif game_state == "exit":
        running = False

    pygame.display.flip()

pygame.quit()
sys.exit()