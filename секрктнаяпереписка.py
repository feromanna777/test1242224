import tkinter as tk

# window.title("Hello world")
# window.geometry("300x300")

# hello = tk.Label(text="Hello world!")
# hello.pack()
# button = tk.Button(text="не нажимай!")
# button.pack()
# button = tk.Button(text="Click me!")
# button.pack()

# Начало программы Секретная переписка


from tkinter import messagebox, simpledialog, Tk


window = tk.Tk()
def get_task():
    message = simpledialog.askstring('Задание', 'Что сделать: зашифровать или расшифровать?')
    return message


def get_message():
    task = simpledialog.askstring('Задание', 'ВВЕДИТЕ СЕКРЕТНОЕ СООБЩЕНИЕ')


def is_even(number):  # функция является ли четным числом
    return number % 2 == 0


def get_even_letters(message):  # получить буквы в четных позициях
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters


def get_odd_letters(message):  # получить буквы в нчетных позициях
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters


def swap_letters(message):  # меняет буквы местами
    letter_list = []
    if not is_even(len(message)):
        message = message + "x"
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message) / 2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ''.join(letter_list)
    return new_message


# root=Tk()

# get_task()
# get_messsage()
while True:
    task = get_task()
    if task == "зашифровать":
        message = get_message()
        print(message)
        zachifrovanaicoobwenie = swap_letters(message)
        messagebox.showinfo("зашифрованое сообщение:", zachifrovanaicoobwenie)


    elif task == 'расшифровать':
        message = get_message()
        raschifrovonae_coobchenie = swap_letters(message)
        messagebox.showinfo("Расшифрованнное сообщение", raschifrovonae_coobchenie)

    else:
        break

tk.mainloop()


