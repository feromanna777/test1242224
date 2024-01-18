# names = ["Иван", "Пётр", "Семён"]
#
# try:
#     with open("data3.txt", mode="w", encoding="UTF-8") as file:
#         print(names[0], names[1], names[2], file=file)
#         print(names[0], names[1], names[2], sep="\n", file=file)
#         print(names[0], file=file)
# except FileNotFoundError:
#     print("Не удалось открыть файл, проверьте путь к файлу!")

"задание1"
# a=input("")
# a=a.split(" ")
# try:
#     with open("data3.txt", mode="w", encoding="UTF-8") as file:
#         file.writelines([i + "\n" for i in a])
# except FileNotFoundError:
#     print("Не удалось открыть файл, проверьте путь к файлу!")

"задание2"

# import random
#
#
# list1=[random.randint(-1000,1000) for i in range(100)]
#
# list2=[random.randint(-1000,1000) for i in range(100)]
#
# print(list1)
#
# try:
#     with open("file4.txt", mode="w+", encoding="UTF-8") as file:
#         for num in list1:
#             file.write(str(num) + "\n")
#         file.seek(0)
#         text=file.readlines()
#         print(text)
# except FileNotFoundError:
#     print("Не удалось открыть файл, проверьте путь к файлу!")
#
#
# try:
#     with open("file5.txt", mode="w+", encoding="UTF-8") as file:
#         for num in list2:
#             file.write(str(num) + "\n")
#         # file.seek(0)
#         # text2=file.readlines()
#         # print(text2)
# except FileNotFoundError:
#     print("Не удалось открыть файл, проверьте путь к файлу!")
#
#
# common_numbers = list(set(list1) & set(list2))
# try:
#     with open("file6.txt", mode="w+", encoding="UTF-8") as file:
#         for num in common_numbers:
#             file.write(str(num) + "\n")
#         file.seek(0)
#         text3=file.readlines()
#         print(text3)
# except FileNotFoundError:
#     print("Не удалось открыть файл, проверьте путь к файлу!")

"задание3"

# try:
#     with open("file7.txt", mode="a+", encoding="UTF-8") as file:
#         file.seek(0)
#         text=file.readlines()
#
#         if len(text)==0:
#             count=1
#         else:
#             count=len(text)+1
#         file.seek(0)
#         while True:
#             a=input("vvedi")
#             if a=="СТОП":
#                 break
#             file.write(str(count)+str(a) + "\n")
#             count+= 1
#         file.seek(0)
#         text=file.readlines()
#         print(len(text))
# except FileNotFoundError:
#     print("Не удалось открыть файл, проверьте путь к файлу!")

"задание4"
# try:
#     with open("data4.txt", mode="r+", encoding="UTF-8") as file:
#         text = file.readlines()
#         for i in text:
#             print(i,"i")
#             text2 = i.split(":")
#             text3=text2[1].split("   ")
#             print(text3[-1], "t3[-1]")
#             text3[-1]=text3[-1].replace("\n","")
#             print(text3[-1], "t3[-1]")
#             # print(text3,"t3")
#             text3[0]=text3[0].replace(" ","")
#             print(text3, '''replace(' ","")''')
#             text3 = map(int, text3)
#             print(text3, 'map')
#             text4=list(text3)
#             print(text4)
#             sum2=sum(text4)
#             print(sum2)
# except FileNotFoundError:
#     print("Не удалось открыть файл, проверьте путь к файлу!")


stroki=[]
try:
    with open("data4.txt", mode="r+", encoding="UTF-8") as file:
        text = file.readlines()
        for i in text:

            # print(i,"i")
            text2 = i.split(":")
            text2[1]=text2[1].replace("   ","").strip()
            i=i.replace("\n","")
            # print(text2[1])
            summa=0
            print(i)
            print("----")
            for h in text2[1]:
                summa+=int(h)
            print(len(text2[1]))
            # print(summa)
            midnumber=summa/len(text2[1])
            rounded_midnumber = round(midnumber, 2)
            i=i+"   "+str(rounded_midnumber)+"\n"
            file.seek(0)
            stroki.append(i)
        print(stroki,"stroki")
        file.seek(0)
        file.writelines(stroki)


except FileNotFoundError:
    print("Не удалось открыть файл, проверьте путь к файлу!")