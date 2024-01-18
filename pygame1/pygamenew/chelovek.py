import pygame
import random

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
speed_x=2
x = 100
y = 500




y_ball = 550
x_a = random.randint(1, WIDTH)

# Цикл игры
while True:
    # Контролируем ФПС
    clock.tick(FPS)

    # Ввод события (нажатие клавиш, нажатия мыши)
    for e in pygame.event.get():
        # Если нажали на крестик
        if e.type == pygame.QUIT:
            exit()

    # Обновление
    x += speed_x

    if x > 300:
        x = 300
        y_ball-=2
    #     speed_x=-2
    # x += speed_x
    # if x < 0:
    #
    #     speed_x = 2

    if y_ball == 20:

        if x-30<x_a<x+30:
            print("ты победил!")


     # Рендеринг (отрисовка)
    screen.fill(WHITE)
    # тело
    pygame.draw.line(screen, RED, (x, y), (x, y + 50), 10)
    # голова
    pygame.draw.circle(screen, BLACK, (x, y), 15)
    # руки
    pygame.draw.line(screen, RED, (x, y + 15), (x - 30, y + 20), 5)
    pygame.draw.line(screen, RED, (x, y + 15), (x + 30, y + 20), 5)
    # ноги
    pygame.draw.line(screen, BLUE, (x, y + 50), (x - 10, y + 80), 10)
    pygame.draw.line(screen, BLUE, (x, y + 50), (x + 10, y + 80), 10)
    #мяч
    pygame.draw.circle(screen, BLUE, (x, y_ball), 15)
    #мишень
    pygame.draw.circle(screen, RED, (x_a, 20), 15)







    pygame.display.flip()