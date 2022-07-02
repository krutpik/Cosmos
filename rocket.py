import pygame


class Rocket:
    """Класс для управления кораблём"""

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load('image/pixil-frame-0.png')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.move_RIGHT = False
        self.move_LEFT = False
        self.move_UP = False
        self.move_DOWN = False
        self.image_right = pygame.transform.rotate(self.image, -90)
        self.image_left = pygame.transform.rotate(self.image, 90)
        self.image_up = pygame.transform.rotate(self.image, 0)
        self.image_down = pygame.transform.rotate(self.image, 180)

    def update_rocket(self):
        if self.move_RIGHT:
            self.image = self.image_right
            self.rect.x += 2
        if self.move_LEFT:
            self.image = self.image_left
            self.rect.x -= 2
        if self.move_UP:
            self.image = self.image_up
            self.rect.y -= 2
        if self.move_DOWN:
            self.image = self.image_down
            self.rect.y += 2

    def draw_rocket(self):
        self.screen.blit(self.image, self.rect)
