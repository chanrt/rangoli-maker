import pygame as pg


class Settings:
    def __init__(self):
        pg.init()

        self.bg_color = (1, 22, 39)

        self.big_font_size = 48
        self.small_font_size = 32
    
    def init_screen(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = screen.get_size()


settings = Settings()