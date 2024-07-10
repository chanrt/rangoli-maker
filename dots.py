import pygame as pg
from settings import settings as s
from text import Text


class Dots:
    def __init__(self):
        self.dot_state = 0
        self.dots = [(800, 600)]
        self.tooltip = None

        self.text = Text(200, 200, "[D]ot Mode: Off", s.screen)
        self.text.set_font(s.small_font)

    def toggle_state(self):
        self.dot_state = (self.dot_state + 1) % 2

        if self.dot_state == 0:
            self.text.set_text("[D]ot Mode: Off")
        elif self.dot_state == 1:
            self.text.set_text("[D]ot Mode: On")

    def search_dot(self, coords):
        index = -1
        for i, dot in enumerate(self.dots):
            if (dot[0] - coords[0]) ** 2 + (dot[1] - coords[1]) ** 2 < s.dot_radius ** 2:
                index = i
                break

        return index

    def modify(self, mouse_coords, mouse_button):
        index = self.search_dot(mouse_coords)
        if mouse_button == 1 and index == -1:
            self.dots.append(mouse_coords)
        elif mouse_button == 3 and index != -1:
            self.dots.pop(index)
            self.tooltip = None

    def show_tooltip(self, mouse_coords):
        index = self.search_dot(mouse_coords)
        if index != -1:
            self.tooltip = index
        else:
            self.tooltip = None

    def render(self):
        self.text.render()
        for dot in self.dots:
            pg.draw.circle(s.screen, s.dot_color, dot, s.dot_radius)

        if self.dot_state and self.tooltip is not None:
            pg.draw.circle(s.screen, s.dot_color, self.dots[self.tooltip], 2 * s.dot_radius, 1)