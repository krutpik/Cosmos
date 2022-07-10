import pygame.font


class Score:
    """Класс для вывода игровой информации"""

    def __init__(self, screen, settings):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.stats = 10
        self.text_color = (250, 250, 250)

    def prep_score(self, size, x, y):
        """Преобразует текущий счет в графическое изображение"""
        self.font = pygame.font.Font('Font/VinSlabPro-Light_0.ttf', size)
        self.score_str = str(self.stats)
        self.score_image = self.font.render(self.score_str, True, self.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.x = x
        self.score_rect.y = y

    def show_score(self):
        """Выводит счёт на экран"""
        self.screen.blit(self.score_image, self.score_rect)
