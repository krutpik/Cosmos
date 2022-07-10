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
        self.direction = ''
        self.bullet_direction()

    def bullet_direction(self):
        """Обновляет положение снаряда"""
        if self.rocket.image == self.rocket.image_right:
            self.direction = "right"
            self.rect = pygame.Rect(0, 0, self.settings.bullets_height, self.settings.bullets_width)
            self.rect.midbottom = self.rocket.rect.midright
            self.rect.y = self.rocket.rect.y + 45
        elif self.rocket.image == self.rocket.image_left:
            self.direction = "left"
            self.rect = pygame.Rect(0, 0, self.settings.bullets_height, self.settings.bullets_width)
            self.rect.midbottom = self.rocket.rect.midleft
            self.rect.y = self.rocket.rect.y + 45
        elif self.rocket.image == self.rocket.image_up:
            self.direction = "up"
            self.rect = pygame.Rect(0, 0, self.settings.bullets_width, self.settings.bullets_height)
            self.rect.midbottom = self.rocket.rect.midtop
        elif self.rocket.image == self.rocket.image_down:
            self.direction = "down"
            self.rect = pygame.Rect(0, 0, self.settings.bullets_width, self.settings.bullets_height)
            self.rect.midbottom = self.rocket.rect.midbottom

    def update(self):
        """Обновляет направление снаряда"""
        if self.direction == 'right':
            self.rect.x += self.settings.bullets_speed
        if self.direction == 'left':
            self.rect.x -= self.settings.bullets_speed
        if self.direction == 'up':
            self.rect.y -= self.settings.bullets_speed
        if self.direction == 'down':
            self.rect.y += self.settings.bullets_speed


    def draw_bullet(self):
        """Рисует снаряд"""
        pygame.draw.rect(self.screen, self.color, self.rect)
