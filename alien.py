import pygame

from pygame.sprite import Sprite

import random


class Alien(Sprite):
    """Класс, представляющий одного пришельца"""

    def __init__(self, screen, settings, rocket):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.rocket = rocket
        self.image = pygame.image.load('image/pixil-frame-1.png')
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.spawn_alien()

    def spawn_alien(self):
        """Появление пришельцев"""
        self.one = random.randint(1000, 1800)
        self.two = random.randint(0, 1800)
        self.one1 = random.randint(500, 1000)
        self.two1 = random.randint(0, 1800)
        self.list = [self.one, self.two]
        self.list1 = [self.one1, self.two1]
        self.rect.x = random.choice(self.list)
        self.rect.y = random.choice(self.list1)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Искусственный интеллект пришельца"""
        if self.x < self.rocket.x:
            self.x += float(self.settings.alien_speed)
        else:
            self.x -= float(self.settings.alien_speed)
        if self.y < self.rocket.rect.y:
            self.y += float(self.settings.alien_speed)
        else:
            self.y -= float(self.settings.alien_speed)
        self.rect.x = self.x
        self.rect.y = self.y
