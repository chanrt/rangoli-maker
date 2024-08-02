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

    # need to write code for hexagon