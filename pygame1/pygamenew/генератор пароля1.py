import random
print("Введите длину пароля")
n = int(input())
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

print("Введите количество паролей")
number = int(input())


j = 0
while number > j:
    password = ""
    i = 0
    while i < n:
        password += random.choice(chars)
        i += 1
    print(password)
    j += 1





# i = 0
# password = ""
# while i < n:
#     password += random.choice(chars)
#     i += 1
#
# print(password)
