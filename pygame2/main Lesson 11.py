import pygame

pygame.init()

WIDTH = 720
HEIGHT = 480

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 5
clock = pygame.time.Clock()

is_game_active = True
pattern_x = 1
speed = 10
x = 40
y = 40

while is_game_active:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    x -= speed * pattern_x
    if x == 0:
        pattern_x = -1
    if x == 100:
        pattern_x = 1
        y += speed
    for i in range(16):  # Количество противников в одном ряду
        for j in range(6):  # Количество рядов противников
            pygame.draw.rect(screen, RED, (x + i * 40, y + j * 40, 20, 20))

    pygame.display.update()
    clock.tick(FPS)