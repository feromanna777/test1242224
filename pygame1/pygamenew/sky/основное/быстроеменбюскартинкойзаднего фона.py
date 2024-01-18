import os

import pygame_menu
import pygame as pg

pg.init()


class Menu:
    def __init__(self):

        self.surface = pg.display.set_mode((900, 550))
        background_image = pygame_menu.baseimage.BaseImage(
            image_path=os.path.join(os.path.dirname(__file__), 'заднийфон.jpg'),
            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY,
 
        )

        # Создание темы с использованием пользовательских параметров
        my_theme = pygame_menu.Theme(
            background_color=background_image,  # Использование изображения в качестве фона
            title_background_color=(4, 47, 126),
            title_font_shadow=True,
            widget_padding=25
            # Добавьте другие параметры темы по вашему выбору
        )

        self.menu = pygame_menu.Menu(
            height=550,
            width=900,
            theme=my_theme,
            title="Пример меню"
        )

        self.menu.add.button("Играть", self.start_game)
        self.menu.add.button("Выйти", self.quit_game)
        self.menu.add.button("Магазин", self.quit_game)

    def start_game(self):
        ...

    def quit_game(self):
        ...

    def run(self):
        while True:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

            self.surface.fill((0, 0, 0))  # Заливка фона цветом (здесь: черным)

            # Отрисовка меню
            self.menu.update(events)
            self.menu.draw(self.surface)

            pg.display.flip()







if __name__ == '__main__':
    menu= Menu()