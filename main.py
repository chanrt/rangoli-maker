import pygame as pg

from dots import Dots
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

    title_text = Text(s.screen_width // 2, s.big_font_size // 2, "Rangoli Art", s.screen)
    title_text.set_font(s.big_font)
    
    while True:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    return
                if event.key == pg.K_g:
                    grid.toggle_state()
                if event.key == pg.K_d:
                    dots.toggle_state()
                if event.key == pg.K_UP:
                    grid.modify_magnification(10)
                if event.key == pg.K_DOWN:
                    grid.modify_magnification(-10)

            if event.type == pg.MOUSEBUTTONUP:
                if dots.dot_state:
                    dots.modify(pg.mouse.get_pos(), event.button)

            if event.type == pg.MOUSEMOTION:
                if dots.dot_state:
                    dots.show_tooltip(pg.mouse.get_pos())

            if event.type == pg.MOUSEWHEEL:
                if event.y > 0:
                    grid.modify_magnification(10)
                elif event.y < 0:
                    grid.modify_magnification(-10)
            if event.type == pg.QUIT:
                pg.quit()
                return
        
        screen.fill(s.bg_color)

        grid.render()
        dots.render()

        title_text.render()
        pg.display.flip()


if __name__ == '__main__':
    app_loop()