import pygame, random

WH = 480
HG = 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self): #__init__(self)
        pygame.sprite.Sprite.__init__(self) #__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill("Green")
        self.rect = self.image.get_rect()
        self.rect.x = WH/2
        self.rect.y = HG - 50
        self.speedx = 0
        # self.speedy = 0 #перенесли в update


    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -7
        if keystate[pygame.K_RIGHT]:
            self.speedx = 7
        self.rect.x += self.speedx
        if self.rect.right > WH:
            self.rect.right = WH
        if self.rect.left < 0:
            self.rect.left = 0
        # if keystate[pygame.K_DOWN]:
        #     self.speedy = 7
        # if keystate[pygame.K_UP]:
        #     self.speedy = -7
        # self.rect.y += self.speedy
    def shoot(self):
        bullet = Bullet(self.rect.x + 35, self.rect.y)  # создание пули появитсы в х игрока + 35
        all_sprites.add(bullet)
        bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
    def __init__(self): #__init__(self)
        pygame.sprite.Sprite.__init__(self) #__init__(self)
        self.image = pygame.Surface((40, 40))
        self.image.fill("Red")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(30, WH - self.rect.right)
        self.rect.y = random.randint(-100, -40)
        self.speedy = random.randint(1, 4)
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HG+10: #HEIGHT + 10
            self.rect.x = random.randint(30, WH - self.rect.width) #!!!rect.width   no right
            # print(self.rect.width)
            # print(self.rect.right)
            self.rect.y = random.randint(-100, -40)
            self.speedy = random.randint(1, 4)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y): #def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self) #__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()  #создание невидимый скулут пурсонажа который помагает отслеживать соприкосновение с другими спрайтами
        self.rect.x = x
        self.rect.y = y
        self.speedy = -10
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

ws = pygame.display.set_mode((WH, HG)) #переставиоа наверх
pygame.display.set_caption("Game23") #переставиоа наверх


clock = pygame.time.Clock()
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()

for i in range(15):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)



while True:
    clock.tick(FPS)


    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                player.shoot()
    all_sprites.update()
    hits = pygame.sprite.spritecollide(player, mobs, True)    #проверка не ударил ли моб игрока.Функция отслеживает соприкосновение спрайтов, если True то враги исчезают
    if hits:
        while 1:
            clock.tick(FPS)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    exit()
            ws.fill(BLACK)
            all_sprites.draw(ws)
            pygame.display.flip()
        exit() # условие если враги коснулись игрока то закрыть игру
    ws.fill(BLACK)
    all_sprites.draw(ws)
    pygame.display.flip()