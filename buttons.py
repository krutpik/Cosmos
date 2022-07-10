import pygame.font


class Buttons:
    """Класс представляющий кнопку"""

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.button_play1()

    def button_play(self, text, x, y):
        self.text_color = 250, 250, 250
        self.font = pygame.font.Font('Font/calibrib.ttf', 100)
        self.text = text
        self.font_image = self.font.render(self.text, True, self.text_color)
        self.font_image_rect = self.font_image.get_rect()
        self.font_image_rect.x = x
        self.font_image_rect.y = y

    def draw_button(self):
        """Отрисовывает кнопку 'Play'"""
        self.screen.blit(self.font_image, self.font_image_rect)

    def button_play1(self):
        self.text_color = 250, 250, 250
        self.font = pygame.font.Font('Font/calibrib.ttf', 80)
        self.font_image1 = self.font.render('MENU', True, self.text_color)
        self.font_image_rect1 = self.font_image1.get_rect()
        self.font_image_rect1.x = 823
        self.font_image_rect1.y = 800

    def draw_button1(self):
        """Отрисовывает кнопку 'Menu'"""
        self.screen.blit(self.font_image1, self.font_image_rect1)

    def button_play2(self, text, x ,y):
        self.text_color = 250, 250, 250
        self.font = pygame.font.Font('Font/calibrib.ttf', 100)
        self.font_image2 = self.font.render(text, True, self.text_color)
        self.font_image_rect2 = self.font_image2.get_rect()
        self.font_image_rect2.x = x
        self.font_image_rect2.y = y

    def draw_button2(self):
        """Отрисовывает кнопку 'Exit'"""
        self.screen.blit(self.font_image2, self.font_image_rect2)
