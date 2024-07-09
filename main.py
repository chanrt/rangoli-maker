import pygame as pg


def app_loop():
    pg.init()
    pg.display.set_caption('Rangoli Maker')
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    
    while True:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    return
            if event.type == pg.QUIT:
                pg.quit()
                return
        
        screen.fill((1, 22, 39))
        pg.display.flip()


if __name__ == '__main__':
    app_loop()