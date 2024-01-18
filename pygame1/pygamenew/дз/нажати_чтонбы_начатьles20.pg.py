import pygame
import random
from os import path
import pygame, random, sys
from pygame.locals import *




# Подключение папки с картинками
img_dir = path.join(path.dirname(__file__), '../img')

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


# Функция отрисовки текста
f_name = pygame.font.match_font("comic sans")
#нажмит ечтобы начать играть
def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == QUIT:
    #             terminate()
    #         if event.type == KEYDOWN:
    #
    #             if event.key == K_ESCAPE: # Нажатие ESC осуществляет выход.
    #                 terminate()
    #             return

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:

                if event.key == K_ESCAPE: # Нажатие ESC осуществляет выход.
                    terminate()
                if event.key == K_RETURN:

                    return


def draw_text(screen, text, size, x, y, color):
    font = pygame.font.Font(f_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(BLACK)  #19 цвет который должен исчезнуть

        # self.image.fill(GREEN)
        self.rect = self.image.get_rect()


        # self.rect.width=self.rect.width-20   #изменить размер прямоугольника изображения скелет
        # self.rect.height = self.rect.height - 30 #изменить размер прямоугольника прямоугольник изображения скелет

        print(self.rect)


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
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.x + 35, self.rect.y)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = mob_img #19

        self.image.set_colorkey(BLACK)#19 цает который должен исчезнуть
        # self.image.fill(RED)
        self.rect = self.image.get_rect()

        # self.rect.width = self.rect.width - 20  # изменить прямоугольник изображения скелет
        # self.rect.height = self.rect.height - 30  # изменить прямоугольник изображения скелет

        self.rect.x = random.randint(30, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speedy = random.randint(1, 4)




    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randint(30, WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speedy = random.randint(1, 4)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((10, 20))
        # self.image.fill(YELLOW)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # если пуля зайдет за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()


# Создаем игру и окно
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()


# Загрузка графики
background = pygame.image.load(path.join(img_dir, "фон2.jpg")).convert()
background_rect = background.get_rect()

# background=pygame.transform.scale(background, (WIDTH, HEIGHT+300)) #не обязательно но можно

player_img = pygame.image.load(path.join(img_dir, "игроксверху.png")).convert()
player_img=pygame.transform.scale(player_img, (50, 60))

mob_img = pygame.image.load(path.join(img_dir, "ghost.png")).convert()
mob_img = pygame.transform.scale(mob_img, (50, 60))
bullet_img = pygame.image.load(path.join(img_dir, "bullet.png")).convert()



# Персонаж
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Мобы
mobs = pygame.sprite.Group()
for i in range(15):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

# Пули
bullets = pygame.sprite.Group()

# Счет
score = 0 #20
gold =0 #20






# Вывод начального экрана.
screen.fill(BLUE)
draw_text(screen, 'Нажмите клавишу для начала игры' , 15, 240, 400, WHITE)#19('Ловкач', font, windowSurface, (WIDTH / 3), (HEIGHT / 3))
draw_text(screen, "ловкач" , 35, 240, 200, WHITE)#19('Нажмите клавишу для начала игры', font, windowSurface, (WINDOWWIDTH / 5) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()


while True:
    print("Начальные настройки")
# Настройка начала игры.
    # Создаем игру и окно



    # Персонаж
    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    # Мобы
    mobs = pygame.sprite.Group()
    for i in range(15):
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    # Пули
    bullets = pygame.sprite.Group()

    # Счет
    score = 0  # 20
    gold = 0  # 20

    while True:
        print("игра началась")


        # Ввод события (нажатие клавиш, нажатия мыши)
        for e in pygame.event.get():
            # Если нажали на крестик
            if e.type == pygame.QUIT:
                exit()
            # Если событие, которое поймал компьютер - это нажатие на клавишу
            if e.type == pygame.KEYDOWN:
                # Если эта клавиша – пробел
                if e.key == pygame.K_SPACE:
                    player.shoot()

        # Обновление
        all_sprites.update()

        # столкновение пули и моба
        hits = pygame.sprite.groupcollide(bullets, mobs, True, True)

        if hits:
            score += 10 #20
            gold+=3 #20
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)

            # Проверка не ударил ли моб игрока
        hits = pygame.sprite.spritecollide(player, mobs, True)


        if hits:
            break

            # while True:
            #     clock.tick(FPS)
            #     for e in pygame.event.get():
            #         if e.type == pygame.QUIT:
            #             exit()
            #     screen.fill(BLACK)
            #     screen.blit(background, background_rect)  # 19
            #     all_sprites.draw(screen)
            #
            #     draw_text(screen, "GAME OVER! Your score: " + str(score), 35, 240, 300, WHITE)#19
            #
            #

        # Рендеринг (отрисовка)
        screen.fill(BLACK)
        screen.blit(background, background_rect) #19
        all_sprites.draw(screen)
        draw_text(screen, "счет "+str(score), 20, 30, 20, WHITE) #19
        draw_text(screen, str(gold), 20, 30, 40, YELLOW)
        pygame.display.flip()

        # Контролируем ФПС
        clock.tick(FPS)

    screen.fill(BLUE)
    draw_text(screen, 'Нажмите клавишу для начала игры', 15, 240, 400, WHITE)  # 19('Ловкач', font, windowSurface, (WIDTH / 3), (HEIGHT / 3))
    draw_text(screen, "игра окончена", 35, 240, 200,WHITE)  # 19('Нажмите клавишу для начала игры', font, windowSurface, (WINDOWWIDTH / 5) - 30, (WINDOWHEIGHT / 3) + 50)
    pygame.display.update()
    waitForPlayerToPressKey()




    # pygame.display.flip()

