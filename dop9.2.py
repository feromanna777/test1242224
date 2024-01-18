# import math
# c=math.log2(int(input()))
#
# if c%1==0:
#     print(int(c))
# else:
#     print("Нет")
# a="gfhrjg"


# spam = {
#     1: 100,
#     2: 2.5,
#     "алгоритм": "algorithm",
#     "numbers": (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# }
# many = (1, 1, 2, 2, 3)
# many={"h","g","o"}
# # many = [1, 1, 2, 2, 3]
# c=sorted(many)
# c="h".join(many)
# print(c)



# spam = {"cat", "dog", "mouse", "fox", "cat", "wolf", "cow"}
#
# print(len(sorted(spam)))


# print("Yhhv".isalpha())
# print("CBN".isupper())
# print(ord('а'))
# print(ord('A'))
#
# char="а"
# print("ord(char)",ord(char))
#
# char2="я"
# print("ord(char2)",ord(char2))
# print((ord(char2)-ord(char)+3) % 32)
# print(34%32+ord(char))
# print(chr(1074))

# shifted_char_code = (ord(char) - base + shift) % 32 + base  # Вычисляем сдвинутый код символа

# word_dict = {}
tovari=input()
ceni=input()

listtovari = tovari.split()
listceni = ceni.split()

new_list = {}

for i in range(0, len(listtovari)):
    new_key = listtovari[i]
    new_value = float(listceni[i])
    new_list[new_key] = new_value

print()

new_list2=sorted(new_list,key=new_list.get)

print(*new_list2, sep="\n")