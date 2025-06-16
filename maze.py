import pygame
import random
from constants import *

class Maze:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.wall_color = BLACK
        self.path_color = WHITE
        self.maze = self.generate_maze(width, height)
        self.wall_image = pygame.image.load("images\\wall.png")  # 加载墙壁图片
        self.wall_image = pygame.transform.scale(self.wall_image, (self.cell_size, self.cell_size))  # 缩放图片
        self.exit_image = pygame.image.load("images\\portal.png")  # 加载出口图片
        self.exit_image = pygame.transform.scale(self.exit_image, (self.cell_size, self.cell_size))  # 缩放图片
        self.first = False
    def generate_maze(self, width, height):
        # 使用DFS随机生成迷宫
        maze = [[1 for _ in range(width)] for _ in range(height)]  # 初始化迷宫，全部为墙壁

        def dfs(x, y):
            maze[y][x] = 0  # 打通当前单元格
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            random.shuffle(directions)  # 随机打乱方向

            for dx, dy in directions:
                nx, ny = x + dx * 2, y + dy * 2  # 下一个单元格
                if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                    maze[y + dy][x + dx] = 0  # 打通中间的墙
                    dfs(nx, ny)
        dfs(1, 1)  # 从起点开始生成
        maze[1][1] = 0  # 起点
        maze[height - 2][width - 2] = 0  # 终点
        return maze

    def draw(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                if self.maze[y][x] == 1:
                    screen.blit(self.wall_image, rect.topleft)  # 使用墙壁图片绘制
                    if(self.first==False):
                       pygame.display.flip()
                       pygame.time.wait(10)
                elif (x, y) == (self.width - 2, self.height - 2):  # 绘制出口图片
                    screen.blit(self.exit_image, rect.topleft)
                else:
                    pygame.draw.rect(screen, self.path_color, rect)

        self.first=True

    def judge(self,x,y):
        return self.maze[x][y]==1