import pygame

import sys

from settings import Settings

from rocket import Rocket

from bullet import Bullet

from alien import Alien

from buttons import Buttons

from score import Score


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
        self.kill_screen = pygame.image.load('image/kill screen.png')
        self.kill_screen_rect = self.kill_screen.get_rect()
        self.settings = Settings()
        self.rocket = Rocket(self.screen, self.settings)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.alien_numbers = 0
        self.game_status = False
        self.play_button = Buttons(self.screen)
        self.score = Score(self.screen, self.settings)
        self.kills_alien = 0
        self.level = 5
        self.kills = 0

    def key_event(self):
        """Обрабатывает нажатие клавиш"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)
                self.check_menu_button(mouse_pos)
                self.check_exit_button(mouse_pos)

    def check_play_button(self, mouse_pos):
        """Запускает новую игру при нажатии кнопки Play"""
        button_clicked = self.play_button.font_image_rect.collidepoint(mouse_pos)
        if (button_clicked and not self.game_status) or self.kills > 0 and button_clicked:
            self.aliens.empty()
            self.bullets.empty()
            self.rocket.rect.center = self.screen_rect.center
            self.rocket.x = float(self.rocket.rect.x)
            self.rocket.y = float(self.rocket.rect.y)
            self.rocket.image = self.rocket.image_up
            self.game_status = True
            self.alien_numbers = 0
            self.kills = 0

    def check_menu_button(self, mouse_pos):
        """Открывает игровое меню при нажатии кнопки Menu"""
        button_clicked = self.play_button.font_image_rect1.collidepoint(mouse_pos)
        if button_clicked and self.kills > 0:
            self.game_status = False

    def check_exit_button(self, mouse_pos):
        """Выход из игры при нажатии кнопки Exit"""
        button_clicked = self.play_button.font_image_rect2.collidepoint(mouse_pos)
        if button_clicked:
            sys.exit()

    def spawn_alien(self, start_time):
        """Генерирует новых пришельцев"""
        alien = Alien(self.screen, self.settings, self.rocket)
        if ((self.rocket.rect.x - 100) >= alien.rect.x <= (self.rocket.rect.x + 100)) and \
                ((self.rocket.rect.y - 100) >= alien.rect.y <= (self.rocket.rect.y + 100)):
            if self.alien_numbers < self.settings.appearance_speed_aliens * (
                    pygame.time.get_ticks() - start_time) / 1000:
                alien.spawn_alien()
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

    def new_level(self):
        """Обновляет уровень сложности"""
        if self.kills_alien > self.level:
            self.settings.alien_speed *= 1.1
            self.level += 5

    def game_finish(self):
        """Завершение игры"""
        if pygame.sprite.spritecollideany(self.rocket, self.aliens):
            self.kills += 1

    def game_timer(self, start_time):
        """Игровой секундомер"""
        current_time = pygame.time.get_ticks()
        self.score.stats = 1 * (current_time - start_time) // 1000
        self.score.prep_score(48, 1870, 20)

    def run_game(self):
        """Обновляет события игры"""
        while True:
            if not self.game_status:
                self.screen.blit(self.menu_image, self.menu)
                self.play_button.button_play('PLAY', 110, 380)
                self.play_button.draw_button()
                self.play_button.button_play2('EXIT', 110, 550)
                self.play_button.draw_button2()
                self.key_event()
                pygame.mouse.set_visible(True)
                self.settings.alien_speed = 1
                self.settings.appearance_speed_aliens = 1
                self.alien_numbers = 0
                start_time = pygame.time.get_ticks()
            elif self.kills > 0:
                self.screen.blit(self.kill_screen, self.kill_screen_rect)
                self.play_button.button_play('PLAY', 830, 680)
                self.play_button.draw_button()
                self.play_button.button_play1()
                self.play_button.draw_button1()
                self.key_event()
                pygame.mouse.set_visible(True)
                self.settings.alien_speed = 1
                self.settings.appearance_speed_aliens = 1
                self.score.prep_score(100, 910, 300)
                self.score.show_score()
                start_time = pygame.time.get_ticks()
            else:
                self.screen.blit(self.fon_image, self.fon)
                pygame.mouse.set_visible(False)
                self.key_event()
                self.rocket.update_rocket()
                collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
                if collisions:
                    self.kills_alien += 1
                self.new_level()
                self.game_timer(start_time)
                self.bullet_sprite()
                self.rocket.draw_rocket()
                self.spawn_alien(start_time)
                self.aliens.update()
                self.aliens.draw(self.screen)
                self.score.show_score()
                self.game_finish()
            pygame.display.flip()


game = Cosmos()
game.run_game()
