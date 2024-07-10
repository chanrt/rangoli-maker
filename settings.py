import pygame as pg


class Settings:
    def __init__(self):
        pg.init()

        # lengths
        self.grid_spacing = 100.0
        self.dot_radius = 5

        # fonts
        self.bg_color = (1, 22, 39)
        self.grid_color = (115, 147, 179)
        self.dot_color = (255, 255, 255)

        # colors
        self.big_font_size = 48
        self.small_font_size = 32

        self.big_font = pg.font.Font("assets/Wittgenstein-Medium.ttf", self.big_font_size)
        self.small_font = pg.font.Font("assets/Wittgenstein-Medium.ttf", self.small_font_size)
    
    def init_screen(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = screen.get_size()


settings = Settings()