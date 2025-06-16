import pygame
from constants import *
from maze import Maze
from player import Player
from enemy import Enemy

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(FONT_PATH, 36)
        self.clock = pygame.time.Clock()  # 添加时钟，用于控制帧率

        # 迷宫参数
        self.maze_width = 35
        self.maze_height = 768 * 35 // 1280
        self.cell_size = SCREEN_WIDTH / self.maze_width  # 每个迷宫单元的大小

        # 创建迷宫对象
        self.maze = Maze(self.maze_width, self.maze_height, self.cell_size)

        # 创建玩家对象
        self.player = Player(1, 1, self.cell_size, self.maze.maze)
        
        # 创建敌人对象
        self.enemy1 = Enemy(33, 1, self.cell_size, self.maze.maze)
        self.enemy2 = Enemy(1, 19, self.cell_size, self.maze.maze)

        # 定义出口位置
        self.exit_x, self.exit_y = self.maze_width - 2, self.maze_height - 2

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:  # 检测是否按下了 ESC 键
            self.player.x, self.player.y = 1, 1
            return "menu"

        self.player.update(keys)
        self.enemy1.update(self.player.x,self.player.y)
        self.enemy2.update(self.player.x,self.player.y)

        # 检查是否到达出口
        if int(self.player.x) == self.exit_x and int(self.player.y) == self.exit_y:
            font = pygame.font.Font(FONT_PATH, 74)
            text = font.render('You Win!', True, GREEN)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(3000)
            self.player.x, self.player.y = 1, 1
            return "menu"
        
        # 检查是否碰到敌人
        if int(self.player.x) == int(self.enemy1.x) and int(self.player.y) == int(self.enemy1.y):
            font = pygame.font.Font(FONT_PATH, 74)
            text = font.render('You Lose!', True, RED)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(3000)
            self.player.x, self.player.y = 1, 1
            return "menu"
        
        if int(self.player.x) == int(self.enemy2.x) and int(self.player.y) == int(self.enemy2.y):
            font = pygame.font.Font(FONT_PATH, 74)
            text = font.render('You Lose!', True, RED)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(3000)
            self.player.x, self.player.y = 1, 1
            return "menu"
        
        return "game"

    def draw(self):
        self.screen.fill(WHITE)

        # 绘制迷宫
        self.maze.draw(self.screen)

        # 绘制玩家
        self.player.draw(self.screen)
        self.enemy1.draw(self.screen)
        self.enemy2.draw(self.screen)

        # 绘制提示信息
        prompt_text = self.font.render("按ESC可退出本局", True, WHITE)
        prompt_rect = prompt_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 15))
        self.screen.blit(prompt_text, prompt_rect)

        # 更新屏幕
        pygame.display.flip()
        self.clock.tick(60)  # 控制帧率为 60 FPS