import pygame

from pygame.sprite import Sprite

from random import randint


class Alien(Sprite):
    """Класс, представляющий одного пришельца"""

    def __init__(self, screen, settings, rocket):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.rocket = rocket
        self.image = pygame.image.load('image/pixil-frame-1.png')
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, 1800)
        self.rect.y = randint(0, 1000)

    def update(self):
        """Искусственный интеллект пришельца"""
        if self.rect.x < self.rocket.rect.x:
            self.rect.x += 1
        else:
            self.rect.x -= 1
        if self.rect.y < self.rocket.rect.y:
            self.rect.y += 1
        else:
            self.rect.y -= 1
