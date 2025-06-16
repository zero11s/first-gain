import pygame
from constants import *

class Player:
    def __init__(self, x, y, cell_size, maze):
        self.x = x
        self.y = y
        self.cell_size = cell_size
        self.speed = self.cell_size * 0.2
        self.image = pygame.image.load("images\\player.png")  # 加载玩家图片
        self.image = pygame.transform.scale(self.image, (self.cell_size, self.cell_size))  # 缩放图片
        self.rect = self.image.get_rect(topleft=(self.x * self.cell_size, self.y * self.cell_size))
        self.maze = maze

    def update(self, keys):
        maze_height = len(self.maze)
        maze_width = len(self.maze[0])

        if keys[pygame.K_UP] and self.y > 0 and self.maze[int(self.y - self.speed / self.cell_size)][int(self.x)] == 0:
            self.y -= self.speed / self.cell_size
        if keys[pygame.K_DOWN] and self.y < maze_height - 1 and self.maze[int(self.y + self.speed / self.cell_size)][int(self.x)] == 0:
            self.y += self.speed / self.cell_size
        if keys[pygame.K_LEFT] and self.x > 0 and self.maze[int(self.y)][int(self.x - self.speed / self.cell_size)] == 0:
            self.x -= self.speed / self.cell_size
        if keys[pygame.K_RIGHT] and self.x < maze_width - 1 and self.maze[int(self.y)][int(self.x + self.speed / self.cell_size)] == 0:
            self.x += self.speed / self.cell_size

        # 更新玩家矩形位置
        self.rect.topleft = (int(self.x) * self.cell_size, int(self.y) * self.cell_size)

    def draw(self, screen):
        screen.blit(self.image, self.rect)