#Homewok

import math
import random

a=random.triangular(0,1000)
print(a)


ost=a*10//1%10
ost=math.ceil(ost)
print(ost)

def multiplication_table(number):
    i = 1
    while i < number:
        result = number * i
        print(f"{i}*{number} = {result}")
        i = i + 1


# number = int(input())
# multiplication_table(number)

# age=10
# name="Ann"
# print(f"hy im {name} me {age}")

#
# def multiplication_table(n):
#     for row in range(1, n + 1):
#         for column in range(1, n + 1):
#             result = row * column
#             print(f"{result}\t", end="")
#         print()
#
# multiplication_table(int(input()))



        #leess8 ex5 Practic function
# def multiplication_table(n):
#     column=1
#     row=1
#     while row<=n:
#         while column<=n:
#
#             result = row * column
#             print(f"{result}\t", end="")
#             column = column + 1
#         print()
#         column = 1
#         row=row+1
#
#
# multiplication_table(int(input()))

# sum = 0
# count = 0

# while True:
#     user_input = input()
#     if user_input != "стоп":
#         number = float(user_input)
#         sum += number
#         count += 1
#         # average = sum / count
#     else:
#         average = sum / count
#         print(average)
#         break
# size = 5
#
# size = int(input())
# e = 1
# for i in range(size, 0,-1):
#
#     for r in range(0,i):
#
#         print(e, end=" ")
#     e=e+1
#     print()

user_input = input()
user_list = list(map(int, user_input.split()))
first=user_list[0]
second=user_list[(len(user_list)-1)]
user_list.insert(0,second)
user_list.insert((len(user_list)-1),first)
print(user_list)
