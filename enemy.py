import pygame
from collections import deque
from constants import *

class Enemy:
    def __init__(self, x, y, cell_size, maze):
        self.x = x
        self.y = y
        self.cell_size = cell_size
        self.image = pygame.image.load("images\\enemy.png")  # 加载敌人图片
        self.image = pygame.transform.scale(self.image, (cell_size, cell_size))  # 缩放图片
        self.rect = self.image.get_rect(topleft=(self.x * cell_size, self.y * cell_size))
        self.maze = maze
        self.move_delay = 0  # 移动延迟计数

    def update(self, player_x, player_y):
        # 添加移动延迟，减少移动频率
        if self.move_delay > 0:
            self.move_delay -= 1
            return

        # 使用BFS找到玩家位置
        path = self.bfs((int(self.x), int(self.y)), (int(player_x), int(player_y)))
        if path:
            next_pos = path[1] if len(path) > 1 else path[0]
            self.x, self.y = next_pos

        # 更新敌人矩形位置
        self.rect.topleft = (self.x * self.cell_size, self.y * self.cell_size)

        # 设置移动延迟，减少移动频率
        self.move_delay = 100  # 调整这个值可以改变移动频率

    def bfs(self, start, end):
        queue = deque([start])
        visited = {start: None}

        while queue:
            current = queue.popleft()
            if current == end:
                break

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                neighbor = (current[0] + dx, current[1] + dy)
                if 0 <= neighbor[0] < len(self.maze[0]) and 0 <= neighbor[1] < len(self.maze):
                    if self.maze[neighbor[1]][neighbor[0]] == 0 and neighbor not in visited:
                        queue.append(neighbor)
                        visited[neighbor] = current

        # 重建路径
        path = []
        current = end
        while current != start:
            path.append(current)
            current = visited.get(current)
            if current is None:
                break
        path.reverse()
        return path

    def draw(self, screen):
        screen.blit(self.image, self.rect)