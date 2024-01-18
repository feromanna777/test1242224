import pygame_menu
import pygame as pg

pg.init()


class Menu:
    def __init__(self):
        background_image = pygame_menu.BaseImage(
            image_path="background.jpg"
        )
        mytheme = pygame_menu.Theme(background_color=background_image,  # transparent background
                        title_background_color=(4, 47, 126),
                        title_font_shadow=True,
                        widget_padding=25,
                        widget_font_color=(255, 0, 0),  # Red font color for widgets
                        title_font_color=(0, 255, 0),  # Green font color for the title
                        selection_color=(0, 0,255) #цвет при наведении мыши
                        )


        self.surface = pg.display.set_mode((900, 550))
        self.menu = pygame_menu.Menu(
            height=550,
            width=900,
            # theme=pygame_menu.themes.THEME_SOLARIZED,
            title="меню",
            theme=mytheme,
        )

        self.menu.add.button("Играть", self.start_game)
        self.menu.add.button("Выйти", self.quit_game)
        self.menu.add.button("Магазин", self.quit_game)

        self.run()

    def start_game(self):
        ...

    def quit_game(self):
        ...

    def run(self):
        self.menu.mainloop(self.surface)


if __name__ == '__main__':
    menu_app = Menu()