# import turtle
#
#
# def test():
#     global score
#     score = score[:7] + str(int(score[7:]) + 1)  # "SCORE " + str(int("0") + 1)
#     pen.clear()
#     pen.write(score, font=("Consolas", 40, "normal"))
#
#
# #        01234567
# score = "SCORE: 0"
#
# screen = turtle.Screen()
#
# pen = turtle.Turtle()
# pen.ht()
# pen.write(score, font=("Consolas", 40, "normal"))
#
# screen.onkeypress(test, "space")
# screen.listen()
#
# screen.mainloop()


#
# n=int(input())
# n1=1
# step=0
# while n1<n:
#         if n>=(n1*2):
#             n1=(n1*2)
#         else:
#             n1+=1
#         print(step,"step")
#         step+=1

import turtle

screen = turtle.Screen()  # графическое окно

pen = turtle.Turtle()     # графический объект
pen.speed(0)
import turtle

screen = turtle.Screen()  # графическое окно

pen = turtle.Turtle()     # графический объект
pen.speed(0)


def rectangle(
    x: int, y: int,
    width: int, height: int,
    line_color="black", fill_color="white",
    thickness=1
):
    """
    x          - координата левого верхнего угла по оси X
    y          - координата левого верхнего угла по оси Y
    width      - ширина прямоугольника
    height     - высота прямоугольника
    line_color - цвет контура
    fill_color - цвет заливки
    thickness  - толщина контура
    """
    pen.color(line_color, fill_color)
    pen.width(thickness)
    pen.up()
    pen.goto(x - width // 2, y + height // 2)
    pen.down()
    pen.begin_fill()  # начать заливку
    i = 2             # нарисовать фигуру
    while i > 0:
        pen.fd(width)
        pen.rt(90)
        pen.fd(height)
        pen.rt(90)
        i -= 1
    pen.end_fill()    # завершить заливку


rectangle(0, 0, 100, 100, "red", "green", 5)  # квадрат
rectangle(0, 150, 300, 100)                   # горизонтальный прямоугольник
rectangle(200, 50, 100, 300)                  # вертикальный прямоугольник


screen.mainloop()




screen.mainloop()