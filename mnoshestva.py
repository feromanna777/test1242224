# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# c=a.union(b)
# # c=a&b
# c=a.update(b)
# print(c)
# many = set()
# many.update([10, 2.5, "алгоритм"])
# many.update("автоматизация")
# many.remove("в")
# print(many)

# "practica 6"
#
# listki = int(input())
#
# seto = []
# for i in range(listki):
#
#     setfamilii = set()
#
#     stroki = int(input())
#     for e in range(stroki):
#         familii = input()
#         setfamilii.add(familii)
#
#     seto.append(setfamilii)
# print(seto)
# a = 0
# many = seto[a].intersection(seto[a + 1])
#
# print(many)
# for a in range(len(seto) - 1):
#     many = many.intersection(seto[a + 1])
# many = sorted(many)
# for a in many:
#     print(a)


"practica 6"

a = set()
for i in range(int(input())):
    b = set()
    for j in range(int(input())):
        b.add(input())
    if not a:
        a |= b
        c = a.union(b)
        print(a, "a")
        print(c, "c")
    else:
        a &= b
        print(b)
        a.intersection(b)
        print(a,"a")
        print(c,"c")

print(*sorted(a), sep="\n")