import random
# import tkinter
#
# screen = tkinter.Tk()
# screen.title("Это моё окно")
# screen.geometry('500x500')
#
# text_out = tkinter.Text(screen, width=50, height=20)
# text_out.pack()
# text = tkinter.Label(text="Здесь можно написать любой текст")
# text.pack()
# text2 = tkinter.Label(text="Это мой блокнот для заметок")
# text2.pack()
#
#
# text2 = tkinter.Label(text="Буду записывать свои мысли")
# text2.pack()
# n = tkinter.Entry(width=10)
# n.pack()
#
#
#
# screen.mainloop()


"Генератор пароля"
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
    n = int(len_pass.get()) # присваиваем переменной n значение, которое было введено в созданном нами поле
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    i = 0
    password = ""
    while i < n:
        password += random.choice(chars)
        i += 1

    text_out.insert(tkinter.END, password + "\n")  #text_out.insert(tkinter.END, word) – вставляем слово “hello” в большое поле для вывода



def clear():
    text_out.delete('1.0', tkinter.END)


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

b5 = tkinter.Button(text="Очистить", command=clear)
b5.pack()

len_text = tkinter.Label(text="Длина пароля")
len_text.pack()

len_pass = tkinter.Entry(width=10, justify=tkinter.CENTER) #2 окно для ввода данных.
len_pass.insert(0, "15")
len_pass.pack()

text_out = tkinter.Text(screen, width=50, height=20)
text_out.pack()

screen.mainloop()

