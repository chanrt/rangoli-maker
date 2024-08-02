from math import cos, pi, sin
from settings import settings as s

class DotFactory:
    def __init__(self, dots):
        self.dots = dots

    def square_pattern(self, length, spacing, center_x=None, center_y=None):
        self.dots.dots = []
        
        if center_x is None:
            center_x = s.screen_width // 2
        if center_y is None:
            center_y = s.screen_height // 2

        half = length // 2
        start_x = center_x - half * spacing + 200
        start_y = center_y - half * spacing + s.big_font_size

        for row in range(length):
            for col in range(length):
                x = int(start_x + col * spacing)
                y = int(start_y + row * spacing)
                self.dots.dots.append((x, y))

    def hexagon_pattern(self, length, spacing, center_x=None, center_y=None):
        num_rows = 2 * length - 1
        row_spacing, col_spacing = spacing * sin(pi / 3), spacing
        min_cols, max_cols = length, num_rows

        if center_x is None:
            center_x = s.screen_width // 2 + 200
        if center_y is None:
            center_y = s.screen_height // 2 + 100

        for row in range(num_rows):
            if row < length:
                num_cols = min_cols + row
            else:
                num_cols = -row + 3 * length - 2

            row_x = center_x - col_spacing * num_cols // 2
            row_y = center_y + (row - length) * row_spacing

            for col in range(num_cols):
                x = int(row_x + col_spacing * col)
                y = int(row_y)
                self.dots.dots.append((x, y))