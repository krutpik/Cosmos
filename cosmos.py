import sys

import pygame

from settings import Settings

from rocket import Rocket

from bullet import Bullet


class Cosmos:
    """Главный класс игры Cosmos"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('Cosmos')
        self.fon_image = pygame.image.load('image/Fon.png')
        self.fon = self.fon_image.get_rect()
        self.settings = Settings()
        self.rocket = Rocket(self.screen, self.settings)
        self.bullets = pygame.sprite.Group()

    def key_event(self):
        """Обрабатывает нажатие клавиш"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_d:
                    self.rocket.move_RIGHT = True
                elif event.key == pygame.K_a:
                    self.rocket.move_LEFT = True
                elif event.key == pygame.K_w:
                    self.rocket.move_UP = True
                elif event.key == pygame.K_s:
                    self.rocket.move_DOWN = True
                elif event.key == pygame.K_SPACE:
                    new_bullet = Bullet(self.screen, self.settings, self.rocket)
                    self.bullets.add(new_bullet)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.rocket.move_RIGHT = False
                elif event.key == pygame.K_a:
                    self.rocket.move_LEFT = False
                elif event.key == pygame.K_w:
                    self.rocket.move_UP = False
                elif event.key == pygame.K_s:
                    self.rocket.move_DOWN = False

    def bullet_sprite(self):
        """Рисует и обновляет спрайт снаряда"""
        for bullet in self.bullets.sprites():
            if bullet.rect.x < 5000 and bullet.rect.x > 0 and bullet.rect.y < 1500 and bullet.rect.y > 0:
                bullet.draw_bullet()
                bullet.update()
            else:
                self.bullets.remove(bullet)

    def run_game(self):
        """Обновляет события игры"""
        while True:
            self.screen.blit(self.fon_image, self.fon)
            self.key_event()
            self.rocket.update_rocket()
            self.bullet_sprite()
            self.rocket.draw_rocket()
            pygame.display.flip()


game = Cosmos()
game.run_game()
