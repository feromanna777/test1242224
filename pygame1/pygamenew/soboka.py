import pygame as pg

screen=pg.display.set_mode((700, 700))
rectbig=pg.Rect(100,100,400,400)
recnos=pg.Rect(275,275,50,50)
recglas1=pg.Rect(150,150,80,100)
recglas2=pg.Rect(370,150,80,100)

recglas11=pg.Rect(170,170,30,40)
recglas22=pg.Rect(390,170,30,40)

recuxo=pg.Rect(10,50,90,90)
recuxo2=pg.Rect(500,50,90,90)


while True:
    screen.fill(pg.Color("green"))
    pg.draw.rect(screen, pg.Color("red"),rectbig)
    pg.draw.rect(screen, pg.Color("black"), recnos)
    pg.draw.rect(screen, pg.Color("blue"), recglas1)
    pg.draw.rect(screen, pg.Color("blue"), recglas2)

    pg.draw.rect(screen, pg.Color("white"), recglas11)
    pg.draw.rect(screen, pg.Color("white"), recglas22)

    pg.draw.rect(screen, pg.Color("blue"), recuxo)
    pg.draw.rect(screen, pg.Color("blue"), recuxo2)

    pg.draw.line(screen, pg.Color("black"), (300, 300), (350, 350), 6)
    pg.draw.line(screen, pg.Color("black"), (300, 300), (250, 350), 6)

    pg.draw.line(screen, pg.Color("black"), (200, 325), (250, 350), 6)
    pg.draw.line(screen, pg.Color("black"), (350, 350), (400, 325), 6)


    pg.display.flip()



    for e in pg.event.get():
        # Если нажали на крестик
        if e.type == pg.QUIT:
            exit()