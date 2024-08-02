import pygame as pg

from color import Color
from dots import Dots
from dot_factory import DotFactory
from lines import Lines
from grid import Grid
from settings import settings as s
from symmetry import Symmetry
from text import Text


def app_loop():
    pg.init()
    pg.display.set_caption('Rangoli Maker')
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    s.init_screen(screen)

    grid = Grid()
    dots = Dots()
    lines = Lines(dots)
    color = Color(dots, lines)
    symmetry = Symmetry(dots, lines, color)

    title_text = Text(s.screen_width // 2, s.big_font_size // 2, "Rangoli Art", s.screen)
    title_text.set_font(s.big_font)
    
    while True:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    return
                
                if event.key == pg.K_DELETE:
                    dots = Dots()
                    lines = Lines(dots)
                    color = Color(dots, lines)
                    symmetry = Symmetry(dots, lines, color)
                
                # display toggles
                if event.key == pg.K_g:
                    grid.toggle_state()
                if event.key == pg.K_PERIOD:
                    dots.toggle_display_state()
                if event.key == pg.K_SLASH:
                    lines.toggle_display_state()
                if event.key == pg.K_s:
                    symmetry.toggle_state()

                # initialize square grid
                if grid.grid_state == 1 and pg.K_1 <= event.key <= pg.K_9:
                    number = event.key - pg.K_0
                    if 1 <= number <= 5:
                        number += 10

                    dots = Dots()
                    lines = Lines(dots)
                    color = Color(dots, lines)
                    symmetry = Symmetry(dots, lines, color)

                    dot_factory = DotFactory(dots)
                    dot_factory.square_pattern(number, s.screen_height / (number + 2))
                    symmetry.calc_com()

                # draw state toggles
                if event.key == pg.K_c:
                    color.toggle_state()
                    if dots.state:
                        dots.toggle_state()
                    if lines.state:
                        lines.toggle_state()
                if event.key == pg.K_d:
                    dots.toggle_state()
                    if color.state:
                        color.toggle_state()
                    if lines.state:
                        lines.toggle_state()
                if event.key == pg.K_l:
                    lines.toggle_state()
                    if dots.state:
                        dots.toggle_state()
                    if color.state:
                        color.toggle_state()

                if event.key == pg.K_UP:
                    grid.modify_magnification(10)
                if event.key == pg.K_DOWN:
                    grid.modify_magnification(-10)

            if event.type == pg.MOUSEBUTTONDOWN:
                if dots.state:
                    status = dots.modify(pg.mouse.get_pos(), event.button)
                    if status is not None:
                        index, exists = status
                        if not exists:
                            lines.communicate_deletion(index)
                        else:
                            symmetry.consider_dot(index)
                            
                if lines.state:
                    status = lines.modify(pg.mouse.get_pos(), event.button)
                    if status is not None:
                        color.fabricate()
                        symmetry.consider_line(status)

                if color.state:
                    color.modify(pg.mouse.get_pos(), event.button)

            if event.type == pg.MOUSEMOTION:
                if dots.state:
                    dots.show_tooltip(pg.mouse.get_pos())
                if lines.state:
                    lines.show_tooltip(pg.mouse.get_pos())

            if event.type == pg.MOUSEWHEEL:
                if event.y > 0:
                    grid.modify_magnification(10)
                elif event.y < 0:
                    grid.modify_magnification(-10)

            if event.type == pg.QUIT:
                pg.quit()
                return

        screen.fill(s.bg_color)

        color.render()
        grid.render()
        symmetry.render()
        dots.render()
        lines.render(pg.mouse.get_pos())

        title_text.render()
        pg.display.flip()


if __name__ == '__main__':
    app_loop()