
import tkinter
import random

def print_hello():
    x = int(n.get())
    word = "\nhelp\nuu "
    for i in range(x):
        text_out.insert(tkinter.END, word)


screen = tkinter.Tk()
screen.title("Это моё окно")
screen.geometry('500x500')


# text_out = tkinter.Text(screen, width=50, height=20)
# text_out.pack()
#
#
#
# text = tkinter.Label(text="Здесь можно написать любой текст")
# text.pack()
#
# text2 = tkinter.Label(text="Это мой блокнот для заметок")
# text2.pack()
#
#
# n = tkinter.Entry(width=10)
# n.pack()
#
#
#
#
#
# b3 = tkinter.Button(screen, text="Ран", command=print_hello)
# b3.pack()


text = tkinter.Label(text="Здесь можно написать любой текст")
text.pack()

text2 = tkinter.Label(text="Это мой блокнот для заметок")
text2.pack()

text2 = tkinter.Label(text="Буду записывать свои мысли")
text2.pack()

n = tkinter.Entry(width=1)
n.pack()

b = tkinter.Button(screen, text="Напечатать", command=print_hello)
b.pack()

text_out = tkinter.Text(screen, width=50, height=20)
text_out.pack()


screen.mainloop()