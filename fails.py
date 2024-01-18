# try:
#     file = open(r"C:\Users\user\PycharmProjects\easypro\failmy.txt", mode="r",  encoding="UTF-8")
#     print(file.closed)
#     file.close()
#     print(file.closed)
# except FileNotFoundError:
#     print("Не удалось открыть файл, проверьте путь к файлу!")

#
# try:
#     file = open(r"C:\Users\user\PycharmProjects\easypro\failmy.txt", mode="r",  encoding="UTF-8")
#
#     text = file.read()
#     # print(text)
#
#     file.seek(0)         # установить позицию в начало
#     print(file.read(5))  # The
#     # file.seek(4)         # установить позицию на четвёртый символ
#     # print(file.read(3))  # Zen
#
#     file.close()
# except FileNotFoundError:
#     print("Не удалось открыть файл, проверьте путь к файлу!")


# try:
#     file = open(r"failmy.txt", mode="r",  encoding="UTF-8")
#
#     text = file.readlines()  # The Zen of Python, by Tim Peters
#
#     print(text)
#
#     file.close()
# except FileNotFoundError:
#     print("Не удалось открыть файл, проверьте путь к файлу!")


# "первое задание"
# file = open(r"data.txt", mode="r",  encoding="UTF-8")
# text = file.readlines()  # The Zen of Python, by Tim Peters
# print(text)
#
#
#
# def x(i):
#     с = i.replace(" ", "")
#     с = с.replace("\n", "")
#     print(с)
#     return с
#
# text=map(x,text)
# text1=list(text)
# print(text1)


"второе задание"


# file = open(r"info.txt", mode="r",  encoding="UTF-8")
# text = file.readlines()  # The Zen of Python, by Tim Peters
# # print(text)
#
# spam = {}
#
# otlichniki= []
# listme=[]
# for i in text:
#     i=i.replace("\n","")
#     i=i.split("-")
#     # print(i[-1][-1])
#     listme.append(i[-1][-1])
#     if i[-1][-1] == "5":
#         otlichniki.append(i[0])
#
# otlichniki=sorted(otlichniki)
# print("Отличники: ", " ".join(otlichniki))
#
# listme=map(int,listme)
# list1=list(listme)
# # print(list1)
#
#
# summa1=sum(list1)
# c=summa1/len(list1)
#
# rounded_number = round(c, 2)
# print(rounded_number)

# "четвертое задание"
# file = open(r"data1.txt", mode="r",  encoding="UTF-8")
# text = file.readlines()
# print(text)
#
# newlist=[]
# summma1diagonal=0
# summma2diagonal=0
#
# for i in text:
#     i = i.replace(" ", "")
#     i = i.replace("\n", "")
#     print(i)
#     newlist.append(i)
#
# for i in range(len(newlist)):
#     # print(newlist[i][i],"newlist[i][i]")
#     summma1diagonal+=int(newlist[i][i])
#
#     print(newlist[i][-i-1],"newlist[i][-i-1]")
#
#     summma2diagonal += int(newlist[i][-i-1])
#
#
# print(summma1diagonal+summma2diagonal)
# file.close()


"третье задание"


# file = open(r"names.txt", mode="r",  encoding="UTF-8")
#
# text = file.read()
# text=text.split(",")
# # print(text)
# text=sorted(text)
# print(text)
# # print(ord("R")-64)
#
#
# summoch_list=list()
# count=1
# for slovo in text:
#     slovo = slovo.replace('"', '')
#     # print(slovo)
#     summoch=0
#     for bukva in slovo:
#         och=ord(bukva) - 64
#         summoch=summoch+och
#     summoch_list.append(summoch*count)
#     count+=1
#
# print(sum(summoch_list))
#
#
#
# file.close()