import time
from sprite import *


def dialogue_mode(sprite, text):
    sprite.update()
    screen.blit(forest, (0, 0))
    screen.blit(sprite.image, sprite.rect)

    text1 = f1.render(text[text_number], True, pg.Color("white"))

    screen.blit(text1, (280, 450))
    if text_number < len(text) - 1:
        text2 = f1.render(text[text_number + 1], True, pg.Color("white"))
        screen.blit(text2, (280, 470))


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
wolf = pg.sprite.Group()
lasers = pg.sprite.Group()

girl1 = Girl1()
girl2 = Girl2()
hero = Hero()

forest = pg.image.load("background.jpg").convert()
forest = pg.transform.scale(forest, size).convert_alpha()

heart = pg.image.load("heart.png")
heart = pg.transform.scale(heart, (30, 30)).convert_alpha()
heart_count = 9 #3test

start_text = ["Вы находитесь в глубоком лесу, ",
              "окруженном густой растительностью,",
              "Наша подруга, заблудившаяся в лесу",
              "нуждается в помощи.",
              "злые волки начали нападать на нее",
              "она заблудились, пытаясь укрыться от них",
              "Отдыхающие детского лагеря Ветерок" ,
              "Долго страдали от них. ",
              "теперь и наша подруга в беде...",
              "Мы должны помочь ей.",
              "Выходим прямо сейчас.",
              "Спасибо, что не побоялись и пришли к лесу ",
              "Нам придется пробираться через камнепад",
              "Пойдемте!",
              ""]

girl2_text = ["СПАСИТЕ! Я ЕЛЕ ДЕРЖУСЬ!",
              "",
              "Волки уже начали выть совсем близко...",
              "Скоро они победят",
              "Спасите!", ]

final_text = ["Огромное вам спасибо,",
              "друзья ",
              "теперь я спасена!",
              "Я хочу отблагодарить тебя.",
              "я дарю вам целую карзину малины",
              "и мешочек мяты для чая",
              "заходите в гости",
              "будем пить чай",
              "Конец Игры",
              "Победа"]

text_number = 0
f1 = pg.font.Font("FRACTAL.otf", 25)

pg.mixer.music.load("Tense Intro.wav")
pg.mixer.music.set_volume(0.2)
pg.mixer.music.play()

laser_sound = pg.mixer.Sound("11377 ice cannon shot.wav")
win_sound = pg.mixer.Sound("Victory Screen Appear 01.wav")

while is_running:

    # СОБЫТИЯ
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                if mode == "start_scene":
                    text_number += 2
                    if text_number > len(start_text):
                        mode = "meteorites"
                        text_number = 0
                        start_time = time.time()
                if mode == "girl2_scene":
                    text_number += 2
                    if text_number > len(girl2_text):
                        mode = "wolf_buttle"
                        hero.switch_mode()
                        text_number = 0
                        start_time = time.time()
            if mode == "wolf_buttle":
                if event.key == pg.K_SPACE:
                    lasers.add(Laser(hero.rect.midtop))
                    laser_sound.play()
            if mode == "final_scene":
                text_number += 2
                if text_number >= len(final_text):
                    mode = "end"
                    text_number = 0
                    start_time = time.time()
                    is_running = False

    if mode == "start_scene":
        dialogue_mode(girl1, start_text)

    if mode == "meteorites":
        if time.time() - start_time > 5.0:
            mode = "girl2_scene"

        if random.randint(1, 30) == 1:
            meteorites.add(Meteorite())

        hero.update()
        meteorites.update()

        hits = pg.sprite.spritecollide(hero, meteorites, True)
        for hit in hits:
            heart_count -= 1
            if heart_count <= 0:
                is_running = False

        # ОТРИСОВКA
        screen.blit(forest, (0, 0))
        screen.blit(hero.image, hero.rect)
        meteorites.draw(screen)

        for i in range(heart_count):
            screen.blit(heart, (i * 30, 0))

    if mode == "girl2_scene":
        dialogue_mode(girl2, girl2_text)

    if mode == "wolf_buttle":
        if time.time() - start_time > 5.0:
            mode = "final_scene"
            pg.mixer.music.fadeout(3)
            #fadeout() используется для плавного угасания воспроизводимой музыки в течение определенного времени
            # (в данном случае, 3 секунд). В результате вызова этого метода музыка будет звучать и затем постепенно угаснет и остановится.
            win_sound.play()

        if random.randint(1, 30) == 1:
            wolf.add(Wolf())

        hero.update()
        wolf.update()
        lasers.update()

        hits = pg.sprite.spritecollide(hero, wolf, True)
        for hit in hits:
            heart_count -= 1
            if heart_count <= 0:
                is_running = False

        hits = pg.sprite.groupcollide(lasers, wolf, True, True)
        for hit in hits:
            ...

        screen.blit(forest, (0, 0))
        screen.blit(hero.image, hero.rect)
        wolf.draw(screen)
        lasers.draw(screen)

        for i in range(heart_count):
            screen.blit(heart, (i * 30, 0))

    if mode == "final_scene":
        girl2.pobeda_mode()
        dialogue_mode(girl2, final_text)

    pg.display.flip()
    clock.tick(FPS)


