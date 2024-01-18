class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
    def increase_speed(self, delta):
        self.speed += delta
bmw = Car("black", 300)
zhiguly = Car("gold", 999)

bmw.increase_speed(1000)
bmw.color="t"
print(bmw.color)