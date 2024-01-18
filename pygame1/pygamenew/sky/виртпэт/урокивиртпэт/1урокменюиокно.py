import pygame as pg

# Инициализация pg
pg.init()

# Размеры окна
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 550

ICON_SIZE = 80#1
PADDING = 5 # константа отступ от экрана
#функция для загрузки картинок любых
def load_image(file, width, height):#1
    image = pg.image.load(file).convert_alpha() #file- название файла
    image = pg.transform.scale(image, (width, height))
    return image

class Game:
    def __init__(self):

        # Создание окна
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Виртуальный питомец")

        self.happiness = 100#1
        self.satiety = 100#1 сытость
        self.health = 100#1

        self.background=pg.image.load( "images/background.jpg")#1 загрузка картинки заднего фона из папки images
        self.background = pg.transform.scale(self.background,(SCREEN_WIDTH,SCREEN_HEIGHT))#1 изменение масштаба по ширине экрана

        # Загрузка иконок
        self.happiness_image = load_image("images/happiness.png", ICON_SIZE, ICON_SIZE)#1

        self.satiety_image = load_image("images/satiety.png", ICON_SIZE, ICON_SIZE)  # 1.s
        self.health_image = load_image("images/health.png", ICON_SIZE, ICON_SIZE)  # 1.s
        self.money_image = load_image("images/money.png", ICON_SIZE, ICON_SIZE)  # 1.s


        self.run()

    def run(self):
        while True:
            self.event()
            self.update()
            self.draw()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

    def update(self):
        ...

    def draw(self):
        self.screen.blit(self.background, (0, 0)) #1отрисовка фона в координатах 0,0
        self.screen.blit(self.happiness_image, (PADDING, PADDING))  # 1отрисовка иконки в координатах 5,5

        self.screen.blit(self.satiety_image, (5, 100))  #1.s
        self.screen.blit(self.health_image, (5, 200))  # 1.s
        self.screen.blit(self.money_image, (SCREEN_WIDTH-80-5, 5))  # 1.s
        pg.display.flip()


if __name__ == "__main__":
    Game()