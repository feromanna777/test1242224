# import pygame
# import sys
# import math
#
# # Инициализация Pygame
# pygame.init()
#
# # Размеры окна
# width, height = 800, 600
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Рисование фигур")
#
# # Цвета
# red = (255, 0, 0)
# white = (255, 255, 255)
#
# # Функция для рисования красного пятиугольника
# def draw_pentagon(surface, color, center, size):
#     angle = 360 / 5
#     points = []
#     for i in range(5):
#         x = center[0] + size * math.cos(math.radians(i * angle))
#         y = center[1] + size * math.sin(math.radians(i * angle))
#         points.append((x, y))
#     pygame.draw.polygon(surface, color, points)
#
# # Функция для рисования трех кругов
# def draw_circles(surface, color, center, radius, distance):
#     for i in range(3):
#         x = center[0] + i * distance
#         y = center[1]
#         pygame.draw.circle(surface, color, (x, y), radius)
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     screen.fill(white)
#
#     # Рисуем красный пятиугольник
#     pentagon_center = (width // 2, height // 2)
#     pentagon_size = 100
#     draw_pentagon(screen, red, pentagon_center, pentagon_size)
#
#     # Рисуем трое кругов
#     circle_radius = 30
#     circle_distance = 150
#     circle_center = (width // 2 - circle_distance, height // 2)
#     draw_circles(screen, red, circle_center, circle_radius, circle_distance)
#
#     pygame.display.flip()
#
# # Завершение работы Pygame
# pygame.quit()
# sys.exit()



# "2"
# import pygame
# import sys
#
# # Инициализация Pygame
# pygame.init()
#
# # Размеры окна
# width, height = 800, 600
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Три красных круга")
#
# # Цвета
# red = (255, 0, 0)
# white = (255, 255, 255)
#
# # Функция для рисования круга
# def draw_circle(surface, color, center, radius):
#     pygame.draw.circle(surface, color, center, radius)
#
# # Размеры и расстояние между кругами
# circle_radius = 50
# distance_between_circles = 200
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     screen.fill(white)
#
#     # Рисуем первый круг
#     circle1_center = (width // 4, height // 2)
#     draw_circle(screen, red, circle1_center, circle_radius)
#
#     # Рисуем второй круг
#     circle2_center = (width // 2, height // 2)
#     draw_circle(screen, red, circle2_center, circle_radius)
#
#     # Рисуем третий круг
#     circle3_center = (3 * width // 4, height // 2)
#     draw_circle(screen, red, circle3_center, circle_radius)
#
#     pygame.display.flip()
#
# # Завершение работы Pygame
# pygame.quit()
# sys.exit()



"3"
import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Три красных круга")

# Цвета
red = (255, 0, 0)
white = (255, 255, 255)

# Функция для рисования круга
def draw_circle(surface, color, center, radius):
    pygame.draw.circle(surface, color, center, radius)

# Размеры и расстояние между кругами
circle_radius = 50
distance_between_circles = 200

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    # Рисуем первый круг
    circle1_center = (100, 400)
    draw_circle(screen, red, circle1_center, circle_radius)

    # Рисуем второй круг
    circle2_center = (250, 400)
    draw_circle(screen, red, circle2_center, circle_radius)

    # Рисуем третий круг
    circle3_center = (400, 400)
    draw_circle(screen, red, circle3_center, circle_radius)

    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
sys.exit()