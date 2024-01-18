# from random import *
# print(randrange(1,10,2))
# print(randint(2, 10))
# print(choice([1,3,8,6]))
# print(triangular(2, 4))
#
# import math
# print(math.sqrt(11))


many1 = set()
while True:
    number=int(input())
    if number=="":
        break
    many1.add(number)

many2 = set()
while True:
    number=int(input())
    if number=="":
        break
    many2.add(number)


c = many1.intersection(many2)
c=list(c)
c.sort()
print(c)