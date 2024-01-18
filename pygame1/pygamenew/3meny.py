import random
from os import path

import pygame
import pygame_menu

# Задание констант, классов и функций
WIDTH = 900
HEIGHT = 550
PADDING = 5  # 22

FPS = 60

PLAYER_WIDTH = 50  # 23
PLAYER_HEIGHT = 60  # 23
MENY_NAV_XPAD = 90  # 23magas
MENY_NAV_YPAD = 130  # 23 magas

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

light_green = (0, 255, 0)
dark_green = (0, 100, 0)

game_mode_main = "Main"
game_mode_menu = "Menu"
game_mode_shop_menu = "Shop Menu"

# Функция отрисовки текста
f_name = pygame.font.match_font("comic sans")

BUTTON_WIDTH = 100  # 22
BUTTON_HEIGHT = 30  # 22

def draw_text(screen, text, size, x, y, color):
    font = pygame.font.Font(f_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)


def gradientRect(window, left_colour, right_colour, target_rect):  # 21 создание полоски здоровье c uhflbtynjv
    """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
    colour_rect = pygame.Surface((2, 2))  # tiny! 2x2 bitmap
    pygame.draw.line(colour_rect, left_colour, (0, 0), (0, 1))  # left colour line
    pygame.draw.line(colour_rect, right_colour, (1, 0), (1, 1))  # right colour line
    colour_rect = pygame.transform.smoothscale(colour_rect, (target_rect.width, target_rect.height))  # stretch!
    window.blit(colour_rect, target_rect)  # paint it


def draw_hp(screen, x, y, hp):  # 21 создание полоски здоровье
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

    gradientRect(screen, RED, BLUE, pygame.Rect(x, y, fill, HEIGHT))  # новый прямоугольник здоровья с заливкой


def load_image(file, width, height):  # 22
    image = pygame.image.load(file).convert_alpha()  # 22
    image = pygame.transform.scale(image, (width, height))  # 22
    return image


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.bullet_sound = pygame.mixer.Sound("vyistrel-s-ruchnyim-perezaryadom.mp3")  # загружаем музыку пули
        self.img_dir = path.join(path.dirname(__file__), 'img')

        # Создаем игру и окно
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("My game")
        self.clock = pygame.time.Clock()

        # Спрайты
        self.all_sprites = pygame.sprite.Group()
        self.mobs_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        # кнопки
        button_x = WIDTH - BUTTON_WIDTH - PADDING  # 22 3 переменная для координаты x кнопки

        self.shop_button = Button("магазин", button_x, PADDING,
                                  func=None)  # 23.2 добавляем func=shop_menu_on для привязывание функции включить меню одежды, 22  3 создание кнопки магазина
        self.eat_button = Button("еда", button_x - 200, PADDING)  # 22  3 создание кнопки магазина

        # меню
        self.shop_menu = ShopMenu()  # 23/2!!!!!!!!!
        self.menu = Menu()

        # картинки
        player_img = pygame.image.load(path.join(self.img_dir, "игроксверху.png")).convert()
        player_img = pygame.transform.scale(player_img, (50, 60))

        mob_img = pygame.image.load(path.join(self.img_dir, "ghost.png")).convert()
        self.mob_img = pygame.transform.scale(mob_img, (50, 60))
        self.bullet_img = pygame.image.load(path.join(self.img_dir, "bullet.png")).convert()

        # Персонаж
        self.player = Player(player_img, self)

        self.all_sprites.add(self.player)

        # Мобы
        for i in range(15):
            m = Mob(self.mob_img)
            self.all_sprites.add(m)
            self.mobs_sprites.add(m)

        self.mode = game_mode_menu
        self.score = 0
        self.gold = 0

        # Загрузка графики
        self.background = pygame.image.load(path.join(self.img_dir, "фон2.jpg")).convert()
        self.background_rect = self.background.get_rect()

    def init_music(self):

        pygame.mixer.music.load("музыкалеса2.mp3")
        pygame.mixer.music.set_volume(0.0)  # громкость  музыки 1 максимум 0 минимум
        pygame.mixer.music.play()

    def run(self):
        self.init_music()

        while True:
            # pygame.mixer.music.play() #музыкаиграть припораженииможновставить
            # Контролируем ФПС
            self.clock.tick(FPS)

            self.event_process()
            self.menu_process()
            self.game_process()
            self.shop_process()

            pygame.display.flip()

    def event_process(self):#процесс проверяет не нажали ли кнопку
        for e in pygame.event.get():
            if self.mode == game_mode_main:
                if e.type == pygame.QUIT:  # Если нажали на крестик
                    self.mode = game_mode_menu
                    continue

                if e.type == pygame.KEYDOWN:  # 23.2 делаем выход на клавишу ESCAPE в цикл игры
                    if e.key == pygame.K_ESCAPE:  # 23.2
                        self.mode = game_mode_menu
                    if e.key == pygame.K_SPACE:
                        self.bullet_sound.play()  # играть звук стрельбы
                        self.player.shoot()
                    continue

                self.eat_button.is_clicked(e)  # 23
                self.shop_button.is_clicked(e)  # 22

            if self.mode == game_mode_menu:  # 23
                self.shop_menu.is_clicked(e)  # 23

    def shop_process(self):
        if self.mode == game_mode_shop_menu:  # 23.2 добавляем отрисовку меню магазина
            self.shop_menu.draw(self.screen)
            print("магазин переключено")  # 23.2

    def game_process(self):
        if self.mode == game_mode_main:
            print(123)
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:  # 23.2 делаем выход на клавишу ESCAPE в цикл игры
                    if e.key == pygame.K_ESCAPE:  # 23.2
                        self.mode = "Main"  # 23.2
                # Если событие, которое поймал компьютер - это нажатие на клавишу

            # Обновление

            self.shop_button.update()  # 22.2.s
            self.eat_button.update()  # 22 обновляем кнопку
            self.all_sprites.update()
            self.shop_menu.update()  # 23 обновляем shop meni

            # столкновение пули и моба
            hits = pygame.sprite.groupcollide(self.bullets, self.mobs_sprites, True, True)

            if hits:
                self.score += 10  # 20
                self.gold += 3  # 20 #золото
                m = Mob(self.mob_img)
                self.all_sprites.add(m)
                self.mobs_sprites.add(m)

            # Проверка не ударил ли моб игрока
            hits = pygame.sprite.spritecollide(self.player, self.mobs_sprites, True)

            if hits:
                for hit in hits:  # 21 наносим урон персонажу
                    self.player.health -= 40  # 21

                    m = Mob(self.mob_img)  # 21 создавать новых мобов при их удалении.
                    self.all_sprites.add(m)  # 21 создавать новых мобов при их удалении.
                    self.mobs_sprites.add(m)  # 21 создавать новых мобов при их удалении.

                    if self.player.health <= 0:  # 21
                        while True:

                            self.clock.tick(FPS)

                            for e in pygame.event.get():
                                if e.type == pygame.QUIT:
                                    exit()

                            background = pygame.image.load(
                                path.join(self.img_dir,
                                          "игра_оконченна.jpg")).convert()  # изменение фона при игра окончена
                            background = pygame.transform.scale(background, (WIDTH, HEIGHT))
                            self.screen.blit(background, self.background_rect)  # 19
                            self.all_sprites.draw(self.screen)

                            draw_text(self.screen, "GAME OVER! Your score: " + str(self.score), 35, 240, 300, RED)  # 20
                            # draw_hp(screen, 5, 5, player.health)
                            pygame.display.flip()

            # Рендеринг (отрисовка)
            self.screen.fill(BLACK)
            self.screen.blit(self.background, self.background_rect)  # 19

            self.all_sprites.draw(self.screen)
            draw_text(self.screen, "счет " + str(self.score), 20, 50, 20, WHITE)  # 19
            draw_text(self.screen, "золото " + str(self.gold), 20, 50, 40, YELLOW)  # золото
            draw_hp(self.screen, 5, 5, self.player.health)
            self.eat_button.draw(self.screen)  # 22

            self.shop_button.draw(self.screen)  # 22.2s

    def menu_process(self):
        if self.mode == game_mode_menu:
            self.menu.run()
            self.mode = game_mode_main
            # if e.type == pygame.KEYDOWN:  # 23.2 делаем выход на клавишу ESCAPE в цикл игры
            #     if e.key == pygame.K_ESCAPE:  # 23.2
            #         self.mode = "Main"


class Item:  # 23классс педмета
    def __init__(self, name, price, file):
        self.name = name
        self.price = price
        self.file = file
        self.image = load_image(file, PLAYER_WIDTH * 2,
                                PLAYER_HEIGHT * 2)  # 23 magas картинка для меню чуть меньшего размера чем полная картинка // 1.4 если игрок большой
        self.full_image = load_image(file, PLAYER_WIDTH, PLAYER_HEIGHT)  # 23 полная картинка предмета для игры

        self.is_using = False
        self.is_bought = False


class ShopMenu:  # ! 23классс менюодежды
    def __init__(self):  # 23 game ссылка на сам класс игры чтобы загружать деньги потом
        # self.game = game  # 23
        self.menu_page = load_image("img/menu/menu_page.png", WIDTH, HEIGHT)

        self.bottom_label_off = load_image("images/menu/bottom_label_off.png", WIDTH,
                                           HEIGHT)  # 23 лэйблы обазначающие купена вещь или надета
        self.bottom_label_on = load_image("images/menu/bottom_label_on.png", WIDTH, HEIGHT)
        self.top_label_off = load_image("images/menu/top_label_off.png", WIDTH, HEIGHT)
        self.top_label_on = load_image("images/menu/top_label_on.png", WIDTH, HEIGHT)

        self.items = [Item("cиняя футболка", 100, "img/items/синяя_футболка.png"),  # 23список всех предметов в магазине
                      Item("пистолет", 100, "img/items/пистолетпредмет.png"),
                      Item("пистолет", 700, "img/items/паук-removebg-preview (1).png")]  # 23

        self.current_item = 0  # индекс текущего предмета
        self.item_rect = self.items[0].image.get_rect()  # берем рект картинки предмета чтобы определить координаты
        self.item_rect.center = (WIDTH // 2, HEIGHT // 2)  # распологаем посередине экрана
        self.next_button = Button("Вперед", WIDTH - MENY_NAV_XPAD - BUTTON_WIDTH,
                                  HEIGHT - MENY_NAV_YPAD - BUTTON_HEIGHT,
                                  width=int(BUTTON_WIDTH // 1.2), height=int(BUTTON_HEIGHT // 1.2),
                                  func=self.to_next)  # 23 прикрепляем будущую функцию для перелистывания намечаем что она должна существовать ниже
        # 23кнопка вперед создать выше  в игреMENY_NAV_XPAD MENY_NAV_YPAD
        # 23от всей шириныэкрана отнимаем отступ и саму ширину кнопки

    def to_next(self):  # 23 наметка позже напишем

        if self.current_item != len(self.items) - 1:  # 23 проверяем что предмет не последний
            self.current_item += 1  # 23 переключаем на следующий предмет
        else:
            self.current_item = 0  # если хотим сделать круговое переключение

    def update(self):  # 23 добавляем функцию для будующих многих кнопок обновления
        self.next_button.update()

    def is_clicked(self, event):  # 23 добавляем функцию для будующих многих кнопок кликнуто
        self.next_button.is_clicked(event)  # получает в качестве аргумента событие

    def draw(self, screen):  # 23 добавляем функцию для отрисовки с параметром экран
        screen.blit(self.menu_page, (0, 0))  # 23 рисуем в нулевых оординатах так как картинка занимает все место

        screen.blit(self.items[self.current_item].image,
                    self.item_rect)  # 23 отрисовываем сам айтем берем весь список предметов выбираем из него текущий по индексу. Берем его картинку self.item rect берем в ачестве коорлинат

        if self.items[self.current_item].is_bought:  # 23 проверяем куплен ли предмет если да
            screen.blit(self.bottom_label_on, (0, 0))  # то отрисовывем боттом лэйбл он
        else:
            screen.blit(self.bottom_label_off, (0, 0))  # 23 то отрисовывем боттом лэйбл off не активный лэйбл
        if self.items[self.current_item].is_using:  # 23 используется ли сейчас предмет
            screen.blit(self.top_label_on, (0, 0))  # 23 то отрисовывем топ лэйбл on
        else:
            screen.blit(self.top_label_off, (0, 0))  # 23 то отрисовывем топ лэйбл off
        self.next_button.draw(screen)  # 23 отрисовать кнопку "следующий"

        # screen.blit(self.price_text, self.price_text_rect)
        # screen.blit(self.name_text, self.name_text_rect)
        # screen.blit(self.use_text, self.use_text_rect)
        # screen.blit(self.buy_text, self.buy_text_rect)


class Button:  # 22 создаем класс для кнопок
    def __init__(self, text, x, y, width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                 func=None):  # 22.2 конструктор класса в котором мы просим указать координаты будущей кнопки
        self.func = func  # 23
        self.idle_image = load_image("img/button.png", BUTTON_WIDTH, BUTTON_HEIGHT)  # 3 обычное состояние кнопки
        self.pressed_image = load_image("img/button_clicked.png", BUTTON_WIDTH,
                                        BUTTON_HEIGHT)  # 3 нажатое состояние кнопки картинка чуть светлее
        self.image = self.idle_image  # 3 изначальное состояние кнопки кнопка в покое
        self.rect = self.image.get_rect()  # 3 создаем для нее рект то есть координаты
        self.rect.topleft = (x, y)  # 3 указываем координаты

        self.is_pressed = False  # 3 изначальное состояние кнопки нажата или нет

        self.text = text  # 22.2 текст к кнопке
        self.x = x  # 22.2 текст к кнопке
        self.y = y  # 22.2 текст к кнопке
        # self.text_rect = self.text.get_rect()  # 22.2 3 текст для кнопок
        # self.text_rect.center = self.rect.center # 22.2 текст для кнопок

    def draw(self, screen):  # 3 метод для отрисовки кнопки
        screen.blit(self.image, self.rect)  # параметры картинка и координаты

        draw_text(screen, self.text, 22, self.rect.center[0], self.y, "black")  # #22.2 текст к кнопке

    def update(self):  # 3метод обновления кнопки
        mouse_pos = pygame.mouse.get_pos()  # 3функция проверяет позицию кнопки
        if self.rect.collidepoint(mouse_pos):  # 3 если позиция кнопки пересекается с мышкой
            if self.is_pressed:  # 3 если кнопка нажата
                self.image = self.pressed_image  # 3 картинка мыши будет нажатой кнопкой
            else:
                self.image = self.idle_image  # 3 иначе картинка будет не нвжатой кнопкой

    def is_clicked(self, event):
        # print(self.text)  # 3специальный метод который мы будем вызывать в евентах игры
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 3 если евент ттип это нажатая кнопка мыщи и нажата левая кнопка
            if self.rect.collidepoint(event.pos):  # 3 проверяем над кнопкой ли мышка
                self.is_pressed = True  # 3 меняем нажатая мышка на правду
                print("кнопка нажата")
                self.func()  ################ CALL THE FUNCTION ##############################
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # 3 для отжатой кнопки
            self.is_pressed = False


class Menu:
    def __init__(self):
        background_image = pygame_menu.BaseImage(
            image_path="background.jpg"
        )
        mytheme = pygame_menu.Theme(background_color=background_image,  # transparent background
                                    title_background_color=(4, 47, 126),
                                    title_font_shadow=True,
                                    widget_padding=25,
                                    widget_font_color=(255, 0, 0),  # Red font color for widgets
                                    title_font_color=(0, 255, 0),  # Green font color for the title
                                    selection_color=(0, 0, 255)  # цвет при наведении мыши
                                    )

        self.surface = pygame.display.set_mode((900, 550))
        self.menu = pygame_menu.Menu(
            height=550,
            width=900,
            # theme=pygame_menu.themes.THEME_SOLARIZED,
            title="меню",
            theme=mytheme,
        )

        self.menu.add.button("Играть", self.start_game)
        self.menu.add.button("Выйти", quit)  # изменяем функцию на просто выход
        self.menu.add.button("Магазин", self.magas)

    def start_game(self):
        self.menu.disable()

    def magas(self):
        ...

    def run(self):
        self.menu.enable()
        self.menu.mainloop(self.surface)


class Player(pygame.sprite.Sprite):
    def __init__(self, player_img, game: Game):
        pygame.sprite.Sprite.__init__(self)
        self.LinkGame = game

        self.image = player_img
        self.image.set_colorkey(BLACK)  # 19 цвет который должен исчезнуть

        # self.image.fill(GREEN)
        self.rect = self.image.get_rect()

        # self.rect.width=self.rect.width-20   #изменить размер прямоугольника изображения скелет
        # self.rect.height = self.rect.height - 30 #изменить размер прямоугольника прямоугольник изображения скелет

        print(self.rect)

        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT - 50
        self.speedx = 0
        # TODO
        self.health = 100  # 21

    def update(self):
        self.speedx = 0
        self.speedy = 0  # y игрока
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
        bullet = Bullet(self.rect.x + 35, self.rect.y, self.LinkGame.bullet_img)
        self.LinkGame.all_sprites.add(bullet)
        self.LinkGame.bullets.add(bullet)


class Mob(pygame.sprite.Sprite):
    def __init__(self, mob_img):
        pygame.sprite.Sprite.__init__(self)

        self.image = mob_img  # 19

        self.image.set_colorkey(BLACK)  # 19 цвет который должен исчезнуть
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
    def __init__(self, x, y, bullet_img):
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


game = Game()
game.run()