from math import cos, pi, sin
import pygame as pg
from settings import settings as s
from text import Text


class Symmetry:
    def __init__(self, dots, lines, color):
        self.state = 0
        self.dots = dots
        self.lines = lines
        self.color = color

        self.angle = 0
        self.num_rotations = 0

        self.text = Text(200, 500, "[S]ymmetry: None", s.screen)
        self.text.set_font(s.small_font)

        self.com_x = 0
        self.com_y = 0

    def toggle_state(self):
        self.state = (self.state + 1) % 4

        if self.state == 0:
            self.text.set_text("[S]ymmetry: None")
            self.angle = 0
            self.num_rotations = 0
        elif self.state == 1:
            self.text.set_text("[S]ymmetry: C3")
            self.angle = 2 * pi / 3
            self.num_rotations = 2
        elif self.state == 2:
            self.text.set_text("[S]ymmetry: C4")
            self.angle = pi / 2
            self.num_rotations = 3
        else:
            self.text.set_text("[S]ymmetry: C6")
            self.angle = pi / 3
            self.num_rotations = 4

    def calc_com(self):
        num_dots = len(self.dots.dots)
        if num_dots == 0:
            self.com_x, self.com_y = 0, 0
            return
        
        self.com_x = sum([dot[0] for dot in self.dots.dots])
        self.com_y = sum([dot[1] for dot in self.dots.dots])
        self.com_x /= num_dots
        self.com_y /= num_dots
        self.com_x = int(self.com_x)
        self.com_y = int(self.com_y)

    def get_closest_dot(self, x, y):
        min_distance = float("inf")
        min_index = -1

        for i, other_dot in enumerate(self.dots.dots):
            distance = (x - other_dot[0]) ** 2 + (y - other_dot[1]) ** 2
            if distance < min_distance:
                min_distance = distance
                min_index = i

        return min_index

    def get_rotated_point_com(self, x, y, rot_angle):
        vector_x = x - self.com_x
        vector_y = y - self.com_y

        rotated_x = cos(rot_angle) * vector_x - sin(rot_angle) * vector_y
        rotated_y = sin(rot_angle) * vector_x + cos(rot_angle) * vector_y

        rotated_x += self.com_x
        rotated_y += self.com_y

        return rotated_x, rotated_y

    def get_rotated_dot(self, index, rot_angle):
        dot = self.dots.dots[index]
        rotated_x, rotated_y = self.get_rotated_point_com(dot[0], dot[1], rot_angle)
        return self.get_closest_dot(rotated_x, rotated_y)

    def consider_line(self, line_modified):
        if self.state == 0:
            return

        dot1, dot2 = line_modified[0], line_modified[1]
        line_exists = (self.lines.search_line(dot1, dot2) != -1)

        current_angle = 0
        for _ in range(self.num_rotations):
            current_angle += self.angle
            rotated_dot1 = self.get_rotated_dot(dot1, current_angle)
            rotated_dot2 = self.get_rotated_dot(dot2, current_angle)

            if rotated_dot1 == -1 or rotated_dot2 == -1:
                continue

            if line_exists:
                self.lines.lines.append([rotated_dot1, rotated_dot2])
                self.color.fabricate()
            else:
                line_index = self.lines.search_line(rotated_dot1, rotated_dot2)
                if line_index != -1:
                    self.lines.lines.pop(line_index)
                    self.color.fabricate()

    def consider_dot(self, index):
        if self.state == 0:
            return
        
        dot = self.dots.dots[index]
        x, y = dot[0], dot[1]
        current_angle = 0

        for _ in range(self.num_rotations):
            current_angle += self.angle
            rotated_x, rotated_y = self.get_rotated_point_com(x, y, current_angle)
            self.dots.modify((int(rotated_x), int(rotated_y)), 1)

    def render(self):
        self.text.render()

        if self.state != 0 and self.com_x != 0:
            if self.state == 1:
                pg.draw.line(s.screen, s.symmetry_color, (self.com_x, self.com_y), (self.com_x + s.screen_width, self.com_y), 1)
                dx = cos(2 * pi / 3) * s.screen_width
                dy = sin(2 * pi / 3) * s.screen_width
                pg.draw.line(s.screen, s.symmetry_color, (self.com_x, self.com_y), (self.com_x + dx, self.com_y + dy), 1)
                dx = cos(4 * pi / 3) * s.screen_width
                dy = sin(4 * pi / 3) * s.screen_width
                pg.draw.line(s.screen, s.symmetry_color, (self.com_x, self.com_y), (self.com_x + dx, self.com_y + dy), 1)

            elif self.state == 2:
                pg.draw.line(s.screen, s.symmetry_color, (0, self.com_y), (s.screen_width, self.com_y), 1)
                pg.draw.line(s.screen, s.symmetry_color, (self.com_x, 0), (self.com_x, s.screen_height), 1)

            else:
                angle = 0
                while angle < 2 * pi:
                    dx = cos(angle) * s.screen_width
                    dy = sin(angle) * s.screen_width
                    pg.draw.line(s.screen, s.symmetry_color, (self.com_x, self.com_y), (self.com_x + dx, self.com_y + dy), 1)
                    angle += pi / 3