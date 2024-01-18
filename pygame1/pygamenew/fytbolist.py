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

x = 100
y = 500

y_ball = 570
y_ball_speed=0
x_ball=x
# x_ball_speed=x


x_a = random.randint(1, WIDTH)
# Цикл игры
ball_throwed=False


f1 = pygame.font.Font(None, 100)   #для текста

mishen=pygame.image.load("кегли1.png")


mishen=pygame.transform.scale(mishen, (70, 70))
mishen_rect=mishen.get_rect(center=(WIDTH//2, HEIGHT//2))


while True:
    # Контролируем ФПС
    clock.tick(FPS)

    # Ввод события (нажатие клавиш, нажатия мыши)
    for e in pygame.event.get():
        # Если нажали на крестик
        if e.type == pygame.QUIT:
            exit()

    # Обновление
    x += 2
    y_ball=y_ball+y_ball_speed
    if not ball_throwed:

        x_ball = x
    if x > 300:
        x = 300
        # y_ball -= 2



    if e.type == pygame.MOUSEBUTTONDOWN:
        if e.button == 1:

            y_ball_speed = - 2
            x_ball = x
            ball_throwed = True


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

    # мяч
    pygame.draw.circle(screen, BLACK, (x_ball, y_ball), 15)

    # мишень
    # pygame.draw.circle(screen, RED, (x_a, 20), 15)
    mishen_rect.centerx=x_a
    mishen_rect.centery=20
    # screen.blit(mishen, (x_a, 20))
    screen.blit(mishen, mishen_rect)

    if y_ball < 20:
        # if x_a == x:
        if x_ball-80<x_a<x_ball+80:
            mishen = pygame.image.load("кегли2.png")
            mishen = pygame.transform.scale(mishen, (70, 70))
            print("ты победил!")
            text1 = f1.render("Ты победил", True, pygame.Color("Blue"))  # для текста
            screen.blit(text1, (100, 200))  # для отрисовки текста

    pygame.display.flip()