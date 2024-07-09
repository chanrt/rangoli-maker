import pygame as pg

from settings import settings as s
from text import Text


def app_loop():
    pg.init()
    pg.display.set_caption('Rangoli Maker')
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    s.init_screen(screen)

    big_font = pg.font.Font("assets/Wittgenstein-Medium.ttf", s.big_font_size)
    small_font = pg.font.Font("assets/Wittgenstein-Medium.ttf", s.small_font_size)

    title_text = Text(s.screen_width // 2, s.big_font_size // 2, "Rangoli Art", s.screen)
    title_text.set_font(big_font)
    
    while True:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    return
            if event.type == pg.QUIT:
                pg.quit()
                return
        
        screen.fill(s.bg_color)

        title_text.render()

        pg.display.flip()


if __name__ == '__main__':
    app_loop()