from math import cos, pi, sin
import pygame as pg
from settings import settings as s


class Grid:
    def __init__(self):
        self.grid_state = 0
        self.magnification = 1.0
        self.lines = []
        self.init_lines()
        self.spacing = 100

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

            x = -10 * self.spacing
            while x < s.screen_width:
                self.lines.append([(x, 0), (x + s.screen_width * cos(pi / 3), s.screen_width * sin(pi / 3))])
                x += self.spacing

            x = 0
            while x < s.screen_width + 10 * self.spacing:
                self.lines.append([(x, 0), (x + s.screen_width * cos(2 * pi / 3), s.screen_width * sin(2 * pi / 3))])
                x += self.spacing

    def toggle_state(self):
        self.grid_state = (self.grid_state + 1) % 3  
        self.init_lines()

    def modify_magnification(self, factor):
        self.spacing += factor
        self.init_lines()
    
    def render(self):
        if self.grid_state > 0:
            for line in self.lines:
                start, end = line
                pg.draw.line(s.screen, s.grid_color, start, end)