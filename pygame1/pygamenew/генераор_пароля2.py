import tkinter

import tkinter
import random


def F1():
    print("Я же просил!")


def F2():
    print("Ты лучший в мире программист!")


def F3():
    x = random.randint(1, 10)
    print(x)


def GenPass():
    print("Введите длину пароля")
    n = int(input())
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    i = 0
    password = ""
    while i < n:
        password += random.choice(chars)
        i += 1

    print(password)


screen = tkinter.Tk()
screen.title("Это моё окно")
screen.geometry('500x500')

b = tkinter.Button(screen, text="Не нажимай", command=F1)
b.pack()

b2 = tkinter.Button(screen, text="Сюда нажимать можно", command=F2)
b2.pack()

b3 = tkinter.Button(screen, text="Рандомное число", command=F3)
b3.pack()

b4 = tkinter.Button(screen, text="Сгенерировать пароль", command=GenPass)
b4.pack()

screen.mainloop()

