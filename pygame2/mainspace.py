import random
import time

import pygame

pygame.init()


def call_menu(sr, fps):
    menu = True
    selected = "start"
    while menu:
        sr.fill(BLUE)
        do_once = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if selected == "start" and event.key == pygame.K_UP and do_once:
                    selected = "quit"
                    do_once = False
                if selected == "settings" and event.key == pygame.K_UP and do_once:
                    selected = "start"
                    do_once = False
                if selected == "quit" and event.key == pygame.K_UP and do_once:
                    selected = "settings"
                    do_once = False
                if selected == "start" and event.key == pygame.K_DOWN and do_once:
                    selected = "settings"
                    do_once = False
                if selected == "settings" and event.key == pygame.K_DOWN and do_once:
                    selected = "quit"
                    do_once = False
                if selected == "quit" and event.key == pygame.K_DOWN and do_once:
                    selected = "start"
                    do_once = False

                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        return True
                    elif selected == "settings":
                        call_settings(sr, fps)
                    else:
                        return False

        f1 = pygame.font.SysFont("Comic Sans MS", 110)
        title = f1.render("Space war", True, BLACK)
        f2 = pygame.font.SysFont("Comic Sans MS", 75)
        if selected == "start":
            start = f2.render("START", True, WHITE)
        else:
            start = f2.render("START", True, BLACK)

        if selected == "settings":
            settings = f2.render("SETTINGS", True, WHITE)
        else:
            settings = f2.render("SETTINGS", True, BLACK)

        if selected == "quit":
            quit = f2.render("QUIT", True, WHITE)
        else:
            quit = f2.render("QUIT", True, BLACK)

        sr.blit(title, (WIDTH / 2 - 300, 10))
        sr.blit(start, (WIDTH / 2 - 50, 170))
        sr.blit(settings, (WIDTH / 2 - 50, 260))
        sr.blit(quit, (WIDTH / 2 - 50, 350))

        pygame.display.update()
        clock.tick(fps)


def call_settings(sr, fps):
    settings = True
    selected = 'volume'
    size = 0.3
    while settings:
        sr.fill(BLUE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if selected == "volume" and event.key == pygame.K_DOWN:
                    selected = "quit"
                if selected == "quit" and event.key == pygame.K_UP:
                    selected = "volume"

                if event.key == pygame.K_LEFT:
                    size -= 0.1
                    Settings.set_music_volume(size)
                    Settings.set_shoot_volume(size - 0.1)
                    Settings.set_explosion_volume(size - 0.2)
                if event.key == pygame.K_RIGHT:
                    size += 0.1
                    Settings.set_music_volume(size)
                    Settings.set_shoot_volume(size - 0.1)
                    Settings.set_explosion_volume(size - 0.2)

                if event.key == pygame.K_RETURN:
                    return False

        f1 = pygame.font.SysFont("Comic Sans MS", 110)
        title = f1.render("Settings", True, BLACK)
        f2 = pygame.font.SysFont("Comic Sans MS", 75)
        if selected == "volume":
            volume = f2.render("VOLUME", True, WHITE)
        else:
            volume = f2.render("VOLUME", True, BLACK)

        if selected == "quit":
            quit = f2.render("QUIT", True, WHITE)
        else:
            quit = f2.render("QUIT", True, BLACK)

        sr.blit(title, (WIDTH / 2 - 300, 10))
        sr.blit(volume, (WIDTH / 2 - 50, 170))
        pygame.draw.rect(sr, RED, (WIDTH / 2 - 50, 300, size * 100, 20))
        sr.blit(quit, (WIDTH / 2 - 50, 360))

        pygame.display.update()
        clock.tick(fps)


class Settings:
    is_music_active = True
    shoot_sound = None
    explosion_sound = None
    score = 0
    is_game_active = True

    @classmethod
    def draw_score(cls, screen, x, y, color):
        f = pygame.font.Font(None, 36)
        score_text = f.render(str(Settings.score), True, color)
        screen.blit(score_text, (x, y))

    @classmethod
    def draw_text(cls, screen, x, y, color, size, text):
        f = pygame.font.Font(None, size)
        score_text = f.render(text, True, color)
        screen.blit(score_text, (x, y))

    @classmethod
    def load_and_start_music(cls, music_path):
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play()

    @classmethod
    def set_music_volume(cls, volume):
        pygame.mixer.music.set_volume(volume)

    @classmethod
    def pause_or_resume_music(cls):
        if Settings.is_music_active:
            pygame.mixer.music.pause()
            Settings.is_music_active = False
        else:
            pygame.mixer.music.unpause()
            Settings.is_music_active = True

    @classmethod
    def load_shoot_sound(cls, shoot_path):
        Settings.shoot_sound = pygame.mixer.Sound(shoot_path)

    @classmethod
    def set_shoot_volume(cls, volume):
        Settings.shoot_sound.set_volume(volume)

    @classmethod
    def play_shoot_sound(cls):
        Settings.shoot_sound.play()

    @classmethod
    def load_explosion_sound(cls, shoot_path):
        Settings.explosion_sound = pygame.mixer.Sound(shoot_path)

    @classmethod
    def set_explosion_volume(cls, volume):
        Settings.explosion_sound.set_volume(volume)

    @classmethod
    def play_explosion_sound(cls):
        Settings.explosion_sound.play()


class GameObject:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.color = RED
        self.size = 20
        self.speed = 5.0
        self.has_image = False
        self.image = None

    def draw(self):
        if not self.has_image:
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.size, self.size))
        else:
            self.screen.blit(self.image, (self.x, self.y))

    def add_image(self, path_to_image):
        my_image = pygame.image.load(path_to_image)
        self.image = pygame.transform.scale(my_image, (self.size, self.size))
        self.has_image = True

    def rotate_image(self, degree):
        self.image = pygame.transform.rotate(self.image, degree)


