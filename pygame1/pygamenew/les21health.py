import pygame
import random
from os import path

pygame.mixer.init() #иницилизируем для работы с музыкой

bullet_sound = pygame.mixer.Sound("vyistrel-s-ruchnyim-perezaryadom.mp3")#загружаем музыку пули

# Подключение папки с картинками
img_dir = path.join(path.dirname(__file__), 'img')

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


def draw_hp(screen, x, y, hp): #21 создание полоски здоровье
    if hp < 0:
        hp = 0
    LEN = 100
    HEIGHT = 10

    fill = (hp / 100) * LEN
    outline_rect = pygame.Rect(x, y, LEN, HEIGHT)

    fill_rect = pygame.Rect(x, y, fill, HEIGHT)
    pygame.draw.rect(screen, RED, fill_rect)
    pygame.draw.rect(screen, WHITE, outline_rect, 2)

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
        self.health = 100 #21
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

        self.image.set_colorkey(BLACK)#19 цвет который должен исчезнуть
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
gold =0 #20 #золото

#Загрузка музыки
pygame.mixer.music.load("музыкалеса2.mp3")
pygame.mixer.music.set_volume(0.5) #громкость  музыки 1 максимум 0 минимум
pygame.mixer.music.play()


# Цикл игры
while True:

    #pygame.mixer.music.play() #музыкаиграть припораженииможновставить
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
                bullet_sound.play() #играть звук стрельбы
                player.shoot()

    # Обновление
    all_sprites.update()

    # столкновение пули и моба
    hits = pygame.sprite.groupcollide(bullets, mobs, True, True)

    if hits:
        score += 10 #20
        gold+=3 #20 #золото
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)



    # Проверка не ударил ли моб игрока
    hits = pygame.sprite.spritecollide(player, mobs, True)


    if hits:
        for hit in hits:#21 наносим урон персонажу
            player.health -= 40#21


            m = Mob()#21 создавать новых мобов при их удалении.
            all_sprites.add(m)#21 создавать новых мобов при их удалении.
            mobs.add(m)#21 создавать новых мобов при их удалении.

            if player.health <= 0:#21
                while True:


                    clock.tick(FPS)

                    for e in pygame.event.get():
                        if e.type == pygame.QUIT:
                            exit()

                    background = pygame.image.load(path.join(img_dir, "игра_оконченна.jpg")).convert() # изменение фона при игра окончена
                    background = pygame.transform.scale(background, (WIDTH, HEIGHT ))
                    screen.blit(background, background_rect)  # 19
                    all_sprites.draw(screen)

                    draw_text(screen, "GAME OVER! Your score: " + str(score), 35, 240, 300, RED)#20
                    # draw_hp(screen, 5, 5, player.health)
                    pygame.display.flip()

    # Рендеринг (отрисовка)
    screen.fill(BLACK)
    screen.blit(background, background_rect) #19

    all_sprites.draw(screen)
    draw_text(screen, "счет "+str(score), 20, 50, 20, WHITE) #19
    draw_text(screen, "золото "+str(gold), 20, 50, 40, YELLOW) #золото
    draw_hp(screen, 5, 5, player.health)

    pygame.display.flip()