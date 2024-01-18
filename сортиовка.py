# #       0  1  2  3  4  5  6  7  8  9
# spam = [9, 2, 0, 3, 6, 1, 6, 0, 5, 8]
#
# min_value = spam[0]
# min_index = 0
#
# for i in range(1, len(spam)):
#     if spam[i] <= min_value:
#         min_value = spam[i]
#         min_index = i
#
# # print(min_value)  # 0
# # print(min_index)
#
#
# spam[min_index] = spam[0]
# # print("u",spam[0] )
# spam[0] = min_value
# # print(min_index)  # 7
# # print(min_value)
# print(spam)
#
#
# for j in range(0, len(spam) - 1):
#
#     min_value = spam[j]
#     min_index = j
#     print("min_index", min_index,"j", j)
#
#     for i in range(j + 1, len(spam)):
#         print("for i",i,"for j", j)
#         if spam[i] <= min_value:
#             min_value = spam[i]
#             min_index = i
#             print("ifi", i,"min_value=",min_value)
#             print(spam)
#
#     print(" spam[min_index] = spam[j]\n", spam[min_index], "=", spam[j])
#     spam[min_index] = spam[j]
#
#     print("min_index",min_index)
#     print("j",j)
#     spam[j] = min_value
#     print("spam2)",spam)
# print(spam)  # [0, 0, 1, 2, 3, 5, 6, 6, 8, 9]



#Cртировка 2
from random import randint
# from random import randint
# from time import time
#
# def selection_sort(spam: list):
#     for j in range(0, len(spam) - 1):
#         min_value = spam[j]
#         min_index = j
#         # print("j",j)
#         for i in range(j + 1, len(spam)):
#             # print("i", i)
#             if spam[i] <= min_value:
#                 min_value = spam[i]
#                 min_index = i
#                 # print("ifi", i, "min_value=", min_value)
#         spam[min_index] = spam[j]
#         spam[j] = min_value
#     return spam
#
#
#
# # ...
# # ...
# # ...
#
# count = 1000      # количество элементов в списке
#
# start = time()   # включить секундомер
# spam = [randint(-1000, 1000) for i in range(count)]
# new_spam = selection_sort(spam)
# finish = time()  # выключить секундомер
# print(new_spam )
# print("time:", finish - start)
#


#Cртировка 3
#       0  1  2  3  4  5  6  7  8  9
# spam = [9, 2, 0, 3, 6, 1, 6, 0, 5, 8]
#
# for i in range(len(spam) - 1):
#     for j in range(len(spam) - i - 1):
#         if spam[j] > spam[j + 1]:
#             spam[j], spam[j + 1] = spam[j + 1], spam[j]
#
# print(spam)  # [0, 0, 1, 2, 3, 5, 6, 6, 8, 9]


# def fun(number: int):
#     return number % 2
# spam = (9, 2, 0, 3, 6, 1, 6, 0, 5, 8)
# print(type(spam))
#
# n=sorted(spam, reverse=False,key=fun)
#
# print(n)  # [0, 0, 1, 2, 3, 5, 6, 6, 8, 9]


# print(*sorted(input()))

#
# print(*sorted(input().split(), reverse=True))

# familia = input()
# list = familia.split()
#
#
# def key_len(familiauser):
#     return len(familiauser)
#
#
# list.sort(key=key_len)
# for i in list:
#     print(i, end=" ")

# familia=input()
# list=familia.split()
# print(list)
# def kkey(element):
#     return element[1]
# list.sort( key=kkey,reverse=True)
#
# for i in list:
#     print (i,end=" ")
#
# str1=input()
# str2=input()
# str1=str1.split()
# str2=str2.split()
#
# str1mnoj=set(str1)
# str2mnoj=set(str2)
# print(str1mnoj.union(str2mnoj))


import turtle

# Создаем объект экрана
screen = turtle.Screen()

# Создаем объект черепашки
pen = turtle.Turtle()

# Устанавливаем максимальную скорость черепашки
pen.speed(0)

# Скрываем черепашку (чтобы не видеть перемещение до окончания рисования)
pen.ht()
line=100
def recursion(line):
    pen.fd(line)
    if line>20:
        pen.rt(10)
        recursion(line-1)
        pen.rt(-20)
        recursion(line-1)
        pen.rt(10)
    pen.bk(line)


# # Цикл для рисования кругов разных размеров и цветов
# for i in range(360):
#     pen.color("red")
#     # pen.circle(i)
#     pen.color("orange")
#     # pen.circle(i * 0.8)
#     pen.rt(i)
#     pen.fd(line)
#     line=line/2
#
# # Запускаем основной цикл обработки событий экрана
recursion(30)
screen.mainloop()