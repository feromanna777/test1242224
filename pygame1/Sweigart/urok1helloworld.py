import pygame,sys
from pygame.locals import*
pygame.init()
window=pygame.display.set_mode((500,400),0,100)
pygame.display.set_caption("Привет мир")




BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

basicFont=pygame.font.SysFont(None,48)
text=basicFont.render("Привет, мир",True, WHITE, BLUE)
textRect=text.get_rect()
textRect.centerx = window.get_rect().centerx
textRect.centery = window.get_rect().centery

window.fill(WHITE)

pygame.draw.polygon(window, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)),18)
pygame.draw.line(window, BLUE, (60, 60), (120, 60), 4)
window.blit(text, textRect)

pygame.draw.ellipse(window, RED, (300, 250, 40, 80), 1)
pygame.draw.circle(window, BLUE, (50, 50), 20, 0)

pygame.draw.rect(window, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

pixArray = pygame.PixelArray(window)
pixArray[480][380]  = BLACK

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()