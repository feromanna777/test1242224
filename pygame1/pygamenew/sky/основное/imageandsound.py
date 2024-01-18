import pygame
import random
pygame.mixer.init()

# Задание констант, классов и функций
WIDTH = 480
HEIGHT = 600
FPS = 1

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

# Функция изменения размера
# def change_size(image):
#     image = pygame.image.load(image)
#     image = pygame.transform.scale(image, (100, 100))
#     return image
#
# character=change_size("picanime1.png")
character_rect=character.get_rect(center=(WIDTH//2, HEIGHT//2))
# character_rect.center=(WIDTH//2, HEIGHT//2)

character2=pygame.transform.flip(character, True, False)


pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.1)

# Цикл игры
while True:
    pygame.mixer.music.play()
    # Контролируем ФПС
    clock.tick(FPS)

    # Ввод события (нажатие клавиш, нажатия мыши)
    for e in pygame.event.get():
        # Если нажали на крестик
        if e.type == pygame.QUIT:
            exit()

    # Обновление

    # Рендеринг (отрисовка)
    screen.fill(pygame.Color(99, 124, 171))
    screen.blit(background, (-150, 0))
    screen.blit(character2, (0,200))
    screen.blit(character2, character_rect)


    pygame.display.flip()