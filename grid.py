from math import cos, pi, sin
import pygame as pg
from settings import settings as s
from text import Text


class Grid:
    def __init__(self):
        self.grid_state = 0
        self.magnification = 1.0
        self.lines = []
        self.init_lines()
        self.spacing = 100

        self.text = Text(200, 100, "[G]rid Toggle: None", s.screen)
        self.text.set_font(s.small_font)

    def init_lines(self):
        self.lines = []

        if self.grid_state == 1:
            x = 0
            while x < s.screen_width:
                self.lines.append([(x, 0), (x, s.screen_height)])
                x += self.spacing

            y = 0
            while y < s.screen_height:
                self.lines.append([(0, y), (s.screen_width, y)])
                y += self.spacing

        if self.grid_state == 2:
            y = 0
            while y < s.screen_height:
                self.lines.append([(0, y), (s.screen_width, y)])
                y += self.spacing * sin(pi / 3)

            x = -20 * self.spacing
            while x < s.screen_width:
                self.lines.append([(x, 0), (x + s.screen_width * cos(pi / 3), s.screen_width * sin(pi / 3))])
                x += self.spacing

            x = 0
            while x < s.screen_width + 20 * self.spacing:
                self.lines.append([(x, 0), (x + s.screen_width * cos(2 * pi / 3), s.screen_width * sin(2 * pi / 3))])
                x += self.spacing

    def toggle_state(self):
        self.grid_state = (self.grid_state + 1) % 3  
        self.init_lines()

        if self.grid_state == 0:
            self.text.set_text("[G]rid Toggle: None")
        elif self.grid_state == 1:
            self.text.set_text("[G]rid Toggle: Square")
        elif self.grid_state == 2:
            self.text.set_text("[G]rid Toggle: Hexagon")

    def modify_magnification(self, factor):
        self.spacing += factor

        if self.spacing < 20:
            self.spacing = 20
        elif self.spacing > s.screen_width / 2:
            self.spacing = s.screen_width / 2

        self.init_lines()
    
    def render(self):
        self.text.render()

        if self.grid_state > 0:
            for line in self.lines:
                start, end = line
                pg.draw.line(s.screen, s.grid_color, start, end)