import pygame as pg

# Инициализация pg
pg.init()

# Размеры окна
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 550

ICON_SIZE = 80  # 1
PADDING = 5  # константа отступ от экрана

BUTTON_WIDTH = 200  # 3константа для создания кнопок
BUTTON_HEIGHT = 60  # 3константа для создания кнопок
font = pg.font.Font(None, 40)  # 3


# функция для загрузки картинок любых
def load_image(file, width, height):  # 1
    image = pg.image.load(file).convert_alpha()  # file- название файла
    image = pg.transform.scale(image, (width, height))
    return image


def text_render(text):
    return font.render(str(text), True, "black")  # 3


class Button:  # 3 создаем класс для кнопок
    def __init__(self, text, x, y, ):  # конструктор класса в котором мы просим указать координаты будущей кнопки

        self.idle_image = load_image("images/button.png", BUTTON_WIDTH, BUTTON_HEIGHT)  # 3 обычное состояние кнопки
        self.pressed_image = load_image("images/button_clicked.png", BUTTON_WIDTH,
                                        BUTTON_HEIGHT)  # 3 нажатое состояние кнопки картинка чуть светлее
        self.image = self.idle_image  # 3 изначальное состояние кнопки кнопка в покое
        self.rect = self.image.get_rect()  # 3 создаем для нее рект то есть координаты
        self.rect.topleft = (x, y)  # 3 указываем координаты

        self.is_pressed = False  # 3 изначальное состояние кнопки нажата или нет

        # self.text_font = text_font#3 шрифт для кнопки
        # self.text = self.text_font.render(str(text), True, "black") #3 текст для кнопок
        self.text = text_render(text)
        self.text_rect = self.text.get_rect()  # 3 текст для кнопок
        self.text_rect.center = self.rect.center  # 3 текст для кнопок

    def draw(self, screen):  # 3 метод для отрисовки кнопки
        screen.blit(self.image, self.rect)  # параметры картинка и координаты
        screen.blit(self.text, self.text_rect)  # параметры картинка и координаты

    def update(self):  # 3метод обновления кнопки
        mouse_pos = pg.mouse.get_pos()  # 3функция проверяет позицию кнопки
        if self.rect.collidepoint(mouse_pos):  # 3 если позиция кнопки пересекается с мышкой
            if self.is_pressed:  # 3 если кнопка нажата
                self.image = self.pressed_image  # 3 картинка мыши будет нажатой кнопкой
            else:
                self.image = self.idle_image  # 3 иначе картинка будет не нвжатой кнопкой

    def is_clicked(self, event):  # 3специальный метод который мы будем вызывать в евентах игры
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:  # 3 если евент ттип это нажатая кнопка мыщи и нажата левая кнопка
            if self.rect.collidepoint(event.pos):  # 3 проверяем над кнопкой ли мышка
                self.is_pressed = True  # 3 меняем нажатая мышка на правду
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:  # 3 для отжатой кнопки
            self.is_pressed = False

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.is_put_on = False
        self.is_bought = False

class Game:
    def __init__(self):

        # Создание окна
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Виртуальный питомец")

        self.happiness = 100  # 1
        self.satiety = 100  # 1 сытость
        self.health = 100  # 1

        self.background = pg.image.load("images/background.jpg")  # 1 загрузка картинки заднего фона из папки images
        self.background = pg.transform.scale(self.background,
                                             (SCREEN_WIDTH, SCREEN_HEIGHT))  # 1 изменение масштаба по ширине экрана

        # Загрузка иконок
        self.happiness_image = load_image("images/happiness.png", ICON_SIZE, ICON_SIZE)  # 1

        self.satiety_image = load_image("images/satiety.png", ICON_SIZE, ICON_SIZE)  # 1.s
        self.health_image = load_image("images/health.png", ICON_SIZE, ICON_SIZE)  # 1.s
        self.money_image = load_image("images/money.png", ICON_SIZE, ICON_SIZE)  # 1.s# Создание кнопок

        button_x = SCREEN_WIDTH - BUTTON_WIDTH - PADDING  # 3 переменная для координаты x кнопки

        self.eat_button = Button("еда", button_x, PADDING + ICON_SIZE)  # 3 создание кнопки еды

        self.clothes_button = Button("одежда", button_x, PADDING + ICON_SIZE + BUTTON_HEIGHT + 10)  # 3s

        self.buttons = [...]  # пустой список для будущих кнопок

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

            self.eat_button.is_clicked(event)  # 3проверяем нажата ли кнопка или нет
            self.clothes_button.is_clicked(event)  # 3s

    def update(self):
        self.eat_button.update()  # 3 обновляем кнопку
        self.clothes_button.update()  # 3s обновляем кнопку одежды
        ...

    def draw(self):
        self.screen.blit(self.background, (0, 0))  # 1отрисовка фона в координатах 0,0
        self.screen.blit(self.happiness_image, (PADDING, PADDING))  # 1отрисовка иконки в координатах 5,5

        self.screen.blit(self.satiety_image, (5, 100))  # 1.s
        self.screen.blit(self.health_image, (5, 200))  # 1.s
        self.screen.blit(self.money_image, (SCREEN_WIDTH - 80 - 5, 5))  # 1.s

        self.eat_button.draw(self.screen)  # 3 отрисовываем кнопку на экране
        self.clothes_button.draw(self.screen)  # 3s отрисовываем кнопку на экране
        pg.display.flip()


if __name__ == "__main__":
    Game()
