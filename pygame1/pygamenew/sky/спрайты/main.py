from spraits import *
pg.mixer.init()
pg.init()  #для инициализации пайгейм для слздание текста

size=(700, 700)
screen=pg.display.set_mode(size)

fps=100
clock=pg.time.Clock()

background=pg.image.load("background.jpg")
background=pg.transform.scale(background, size)
character=Character()



stars=pg.sprite.Group()
stars.add(Star())
stars.add(Star())
stars.add(Star())
stars.add(Star())
stars.add(Star())
stars.add(Star())
stars.add(Star())
stars.add(Star())
stars.add(Star())
stars.add(Star())
stars.add(Star())
stars.add(Star())

f1 = pg.font.Font(None, 25)   #для текста


while True:

    for event in pg.event.get():
        if event.type==pg.QUIT:
            quit()

    character.update()
    stars.update()

    screen.blit(background,(0,0))
    screen.blit(character.image,character.rect)
    stars.draw(screen)

    text1=f1.render("старт", True, pg.Color("Blue"))  #для текста
    screen.blit(text1, (200,450))  #для отрисовки текста
    pg.display.flip()
    clock.tick(fps)