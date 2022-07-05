import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс для управления снарядами, выпущенными кораблем"""

    def __init__(self, screen, settings, rocket):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.rocket = rocket
        self.color = self.settings.bullets_color
        self.rect = pygame.Rect(0, 0, self.settings.bullets_width, self.settings.bullets_height)
        self.bullet_direction()

    def bullet_direction(self):
        if self.rocket.image == self.rocket.image_right:
            self.direction = "right"
            self.rect = pygame.Rect(0, 0, self.settings.bullets_height, self.settings.bullets_width)
            self.rect.midbottom = self.rocket.rect.midright
        elif self.rocket.image == self.rocket.image_left:
            self.direction = "left"
            self.rect = pygame.Rect(0, 0, self.settings.bullets_height, self.settings.bullets_width)
            self.rect.midbottom = self.rocket.rect.midleft
        elif self.rocket.image == self.rocket.image_up:
            self.direction = "up"
            self.rect = pygame.Rect(0, 0, self.settings.bullets_width, self.settings.bullets_height)
            self.rect.midbottom = self.rocket.rect.midtop
        elif self.rocket.image == self.rocket.image_down:
            self.direction = "down"
            self.rect = pygame.Rect(0, 0, self.settings.bullets_width, self.settings.bullets_height)
            self.rect.midbottom = self.rocket.rect.midbottom

    def update(self):
        """Перемещение снаряда"""
        if self.direction == 'right':
            self.rect.x += self.settings.rocket_speed
        if self.direction == 'left':
            self.rect.x -= self.settings.rocket_speed
        if self.direction == 'up':
            self.rect.y -= self.settings.rocket_speed
        if self.direction == 'down':
            self.rect.y += self.settings.rocket_speed

    def draw_bullet(self):
        """Рисует снаряд"""
        pygame.draw.rect(self.screen, self.color, self.rect)
