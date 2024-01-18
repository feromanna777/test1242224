# class Cat:
#     def __init__(self,name):
#         self.name=name
#     def voise(self):
#         print("Мяу")
#
#     def get_name(self):
#         print(f"кота зовут {self.name}")
#
#
# someCat=Cat("Рысь")
# someCat.voise()
# someCat.get_name()


class Ship:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def go_swimming(self):
        print(f"{self.name} отправился в плаванье.")

    def how_many_peple(self):
        print(f"На борту корабля {self.name} находится {self.people} человек.")

    def stop_ship(self, time):
        print(f"корабль {self.name} кинул якорь на {time} часов")

ship1=Ship("Чайка",2)
ship1.how_many_peple()
ship1.stop_ship(7)