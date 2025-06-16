import pygame
from button import Button
from constants import *
from video_loader import VideoLoader

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(FONT_PATH, 36)
        self.title_font = pygame.font.Font(FONT_PATH, 52)
        self.start_button = Button("开始游戏", SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2, 200, 50, GRAY, GREEN)
        self.exit_button = Button("退出游戏", SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 + 80, 200, 50, GRAY, GREEN)
        self.video_loader = VideoLoader("videos\\menu_picture.mp4")

    def handle_events(self, events):
        for event in events:
            if self.start_button.is_clicked(event):
                return "game"
            elif self.exit_button.is_clicked(event):
                return "exit"
        return "menu"

    def draw(self):
        frame_surface = self.video_loader.get_frame(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen.blit(frame_surface, (0, 0))

        title_text = self.title_font.render("欢迎来玩迷宫游戏", True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(title_text, title_rect)

        self.start_button.draw(self.screen, self.font)
        self.exit_button.draw(self.screen, self.font)