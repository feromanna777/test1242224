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

pygame.init()

f1 = pygame.font.Font(None, 100)   #для текста

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT - 50
        self.speedx = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0 #y игрока
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -4
        if keystate[pygame.K_RIGHT]:
            self.speedx = 4

        self.rect.x += self.speedx

        if self.rect.right > WIDTH:
            self.rect.right = 0
        if self.rect.left < 0:
            self.rect.left = 0






screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()

player = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
# Цикл игры

# Переменная для отслеживания клика мышью
mouse_clicked = False


while True:
    # Контролируем ФПС
    clock.tick(FPS)

    # Ввод события (нажатие клавиш, нажатия мыши)
    for e in pygame.event.get():
        # Если нажали на крестик
        if e.type == pygame.QUIT:
            exit()

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicked = True
            m = True
        if e.type == pygame.MOUSEBUTTONUP:
            mouse_clicked = False

    all_sprites.update()

    # Проверка времени отображения надписи

    # Рендеринг (отрисовка)
    screen.fill(BLACK)
    if mouse_clicked == True:
        text1 = f1.render("Привет", True, pygame.Color("Blue"))
        screen.blit(text1, (100, 200))  # для отрисовки текста



    all_sprites.draw(screen)
    pygame.display.flip()
