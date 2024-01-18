import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение констант
WIDTH, HEIGHT = 800, 600
FPS = 60
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пример с героем")




# Класс для героя
class Hero(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

    def update(self):
        # Перемещение героя влево-вправо
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Появление с левой стороны, если герой достиг правого края
        if self.rect.right > WIDTH:
            self.rect.left = 0

# Создание объектов
hero = Hero()
all_sprites = pygame.sprite.Group()
all_sprites.add(hero)

# Создание объекта шрифта
font = pygame.font.Font(None, 36)

# Переменная для отслеживания клика мышью
mouse_clicked = False

# Переменные для отслеживания времени отображения надписи
show_time = 0
DISPLAY_TIME = 2000  # 2000 миллисекунд = 2 секунды

# Основной игровой цикл
clock = pygame.time.Clock()
running = True




while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicked = True
            show_time = pygame.time.get_ticks()  # Запоминаем время клика

    # Обновление спрайтов
    all_sprites.update()

    # Отрисовка спрайтов
    screen.fill(BLACK)  # Черный фон
    all_sprites.draw(screen)

    # Проверка времени отображения надписи
    current_time = pygame.time.get_ticks()
    if mouse_clicked and current_time - show_time < DISPLAY_TIME:
        text = font.render("Привет", True, (255, 255, 255))
        screen.blit(text, (10, 10))
    else:
        mouse_clicked = False  # Сбрасываем флаг, когда прошло 2 секунды

    # Обновление экрана
    pygame.display.flip()

    # Ограничение частоты кадров
    clock.tick(FPS)

# Завершение программы
pygame.quit()
sys.exit()
