import sys

import pygame

from settings import Settings

from rocket import Rocket

from bullet import Bullet

from alien import Alien


class Cosmos:
    """Главный класс игры Cosmos"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('Cosmos')
        self.fon_image = pygame.image.load('image/Fon.png')
        self.fon = self.fon_image.get_rect()
        self.menu_image = pygame.image.load('image/Menu.png')
        self.menu = self.menu_image.get_rect()
        self.settings = Settings()
        self.rocket = Rocket(self.screen, self.settings)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.alien_numbers = 0
        self.game_status = True

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

    def spawn_alien(self):
        """Генерирует новых пришельцев"""
        alien = Alien(self.screen, self.settings, self.rocket)
        if ((self.rocket.rect.x - 10) >= alien.rect.x <= (self.rocket.rect.x + 10)) and\
                ((self.rocket.rect.y - 10) >= alien.rect.y <= (self.rocket.rect.y + 10)):
            if self.alien_numbers < self.settings.appearance_speed_aliens * pygame.time.get_ticks() / 1000:
                self.aliens.add(alien)
                self.alien_numbers += 1

    def bullet_sprite(self):
        """Рисует и обновляет спрайт снаряда"""
        for bullet in self.bullets.sprites():
            if bullet.rect.x < 5000 and bullet.rect.x > 0 and bullet.rect.y < 1500 and bullet.rect.y > 0:
                bullet.draw_bullet()
                bullet.update()
            else:
                self.bullets.remove(bullet)

    def game_finish(self):
        """Завершение игры"""
        if pygame.sprite.spritecollideany(self.rocket, self.aliens):
            self.game_status = False

    def run_game(self):
        """Обновляет события игры"""
        while True:
            if not self.game_status:
                self.screen.blit(self.menu_image, self.menu)
                self.key_event()
            else:
                self.screen.blit(self.fon_image, self.fon)
                self.key_event()
                self.rocket.update_rocket()
                pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
                self.bullet_sprite()
                self.rocket.draw_rocket()
                self.spawn_alien()
                self.aliens.update()
                self.aliens.draw(self.screen)
                self.game_finish()
            pygame.display.flip()


game = Cosmos()
game.run_game()
