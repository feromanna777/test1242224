import time

#CTRL SIFT R замена во всем проекте
#CTRL R замена в файле
from sprite import *


def dialogue_mode(sprite, text):
    ...


pg.init()
pg.mixer.init()

size = (800, 600)
screen = pg.display.set_mode(size)
pg.display.set_caption("Таинственный лес")

FPS = 120
clock = pg.time.Clock()

is_running = True
mode = "start_scene"

meteorites = pg.sprite.Group()
mice = pg.sprite.Group()
lasers = pg.sprite.Group()

space=pg.image.load("background.jpg").convert() #1загружаем фон и конвертируем
space=pg.transform.scale(space,size)    #1 изменяем масштаб делаем мастштаб по размеру окна

start_text = ["Мы засекли сигнал с планеты Мур.",
              "",
              "Наши друзья, инопланетные коты,",
              "нуждаются в помощи.",
              "Космические мыши хотят съесть их луну,",
              "потому что она похожа на сыр.",
              "Как долго наш народ страдал от них, ",
              "теперь и муряне в беде...",
              "Мы должны помочь им.",
              "Вылетаем прямо сейчас.",
              "Спасибо, что починил звездолёт, штурман. ",
              "Наконец-то функция автопилота работает.",
              "Поехали!"]

alien_text = ["СПАСИТЕ! МЫ ЕЛЕ ДЕРЖИМСЯ!",
              "",
              "Мыши уже начали грызть луну...",
              "Скоро куски луны будут падать на нас.",
              "Спасите муриан!", ]

final_text = ["Огромное вам спасибо,",
              "друзья с планеты Мяу!",
              "Как вас называть? Мяуанцы? Мяуриане?",
              "В любом случае, ",
              "теперь наша планета спасена!",
              "Мы хотим отблагодарить вас.",
              "Капитан Василий и его штурман получают",
              "орден SKYSMART.",
              "А также несколько бутылок нашей",
              "лучшей валерьянки.",
              "",
              ""]

text_number = 0

f1=pg.font.Font("Космические коты - шрифт.otf", 25) #1pg.font.Font() класс для создания шрифта. В скобках можно указать None для стандартного шрифта сиситемы или указать название файла со шрифтом второй аргумент размер шрифта

while is_running:

    # СОБЫТИЯ
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

    # ОБНОВЛЕНИЯ
    if mode == "start_scene":
        screen.blit(space,(0,0)) #1отрисовка игрового фона в координатах 0,0

        text1 = f1.render(start_text[text_number], True, pg.Color("White"))
        # text1 = f1.render("start_text", True, pg.Color("White"))
        #1 font.render(text, smoothing(сглаживание), color) — метод создаёт картинку с прозрачным фоном, на которой написан текст

        screen.blit(text1,(280,450)) #1отрисовка текста в заданных координатах

        if text_number<len(start_text)-1: #1.2 проверка не вышли ли за пределы списка текста
            text2 = f1.render(start_text[text_number+1], True, pg.Color("White")) #1.2 добавляем чтобы текст отображался попарно
            screen.blit(text2, (280, 450))  # 1отрисовка текста в заданных координатах


    if mode == "meteorites":
        ...

    if mode == "alien_scene":
        ...

    if mode == "moon":
        ...

    if mode == "final_scene":
        ...

    pg.display.flip()
    clock.tick(FPS)
