import pygame
size=(700,700)
screen=pygame.display.set_mode(size)


# smallrect.left=70
fps=90
clock=pygame.time.Clock()


smallrect=pygame.Rect(0,0, 50,50)

direction='right'
def autopilot(starship_rect, direction):
    smallrect = pygame.Rect(starship_rect[0],starship_rect[1], 50, 50)
    if direction=='right':
        smallrect.x += 50

    return smallrect.topleft


while True:
    # smallrect.center = (size[0] // 2, size[0] // 2)

    for e in pygame.event.get():
        # Если нажали на крестик
        if e.type == pygame.QUIT:
            exit()
    c=autopilot((380, 0), 'right')
    smallrect = pygame.Rect(c[0], c[1], 50, 50)
    # if smallrect.left==0:
    #     direction='right'
    #
    # if smallrect.right==size[0]:
    #     direction='left'


    # if direction=='right':
    #     smallrect.x += 1
    #
    # if direction=='left':
    #     smallrect.x -= 1

    screen.fill(pygame.Color("green"))
    pygame.draw.rect(screen,pygame.Color("red"),smallrect)

    print(autopilot((40,0), 'right'))
    pygame.display.flip()
    clock.tick(fps)