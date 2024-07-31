import pygame as pg

from color import Color
from dots import Dots
from lines import Lines
from grid import Grid
from settings import settings as s
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

    title_text = Text(s.screen_width // 2, s.big_font_size // 2, "Rangoli Art", s.screen)
    title_text.set_font(s.big_font)
    
    while True:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    return
                
                # display toggles
                if event.key == pg.K_g:
                    grid.toggle_state()
                if event.key == pg.K_PERIOD:
                    dots.toggle_display_state()
                if event.key == pg.K_SLASH:
                    lines.toggle_display_state()

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
                        lines.communicate_deletion(status)
                if lines.state:
                    status = lines.modify(pg.mouse.get_pos(), event.button)
                    if status is not None:
                        color.fabricate()
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
        dots.render()
        lines.render(pg.mouse.get_pos())

        title_text.render()
        pg.display.flip()


if __name__ == '__main__':
    app_loop()