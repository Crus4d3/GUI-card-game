import pygame
import os

class Assets():
    def __init__(self):
        self.BGImage = pygame.image.load(os.path.join("assets", "BGImage.png"))
