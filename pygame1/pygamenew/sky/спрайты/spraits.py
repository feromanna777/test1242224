import random

import pygame as pg
class Character(pg.sprite.Sprite):
    def __init__(self):

        pg.sprite.Sprite.__init__(self)

        #import pygame as pg: Эта строка импортирует библиотеку Pygame и псевдонимирует ее как pg. Теперь вы можете обращаться к функциям и классам Pygame, используя pg вместо полного имени pygame. Например, вместо pygame.sprite.Sprite вы можете использовать pg.sprite.Sprite.

# class Character(pg.sprite.Sprite):: Эта строка определяет новый класс Character, который наследуется от класса pg.sprite.Sprite. Таким образом, Character будет являться подклассом Sprite из библиотеки Pygame, что позволит вам создавать спрайты для игрового персонажа.
#
# def __init__(self):: Этот метод __init__ - это конструктор класса Character. Он будет вызываться при создании нового объекта класса Character. Внутри этого метода вы можете выполнять инициализацию объекта, устанавливать его начальное состояние и параметры.
#
# pg.sprite.Sprite.__init__(self): Эта строка вызывает конструктор класса Sprite из библиотеки Pygame. Вызывая pg.sprite.Sprite.__init__(self), вы выполняете инициализацию объекта Character как экземпляр класса Sprite. Это позволяет объекту Character использовать функциональность Sprite, такую как добавление его в группы спрайтов и работу с коллизиями.
#
# Основная идея здесь заключается в том, что вы создаете собственный класс Character, который будет использовать функциональность и возможности класса Sprite из Pygame для создания игрового персонажа в вашей игре.


        self.image=pg.image.load("character.png")
        self.image = pg.transform.scale(self.image,(90,90))
        self.rect=self.image.get_rect()

        self.rect.x=100
        self.rect.y = 50

    def update(self):
        keys=pg.key.get_pressed() #без селф потому что  в других методах непонадобится

        if keys[pg.K_LEFT]:
            self.rect.x -=1
        if keys[pg.K_RIGHT]:
            self.rect.x +=1



class Star(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("звезда.png")
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,700)
        self.rect.y = random.randint(0,700)

    def update(self):
        if random.randint(0,1)==0:
            self.rect.x -= 1
            self.rect.y += 1

        else:
            self.rect.x += 1

