import pygame as pg
from settings import settings as s
from text import Text


class Lines:
    def __init__(self, dots):
        self.state = 0
        self.display_state = 1
        self.draw_state = 0
        self.dot1 = None

        self.lines = []
        self.tooltip = None
        self.dots = dots

        self.text = Text(200, 300, "[L]ine Mode: Off", s.screen)
        self.text.set_font(s.small_font)

    def search_line(self, index1, index2):
        index = -1
        for i, line in enumerate(self.lines):
            if (line[0] == index1 and line[1] == index2) or (line[0] == index2 and line[1] == index1):
                index = i
                break

        return index

    def toggle_state(self):
        self.state = (self.state + 1) % 2

        if self.state == 0:
            self.text.set_text("[L]ine Mode: Off")
            self.reset_state()
        elif self.state == 1:
            self.text.set_text("[L]ine Mode: On")

    def toggle_display_state(self):
        self.display_state = (self.display_state + 1) % 2

    def show_tooltip(self, mouse_coords):
        index = self.dots.search_dot(mouse_coords)
        if index != -1:
            self.tooltip = index
        else:
            self.tooltip = None

    def modify(self, mouse_coords, mouse_button):
        index = self.dots.search_dot(mouse_coords)

        if self.draw_state == 0:
            if index != -1:
                # a new dot has been selected
                self.dot1 = index

                if mouse_button == 1:
                    # for new line
                    self.draw_state = 1
                elif mouse_button == 3:
                    # for deleting an old line
                    self.draw_state = -1
            else:
                # reset
                self.dot1 = None
        elif self.draw_state == 1:
            if index != -1:
                # complete line and insert it if it doesn't exist
                self.dot2 = index
                line_index = self.search_line(self.dot1, self.dot2)

                if line_index == -1 and self.dot1 != self.dot2:
                    new_line = [self.dot1, self.dot2]
                    self.lines.append(new_line)
                    self.dot1 = self.dot2
                    return new_line
            else:
                # stop new line construction
                self.reset_state()
        elif self.draw_state == -1:
            if index != -1:
                # find line and delete if it exists
                self.dot2 = index
                line_index = self.search_line(self.dot1, self.dot2)

                if line_index != -1:
                    deleted_line = self.lines.pop(line_index)
                    self.reset_state()
                    return deleted_line
            else:
                # stop line deletion
                self.reset_state()
        return None

    def reset_state(self):
        self.dot1 = None
        self.dot2 = None
        self.draw_state = 0

    def communicate_deletion(self, index):
        to_delete = [line for line in self.lines if line[0] == index or line[1] == index]
        for line in to_delete:
            self.lines.remove(line)

        for line in self.lines:
            if line[0] > index:
                line[0] -= 1
            if line[1] > index:
                line[1] -= 1

    def render(self, mouse_coords):
        self.text.render()

        if not self.display_state:
            return

        for line in self.lines:
            start, end = line
            if start < len(self.dots.dots) and end < len(self.dots.dots):
                pg.draw.aaline(s.screen, s.line_color, self.dots.dots[start], self.dots.dots[end], s.line_thickness)

        if self.state and self.tooltip is not None:
            if self.tooltip < len(self.dots.dots): 
                pg.draw.circle(s.screen, s.dot_color, self.dots.dots[self.tooltip], 2 * s.dot_radius, 1)

        if self.draw_state != 0 and self.dot1 < len(self.dots.dots):
            if self.draw_state == 1:
                color = s.construct_color
                pg.draw.aaline(s.screen, s.line_color, self.dots.dots[self.dot1], mouse_coords, s.line_thickness)
            elif self.draw_state == -1:
                color = s.destruct_color

            pg.draw.circle(s.screen, color, self.dots.dots[self.dot1], 2 * s.dot_radius, 1)
