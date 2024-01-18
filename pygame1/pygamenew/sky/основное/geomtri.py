import pygame as pg

size=(500,500)
screen=pg.display.set_mode(size)
small_rect=pg.Rect(0,0, 50, 50)
small_rect.x=0 #координата верхнего левого угла по x
small_rect.y=0#координата верхнего левого угла по y
small_rect.top=50 #координата вверха прямоугольника равна 50
small_rect.bottom=50 #координата низа прямоугольника равна 50

small_rect.left=50 #координата  лева (x)равна 50
small_rect.right=50 #координата права прямоугольника равна 50

small_rect.centerx=50 #середина прямоугольника по x равна 50
small_rect.centery=50 #середина прямоугольника по y равна 50

small_rect.topleft=(100,100) #координата верхнего левого угла
small_rect.topright=(100,100) #координата верхнего правого угла

small_rect.height=20 #высота
small_rect.width=30 #ширина
small_rect.size=(200,200) #размер
while True:
    screen.fill("green")

    pg.draw.rect(screen,"red",small_rect,3) # с контуром 3
    # pg.draw.rect(screen, "red", (-60, 0, 100, 200)) # закрашенный

    pg.display.flip()