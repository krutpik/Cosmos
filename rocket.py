import pygame


class Rocket:
    """Класс для управления кораблём"""

    def __init__(self, screen, settings):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.image = pygame.image.load('image/pixil-frame-0.png')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.move_RIGHT = False
        self.move_LEFT = False
        self.move_UP = False
        self.move_DOWN = False
        self.image_right = pygame.transform.rotate(self.image, -90)
        self.image_left = pygame.transform.rotate(self.image, 90)
        self.image_up = pygame.transform.rotate(self.image, 0)
        self.image_down = pygame.transform.rotate(self.image, 180)

    def update_rocket(self):
        """Обновляет позицию корабля"""
        if self.move_RIGHT and self.rect.right < self.screen_rect.right:
            self.image = self.image_right
            self.x += self.settings.rocket_speed
        if self.move_LEFT and self.rect.left > self.screen_rect.left:
            self.image = self.image_left
            self.x -= self.settings.rocket_speed
        if self.move_UP and self.rect.top > self.screen_rect.top:
            self.image = self.image_up
            self.y -= self.settings.rocket_speed
        if self.move_DOWN and self.rect.bottom < self.screen_rect.bottom:
            self.image = self.image_down
            self.y += self.settings.rocket_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_rocket(self):
        """Отрисовывает корабль"""
        self.screen.blit(self.image, self.rect)
