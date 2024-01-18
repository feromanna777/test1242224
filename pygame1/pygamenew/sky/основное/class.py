# class Airplane:
#     engine=2
#     seats=200
#
# DDT=Airplane()
# print(DDT.seats)
# DDT.seats=20
# print(DDT.seats)


# class Airplane:
#     def __init__(self):
#         self.engine=int(input("Двигатели"))
#         self.seats=int(input("Места"))
#         print("Самолет собран")
#
# # DDT=Airplane()
#
#
# plane1=Airplane()
# plane2=Airplane()
# plane3=Airplane()
#
# print(plane1.engine)


#self при создании обьекта вместо селф будет передаваться имя обьекта


# class Car:
#     def __init__(self, color, brand, speed):
#         self.color = color
#         self.brand = brand
#         self.speed = speed
#         print('Автомобиль готов!')




class Airplane:
    def __init__(self,engines,seats):
        self.engines=engines
        self.seats=seats
        print("Самолет собран")

# DDT=Airplane()


plane1=Airplane(seats=2,engines=4)
plane2=Airplane(engines=4,seats=2)
plane3=Airplane(engines=5,seats=10)

print(plane1.engines)