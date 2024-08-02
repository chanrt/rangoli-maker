import pygame as pg


class Settings:
    def __init__(self):
        pg.init()

        # lengths
        self.grid_spacing = 100.0
        self.dot_radius = 5
        self.line_thickness = 3
        self.tooltip_thickness = 2

        # fonts
        self.bg_color = (1, 22, 39)
        self.grid_color = (115, 147, 179)
        self.dot_color = (255, 255, 255)
        self.construct_color = (0, 0, 255)
        self.destruct_color = (255, 0, 0)
        self.line_color = (255, 255, 255)

        # colors
        self.big_font_size = 48
        self.small_font_size = 32

        self.big_font = pg.font.Font("assets/Wittgenstein-Medium.ttf", self.big_font_size)
        self.small_font = pg.font.Font("assets/Wittgenstein-Medium.ttf", self.small_font_size)
    
    def init_screen(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = screen.get_size()
        self.bg_color_map = self.screen.map_rgb(self.bg_color)
        self.init_color_palette()

    def init_color_palette(self):
        self.rect_length = 25
        self.gap = 6
        self.colors = [
            (0, 0, 0), # black
            (128, 128, 128), # gray
            (192, 192, 192), # light gray
            (255, 255, 255), # white

            (235, 51, 36), # red
            (58, 6, 3), # dark red
            (119, 67, 66), # brown

            (0, 35, 245), # blue
            (126, 132, 247), # light blue
            (0, 18, 154), # dark blue
            (239, 136, 190), # pink

            (117, 249, 77), # green
            (161, 251, 142), # light green
            (55, 125, 34), # dark green

            (255, 253, 85), # yellow
            (240, 134, 80), # orange
        ]
        self.num_colors = len(self.colors)
        self.start_x = (self.screen_width - self.num_colors * (self.rect_length + self.gap)) // 2
        self.start_y = self.screen_height - self.rect_length - self.gap

settings = Settings()