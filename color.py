import pygame as pg
from settings import settings as s
from text import Text


class Color:
    def __init__(self, dots, lines):
        self.state = 0
        self.dots = dots
        self.lines = lines
        self.fill_color_index = 0

        self.maze = [[0 for _ in range(s.screen_height)] for _ in range(s.screen_width)]
        self.canvas = [[s.bg_color_map for _ in range(s.screen_height)] for _ in range(s.screen_width)]

        self.text = Text(200, 400, "[C]olor Mode: Off", s.screen)
        self.text.set_font(s.small_font)

        self.fabricate()

    def fabricate(self):
        self.maze = [[0 for _ in range(s.screen_height)] for _ in range(s.screen_width)]

        for line in self.lines.lines:
            dot1, dot2 = line
            x1, y1 = self.dots.dots[dot1]
            x2, y2 = self.dots.dots[dot2]
            x_range, y_range = abs(x1 - x2), abs(y1 - y2)
            num_points = max(x_range, y_range)

            if num_points == 0:
                continue

            dx, dy = (x2 - x1) / num_points, (y2 - y1) / num_points

            for i in range(num_points + 1):
                x, y = int(x1 + i * dx), int(y1 + i * dy)
                self.maze[x][y] = 1

        # for row in range(s.screen_height):
        #     for col in range(s.screen_width):
        #         print(self.maze[col][row], end=" ")
        #     print("")

    def modify(self, mouse_pos, mouse_button):
        mouse_x, mouse_y = mouse_pos
        if mouse_y > s.start_y:
            index = (mouse_x - s.start_x) // (s.rect_length + s.gap)
            if 0 <= index < s.num_colors:
                self.fill_color_index = index
            return

        stack = [mouse_pos]
        visited = [[False for _ in range(s.screen_height)] for _ in range(s.screen_width)]

        if mouse_button == 1:
            mapped_color = s.screen.map_rgb(s.colors[self.fill_color_index])
        elif mouse_button == 3:
            mapped_color = s.bg_color_map

        while len(stack) > 0:
            pixel = stack.pop()
            x, y = pixel
            visited[x][y] = True

            if x > 0 and not self.maze[x - 1][y] and not visited[x - 1][y]:
                self.canvas[x - 1][y] = mapped_color
                stack.append((x - 1, y))
            if x < s.screen_width - 1 and not self.maze[x + 1][y] and not visited[x + 1][y]:
                self.canvas[x + 1][y] = mapped_color
                stack.append((x + 1, y))
            if y > 0 and not self.maze[x][y - 1] and not visited[x][y - 1]:
                self.canvas[x][y - 1] = mapped_color
                stack.append((x, y - 1))
            if y < s.screen_height - 1 and not self.maze[x][y + 1] and not visited[x][y + 1]:
                self.canvas[x][y + 1] = mapped_color
                stack.append((x, y + 1))

    def toggle_state(self):
        self.state = (self.state + 1) % 2

        if self.state == 0:
            self.text.set_text("[C]olor Mode: Off")
        elif self.state == 1:
            self.text.set_text("[C]olor Mode: On")

    def render(self):        
        pixel_array = pg.PixelArray(s.screen)
        for col in range(s.screen_width):
            pixel_array[col] = self.canvas[col]
        pixel_array.close()

        self.text.render()

        if self.state:
            pg.draw.line(s.screen, (255, 255, 255), (0, s.start_y - s.gap), (s.screen_width, s.start_y - s.gap))

            x, y = s.start_x, s.start_y
            for i in range(s.num_colors):
                pg.draw.rect(s.screen, s.colors[i], (x, y, s.rect_length, s.rect_length))
                x += s.rect_length + s.gap

            x = s.start_x + self.fill_color_index * (s.rect_length + s.gap) - 2
            y = s.start_y - 2
            pg.draw.rect(s.screen, (255, 255, 255), (x, y, s.rect_length + 4, s.rect_length + 4), 2)