class Explosion(GameObject):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.color = RED
        self.size = 1

    def expand(self, explosion_list):
        self.size += 6
        self.x -= 3
        self.y -= 3
        if self.size >= 40:
            explosion_list.remove(self)


class Boss(GameObject):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.color = RED
        self.pattern_x = 1
        self.size = 30

    def move(self):
        self.x += self.speed * self.pattern_x
        if self.x > WIDTH:
            self.pattern_x = -1
        if self.x < 0:
            self.pattern_x = 1

    def shoot(self, projectiles):
        projectile = Projectile(self.x + self.size // 2, self.y - self.size / 2 + 30, screen, -1)
        projectile.add_image('images\\projectile.png')
        projectile.rotate_image(50)
        projectiles.append(projectile)


class Enemy(GameObject):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.color = RED
        self.pattern_x = 1
        self.start_x = x
        self.speed = 2.5

    def move(self):
        self.x -= self.speed * self.pattern_x
        if self.x <= self.start_x - 40:
            self.pattern_x = -1
        if self.x >= self.start_x + 60:
            self.pattern_x = 1
            self.y += self.speed
            self.speed += 0.2

    def check_end(self):
        if self.y >= HEIGHT - self.size:
            Settings.is_game_active = False


class Hero(GameObject):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.color = GREEN
        self.size = 50

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def shoot(self, projectiles):
        projectile = Projectile(self.x + self.size // 2, self.y - self.size / 2 + 30, screen, 1)
        projectile.add_image('images\\projectile.png')
        projectile.rotate_image(-130)
        projectiles.append(projectile)


class Projectile(GameObject):
    def __init__(self, x, y, screen, align):
        super().__init__(x, y, screen)
        self.size = 5
        self.color = BLUE
        self.align = align

    def move(self):
        self.y -= self.speed * self.align

    def check_collision(self, enemy_list, boss_list, hero, projectile_list, explosion_list):
        if self.align == 1:
            for enemy in enemy_list:
                self.check_enemy(enemy, enemy_list, explosion_list, projectile_list)
            for boss in boss_list:
                self.check_enemy(boss, boss_list, explosion_list, projectile_list)

            if 0 >= self.y:
                projectile_list.remove(self)
        else:
            if hero.y - hero.size / 8 <= self.y <= hero.y + hero.size / 8:
                if hero.x - hero.size / 8 <= self.x <= hero.x + hero.size / 8:
                    Settings.is_game_active = False

            if HEIGHT <= self.y:
                projectile_list.remove(self)

    def check_enemy(self, enemy, enemy_list, explosion_list, projectile_list):
        if enemy.y - enemy.size / 2 <= self.y <= enemy.y + enemy.size / 2:
            if enemy.x - enemy.size / 2 <= self.x <= enemy.x + enemy.size / 2:
                enemy_list.remove(enemy)
                if type(enemy) is Boss:
                    Settings.score += 10
                elif type(enemy) is Enemy:
                    Settings.score += 1
                explosion_list.append(Explosion(self.x, self.y, self.screen))
                projectile_list.remove(self)
                Settings.play_explosion_sound()


WIDTH = 720
HEIGHT = 480

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 30
clock = pygame.time.Clock()

enemies = list()
projectiles = list()
explosions = list()
bosses = list()
boss = Boss(0, 10, screen)
boss.add_image('images\\boss.png')
bosses.append(boss)

for i in range(16):  # Количество противников в одном ряду
    for j in range(6):  # Количество рядов противников
        enemy = Enemy(40 + i * 40, 40 + j * 40, screen)
        enemy.add_image('images\\enemy.png')
        enemies.append(enemy)

hero = Hero(WIDTH / 2, HEIGHT - 50, screen)
hero.add_image('images\\hero.png')

is_left = False
is_right = False
is_shoot = False

background_image = pygame.image.load('images\\background.png')
scale_background = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

start_ticks_shoot = pygame.time.get_ticks()
start_ticks_shoot_boss = pygame.time.get_ticks()

Settings.load_and_start_music('music\\background.mp3')
Settings.set_music_volume(0.3)

Settings.load_shoot_sound('music\\shoot.wav')
Settings.set_shoot_volume(0.2)

Settings.load_explosion_sound('music\\explosion.wav')
Settings.set_explosion_volume(0.1)

is_start = call_menu(screen, FPS)
if not is_start:
    quit()

while Settings.is_game_active:
    screen.fill(BLACK)
    screen.blit(scale_background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                is_left = True
            if event.key == pygame.K_d:
                is_right = True
            if event.key == pygame.K_SPACE:
                is_shoot = True
            if event.key == pygame.K_p:
                Settings.pause_or_resume_music()
            if event.key == pygame.K_ESCAPE:
                is_start = call_menu(screen, FPS)
                if not is_start:
                    quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                is_left = False
            if event.key == pygame.K_d:
                is_right = False
            if event.key == pygame.K_SPACE:
                is_shoot = False

    seconds_from_last_shoot = (pygame.time.get_ticks() - start_ticks_shoot) / 1000
    seconds_from_last_shoot_boss = (pygame.time.get_ticks() - start_ticks_shoot_boss) / 1000

    if is_left:
        hero.move_left()
    if is_right:
        hero.move_right()
    if is_shoot and seconds_from_last_shoot > 0.5:
        hero.shoot(projectiles)
        Settings.play_shoot_sound()
        start_ticks_shoot = pygame.time.get_ticks()

    for enemy in enemies:
        enemy.move()
        enemy.draw()
        enemy.check_end()

    for boss in bosses:
        boss.move()
        boss.draw()
        if seconds_from_last_shoot_boss > random.random() * 10:
            boss.shoot(projectiles)
            start_ticks_shoot_boss = pygame.time.get_ticks()

    hero.draw()

    for projectile in projectiles:
        projectile.move()
        projectile.check_collision(enemies, bosses, hero, projectiles, explosions)
        projectile.draw()

    for explosion in explosions:
        explosion.expand(explosions)
        explosion.draw()

    Settings.draw_score(screen, 0, 0, GREEN)
    pygame.display.update()
    clock.tick(FPS)

screen.fill(BLACK)
Settings.draw_text(screen, 250, 200, RED, 50, "Game Over")
pygame.display.update()
time.sleep(5)
quit()