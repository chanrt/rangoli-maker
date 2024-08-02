import pygame as pg
from settings import settings as s
from text import Text


class Dots:
    def __init__(self):
        self.state = 0
        self.display_state = 1
        self.dots = []
        self.tooltip = None

        self.text = Text(200, 200, "[D]ot Mode: Off", s.screen)
        self.text.set_font(s.small_font)

    def toggle_state(self):
        self.state = (self.state + 1) % 2

        if self.state == 0:
            self.text.set_text("[D]ot Mode: Off")
        elif self.state == 1:
            self.text.set_text("[D]ot Mode: On")

    def toggle_display_state(self):
        self.display_state = (self.display_state + 1) % 2

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
            return len(self.dots) - 1, True
        elif mouse_button == 3 and index != -1:
            self.dots.pop(index)
            self.tooltip = None
            return index, False
        
        return None

    def show_tooltip(self, mouse_coords):
        index = self.search_dot(mouse_coords)
        if index != -1:
            self.tooltip = index
        else:
            self.tooltip = None

    def get_bounds(self):
        x_min = min([dot[0] for dot in self.dots])
        x_max = max([dot[0] for dot in self.dots])
        y_min = min([dot[1] for dot in self.dots])
        y_max = max([dot[1] for dot in self.dots])

        width = x_max - x_min
        height = y_max - y_min
        return x_min, y_min, width, height

    def render(self):
        self.text.render()

        if not self.display_state:
            return
        
        for dot in self.dots:
            pg.draw.circle(s.screen, s.dot_color, dot, s.dot_radius)

        if self.state and self.tooltip is not None:
            if self.tooltip < len(self.dots):
                pg.draw.circle(s.screen, s.dot_color, self.dots[self.tooltip], 2 * s.dot_radius, s.tooltip_thickness)