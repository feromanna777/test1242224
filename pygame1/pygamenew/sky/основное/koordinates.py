import pygame
size=(700,700)
screen=pygame.display.set_mode(size)
smallrect=pygame.Rect(0,0, 400,400)

# smallrect.left=70
fps=90
clock=pygame.time.Clock()


left_eye=pygame.Rect(0,0, 50,50)
right_eye=pygame.Rect(0,0, 50,50)

left_eye.midright=(size[0] // 2-10,size[1]//2)

right_eye.midleft=(size[0] // 2+10,size[1]//2)
# print(smallrect.x)
smallrect.center=(size[0]//2,size[0]//2)
# smallrect.x = size[0] // 2 - smallrect.width // 2
# print(smallrect.x)
# print(size[0] // 2)



direction='right' #начальное направление движения

while True:
    # smallrect.center = (size[0] // 2, size[0] // 2)

    # smallrect.height += 1 #увеличиваем размер высоты
    # smallrect.width += 1 #увеличиваем размер ширины

    if smallrect.left==0: #смена напрвления если дошли до левого края
        direction='right'

    if smallrect.right==size[0]:
        direction='left' #смена напрвления если дошли до правого края


    if direction=='right':
        smallrect.x += 1 #перемещаем прямоугольник вправо на 1 px по x
        right_eye.x += 1
        left_eye.x += 1

    if direction=='left':
        smallrect.x -= 1
        right_eye.x-=1
        left_eye.x-=1


    screen.fill(pygame.Color("green"))
    pygame.draw.rect(screen,pygame.Color("red"),smallrect)
    pygame.draw.rect(screen, pygame.Color("white"), left_eye)
    pygame.draw.rect(screen, pygame.Color("white"), right_eye)

    pygame.display.flip()
    clock.tick(fps)