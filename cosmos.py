import sys

import pygame


class Cosmos:
    """Главный класс игры Cosmos"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption('Cosmos')
        self.fon_image = pygame.image.load('image/Fon.png')
        self.fon = self.fon_image.get_rect()


    def key_event(self):
        """Обрабатывает нажатие клавиш"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

    def run_game(self):
        """Обновляет события игры"""
        while True:
            self.key_event()
            self.screen.blit(self.fon_image, self.fon)
            pygame.display.flip()


game = Cosmos()
game.run_game()
