import pygame
size=(700,700)
screen=pygame.display.set_mode(size)
smallrect=pygame.Rect(0,0, 400,400)

# smallrect.left=70
fps=90
clock=pygame.time.Clock()


smallrect.center=(size[0]//2,size[0]//2)






while True:
    smallrect.center = (size[0] // 2, size[0] // 2)

    smallrect.height += 1 #увеличиваем размер высоты
    smallrect.width += 1 #увеличиваем размер ширины




    screen.fill(pygame.Color("green"))
    pygame.draw.rect(screen,pygame.Color("red"),smallrect)

    pygame.display.flip()
    clock.tick(fps)