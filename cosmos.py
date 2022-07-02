import sys

import pygame

from rocket import Rocket


class Cosmos:
    """Главный класс игры Cosmos"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption('Cosmos')
        self.fon_image = pygame.image.load('image/Fon.png')
        self.fon = self.fon_image.get_rect()
        self.rocket = Rocket(self.screen)

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
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.rocket.move_RIGHT = False
                elif event.key == pygame.K_a:
                    self.rocket.move_LEFT = False
                elif event.key == pygame.K_w:
                    self.rocket.move_UP = False
                elif event.key == pygame.K_s:
                    self.rocket.move_DOWN = False

    def run_game(self):
        """Обновляет события игры"""
        while True:
            self.screen.blit(self.fon_image, self.fon)
            self.rocket.draw_rocket()
            self.key_event()
            self.rocket.update_rocket()
            pygame.display.flip()


game = Cosmos()
game.run_game()
