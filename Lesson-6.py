# Задача 1
from time import sleep
class Svetofor:
    __COLORS = {"red": 7, "yellow": 2, "green": 5}

    def __init__(self, c = "red"):
        self.__color = c
        print("Краснный")

    def running(self):
        if self.__color == "red":
            self.__color = "yellow"
            print("Желтый")
        elif self.__color == "yellow":
            self.__color = "green"
            print("Зеленый")
        else:
            self.__color = "red"

    def change_collor(self):
        return self.__color

    def interval(self, c):
        return self.__COLORS[c]


s = Svetofor()
sleep(s.interval(s.change_collor()))
s.running()
sleep(s.interval(s.change_collor()))
s.running()
sleep(s.interval(s.change_collor()))

# Задача 2
class Road:
    __length = 0
    __width = 0
    __mass = 25
    __deep = 5

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calc(self):
        return f"{(self.__length * self.__width * self.__mass * self.__deep) / 1000} тонн"


r = Road(20, 5000)
print(r.calc())

# Задача 3
class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"wage": 0, "bonus": 0}


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

    def position_worker(self):
        return self.position


a = Position()
a.name = "Сергей"
a.surname = "Иванов"
a.position = "Электрик"
a._income["wage"] = 25000
a._income["bonus"] = 20000

print(a.get_full_name())
print(a.position_worker())
print(a.get_total_income())

#Задача 4
class Car:
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула на{direction}")

    def show_speed(self):
        return self.speed


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


    def show_speed(self):
        speed = super().show_speed()
        return speed if speed <= 40 else f"Превышение скорости: {speed}!"


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        speed = super().show_speed()
        return speed if speed <= 60 else f"Превышение скорости: {speed}!"


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, True)


tc = TownCar(0, "Зеленый", "Автобус")
wc = WorkCar(0, "Ораньжевый", "Камаз")
sc = SportCar(0, "Желтый", "Lamborghini")
pc = PoliceCar(0, "Серый", "Форд", True)


print(wc.color, wc.name)
wc.go()
wc.turn("право")
wc.speed = 40
print(wc.show_speed())
wc.speed = 150
print(wc.show_speed())
wc.speed = 60
print(wc.show_speed())

#Задача 5
class Stationery:
    title = ""

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручки")


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандаша")


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркера")


stationery = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()

stationery.draw()
pen.draw()
pencil.draw()
handle.draw()