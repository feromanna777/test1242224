import pygame
import random
pygame.mixer.init()
# Задание констант, классов и функций
WIDTH = 480
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Создаем игру и окно
pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()

background=pygame.image.load("../лес_полныйпроект/complete/background.jpg")
background=pygame.transform.scale(background, (WIDTH+300, HEIGHT))

character=pygame.image.load("picanime1.png")
character=pygame.transform.scale(character, (400, 400))

small_rect=pygame.Rect(0,0,20,20)


# Функция изменения размера
# def change_size(image):
#     image = pygame.image.load(image)
#     image = pygame.transform.scale(image, (100, 100))
#     return image
#
# character=change_size("picanime1.png")
character_rect=character.get_rect(center=(WIDTH//2, HEIGHT//2))
# character_rect.center=(WIDTH//2, HEIGHT//2)




pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.01)

pygame.mixer.music.play()

import pygame as pg


# def move(starship_rect, events):
#     for event in events:
#         if e.type == pygame.KEYDOWN:
#             if e.key == pygame.K_LEFT:
#                 starship_rect.x-=1
#             if e.key == pygame.K_RIGHT:
#                 starship_rect.x+=1
#             if e.key == pygame.K_UP:
#                 starship_rect.y+=1
#             if e.key == pygame.K_DOWN:
#                 starship_rect.y-=1
#     return starship_rect

# Цикл игры
while True:



    # Ввод события (нажатие клавиш, нажатия мыши)
    for e in pygame.event.get():
        # Если нажали на крестик
        if e.type == pygame.QUIT:
            exit()

        if e.type==pygame.MOUSEBUTTONDOWN: #код распазнает единичное нажатие
            if e.button==1:
                print(e.pos)
                small_rect.center=e.pos

        # if e.type == pygame.KEYDOWN:
        #     if e.key == pygame.K_LEFT:
        #         character_rect.x-=10
        #     if e.key == pygame.K_RIGHT:
        #         character_rect.x+=10





    keys=pygame.key.get_pressed()

    # print(keys)
    print(type(keys))
    if keys[pygame.K_LEFT]:
        character_rect.x -= 10
    if keys[pygame.K_RIGHT]:
        character_rect.x += 10
    if keys[pygame.K_UP]:
        character_rect.y -= 10
    if keys[pygame.K_DOWN]:
        character_rect.y += 10


    # Обновление


    # распазнает зажатие
    mouse_pos=pygame.mouse.get_pos()  # функция возращает кортеж
    mouse_keys=pygame.mouse.get_pressed()    # функция возращает словарь
    if mouse_keys[0]: #начинаем с 0 0 это левая кнопка мыши 1 калесико 2 правая
        character_rect.center=mouse_pos

    # Рендеринг (отрисовка)
    screen.fill(pygame.Color(99, 124, 171))
    screen.blit(background, (-150, 0))
    screen.blit(character, character_rect)

    pygame.draw.rect(screen,RED,small_rect)
    pygame.display.flip()
    # Контролируем ФПС
    clock.tick(FPS)

#