import pygame
import random
from os import path

import json #24





pygame.init()
pygame.mixer.init() #иницилизируем для работы с музыкой

bullet_sound = pygame.mixer.Sound("vyistrel-s-ruchnyim-perezaryadom.mp3")#загружаем музыку пули

# Подключение папки с картинками
img_dir = path.join(path.dirname(__file__), 'img')

# Задание констант, классов и функций
WIDTH = 480
HEIGHT = 600
FPS = 60

PLAYER_WIDTH = 50#23
PLAYER_HEIGHT = 60#23

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

light_green = (0, 255, 0)
dark_green = (0, 100, 0)

# Функция отрисовки текста
f_name = pygame.font.match_font("comic sans")

# font = pygame.font.Font(None, 40) #22


BUTTON_WIDTH = 100 #22
BUTTON_HEIGHT = 30 #22


def draw_text(screen, text, size, x, y, color):
    font = pygame.font.Font(f_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)

def gradientRect( window, left_colour, right_colour, target_rect ):#21 создание полоски здоровье c uhflbtynjv
    """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
    colour_rect = pygame.Surface( ( 2, 2 ) )                                   # tiny! 2x2 bitmap
    pygame.draw.line( colour_rect, left_colour,  ( 0,0 ), ( 0,1 ) )            # left colour line
    pygame.draw.line( colour_rect, right_colour, ( 1,0 ), ( 1,1 ) )            # right colour line
    colour_rect = pygame.transform.smoothscale( colour_rect, ( target_rect.width, target_rect.height ) )  # stretch!
    window.blit( colour_rect, target_rect )                                    # paint it


def draw_hp(screen, x, y, hp): #21 создание полоски здоровье
    if hp < 0:
        hp = 0
    LEN = 100
    HEIGHT = 10

    fill = (hp / 100) * LEN
    outline_rect = pygame.Rect(x, y, LEN, HEIGHT)

    # fill_rect = pygame.Rect(x, y, fill, HEIGHT)#старый прямоугольник здоровья
    # gradientRect(screen, (255, 255, 0), (0, 0, 255), pygame.Rect(x, y, fill, 30))#пример другого цвета
    # gradientRect(screen, (0, 255, 0), (0, 100, 0),pygame.Rect(x, y, fill, HEIGHT))  # пример зеленого цветай

    # pygame.draw.rect(screen, RED, fill_rect)#старый прямоугольник здоровья
    pygame.draw.rect(screen, WHITE, outline_rect, 2)

    gradientRect( screen, RED, BLUE, pygame.Rect( x,y, fill, HEIGHT) )#новый прямоугольник здоровья с заливкой


# def text_render(text):#22
#     return font.render(str(text), True, "black")#22



def load_image(file, width, height):#22
    image = pygame.image.load(file).convert_alpha()#22
    image = pygame.transform.scale(image, (width, height))#22
    return image

class Item:#23
    def __init__(self, name, price, file, is_using, is_bought):
        self.name = name
        self.price = price
        self.file = file
        self.image = load_image(file, PLAYER_WIDTH // 1.7, PLAYER_HEIGHT // 1.7)
        self.is_using = is_using
        self.is_bought = is_bought

        self.full_image = load_image(file, PLAYER_WIDTH, PLAYER_HEIGHT)

class Button: #22 создаем класс для кнопок
    def __init__(self, text, x, y): #22.2 конструктор класса в котором мы просим указать координаты будущей кнопки


        self.idle_image = load_image("img/button.png", BUTTON_WIDTH,BUTTON_HEIGHT) #3 обычное состояние кнопки
        self.pressed_image = load_image("img/button_clicked.png", BUTTON_WIDTH,BUTTON_HEIGHT) #3 нажатое состояние кнопки картинка чуть светлее
        self.image = self.idle_image #3 изначальное состояние кнопки кнопка в покое
        self.rect = self.image.get_rect() #3 создаем для нее рект то есть координаты
        self.rect.topleft = (x, y) #3 указываем координаты

        self.is_pressed = False #3 изначальное состояние кнопки нажата или нет

        self.text = text#22.2 текст к кнопке
        self.x=x#22.2 текст к кнопке
        self.y = y#22.2 текст к кнопке
        # self.text_rect = self.text.get_rect()  # 22.2 3 текст для кнопок
        # self.text_rect.center = self.rect.center # 22.2 текст для кнопок




    def draw(self,screen): #3 метод для отрисовки кнопки
        screen.blit(self.image, self.rect) # параметры картинка и координаты

        draw_text(screen, self.text, 22, self.rect.center[0], self.y, "black")  # #22.2 текст к кнопке

    def update(self): #3метод обновления кнопки
        mouse_pos = pygame.mouse.get_pos() #3функция проверяет позицию кнопки
        if self.rect.collidepoint(mouse_pos): #3 если позиция кнопки пересекается с мышкой
            if self.is_pressed: #3 если кнопка нажата
                self.image = self.pressed_image  #3 картинка мыши будет нажатой кнопкой
            else:
                self.image = self.idle_image #3 иначе картинка будет не нвжатой кнопкой

    def is_clicked(self, event): #3специальный метод который мы будем вызывать в евентах игры
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #3 если евент ттип это нажатая кнопка мыщи и нажата левая кнопка
            if self.rect.collidepoint(event.pos):#3 проверяем над кнопкой ли мышка
                self.is_pressed = True #3 меняем нажатая мышка на правду
                print("меню нажато")
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1: #3 для отжатой кнопки
            self.is_pressed = False



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

PADDING=5#22

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

with open("золото_колво.json", "r", encoding="utf-8") as f:#24
    data = json.load(f)#24
    print(data)#24

gold=data["золото"]


# gold =0 #20 #золото

#Загрузка музыки
pygame.mixer.music.load("музыкалеса2.mp3")
pygame.mixer.music.set_volume(0.0) #громкость  музыки 1 максимум 0 минимум
pygame.mixer.music.play()

#кнопки
button_x = WIDTH - BUTTON_WIDTH - PADDING  # 22 3 переменная для координаты x кнопки

shop_button = Button("магазин",button_x, PADDING )  #22  3 создание кнопки магазина
eat_button = Button("еда",button_x-200, PADDING )  #22  3 создание кнопки магазина



print(gold)

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
        eat_button.is_clicked(e)#22

    # Обновление

    shop_button.update()#22.2.s

    eat_button.update()  # 22 обновляем кнопку


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


                "изменяем количество золота в записанном файле"  # 24
                data["золото"] = gold
                with open("золото_колво.json", "w", encoding="utf-8") as f:  # 24
                    json.dump(data, f, ensure_ascii=False)  # 24
                    #Теория
                    #Параметр json.dump() ensure_ascii ответственен за то, экранируются ли символы при сохранении.
                    # Если он равен True, то экранируются и хранятся в виде \u000,
                    # если равен False — то символы спокойно сможет прочитать человек.
                    print(data)  # 24


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
    eat_button.draw(screen)#22

    shop_button.draw(screen)#22.2s
    pygame.display.flip()


