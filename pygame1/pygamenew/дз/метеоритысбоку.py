import pygame
import random
from os import path

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


        self.rect.x = 5
        self.rect.y = HEIGHT//2
        self.speedx = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0 #y игрока
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy = -4
        if keystate[pygame.K_DOWN]:
            self.speedy = 4

        self.rect.y += self.speedy

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

        self.rect.x = random.randint(WIDTH - self.rect.width, WIDTH+100)
        self.rect.y = random.randint(30, HEIGHT-40)
        self.speedx = random.randint(1, 2)




    def update(self):
        global score
        self.rect.x -= self.speedx
        if self.rect.left <0:
            score+=3
            self.rect.x = random.randint(WIDTH - self.rect.width, WIDTH + 100)
            self.rect.y = random.randint(30, HEIGHT - 40)
            self.speedx = random.randint(1, 2)

score = 0 #20
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
for i in range(7):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

# Пули
bullets = pygame.sprite.Group()

# Счет

gold =0 #20

# Цикл игры
while True:
    # Контролируем ФПС
    clock.tick(FPS)

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
        while True:
            clock.tick(FPS)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    exit()
            screen.fill(BLACK)
            screen.blit(background, background_rect)  # 19
            all_sprites.draw(screen)

            draw_text(screen, "GAME OVER! Your score: " + str(score), 35, 240, 300, WHITE)#19

            pygame.display.flip()

    # Рендеринг (отрисовка)
    screen.fill(BLACK)
    screen.blit(background, background_rect) #19
    all_sprites.draw(screen)
    draw_text(screen, "счет "+str(score), 20, 30, 20, WHITE) #19
    draw_text(screen, str(gold), 20, 30, 40, YELLOW)

    pygame.display.flip()