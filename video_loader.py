from moviepy import VideoFileClip
import pygame
import numpy as np

class VideoLoader:
    def __init__(self, video_path):
        self.video = VideoFileClip(video_path)
        self.video_frame = 0

    def get_frame(self, screen_width, screen_height):
        frame = self.video.get_frame(self.video_frame)
        self.video_frame += 0.2 / self.video.fps
        if self.video_frame >= self.video.duration:
            self.video_frame = 0
        frame = np.rot90(frame, 1)
        frame_surface = pygame.surfarray.make_surface(frame)
        frame_surface = pygame.transform.scale(frame_surface, (screen_width, screen_height))
        return frame_surface