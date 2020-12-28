# Задача 1
class Date:
    long_months = [1, 3, 5, 7, 8, 10, 12]
    short_months = [4, 6, 9, 11]
    february = [28]
    february_leap = [29]

    def __init__(self, day):
        self.day = day

    @staticmethod
    def date_validate(day: str):
        li = Date.date_to_number(day)

        leapflag = 1 if li[2] % 4 == 0 else 0

        if li[1] in Date.long_months and li[0] > 31 or li[1] in Date.short_months and li[0] > 30:
            print("День введен некорректно!")
        if leapflag and li[0] > 29 or li[0] > 28:
            print("В феврале не может быть такого числа")
        if not (0 < li[1] < 13):
            print("Некоректно введен месяц")
        return True


# Задача 2
class DivisionByZero(ZeroDivisionError):

    def __str__(self):
        return 'Делить на 0 нельзя. Попробуйте ввести другое значение!'

def div(a, b):
    if not b:
        raise DivisionByZero
    return a/b

if __name__ == "__main__":
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    try:
        print(div(a, b))
    except MyShinyDivisionByZero as err:
        print(err)


#Задача 3
class NotNumber(ValueError):
    pass

my_list = []
while True:
    try:
        a = input("Введите число в список или напишите stop: ")
        if a == "stop":
            break
        if not a.isdigit():
            raise NotNumber(a)
        my_list.append(int(a))
    except NotNumber as ex:
        print("Не число!", ex)
print(my_list)

# Задача 4

class Orgtechnica:
    def __init__(self, name: str, price: float, cnt: int, otdel: str):
        self.name = name
        self.price = price
        self.cnt = cnt
        self.otdel = otdel

    def __str__(self):
        params = ''
        for key in self.__dict__:
            if key == '':
                params = f"{params}{key} : {self.__dict__[key].name} \n"
            else:
                params = f"{params}{key} : {self.__dict__[key]} \n"
        return params


class Printer(Orgtechnica):
    def __init__(self, name, price, cnt, otdel, color: str, speed: int):
        super().__init__(name, price, cnt, otdel)
        self.color = color
        self.speed = speed


class Scaner(Orgtechnica):
    def __init__(self, model, price, cnt, otdel, color: str, wifi: bool):
        super().__init__(model, price, cnt, otdel)
        self.color = color
        self.wifi = wifi


class Shreder(Orgtechnica):
    def __init__(self, model, price, cnt, otdel, size: int, speed:int):
        super().__init__(model, price, cnt, otdel)
        self.size = size
        self.speed = speed



if __name__ == "__main__":
    office_tech = [Printer("Canon", '10000', "20", "Buh", "Color", "122"),
                   Scaner("HP", '5000', "5", "Buh", "Color", True),
                   Shreder("Shrder", '7000', "1", "Buh", "220", "200")]

    for el in office_tech:
        print(el)

# Задача 7
class ComplexNumber:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def __str__(self):
        b = ' + ' if self.b > 0 else ' - '
        b = f'{b}{abs(self.b)}' if abs(self.b) != 1 else f'{b}'
        if self.b != 0:
            return f"{self.a}{b}i"
        else:
            return f"{self.a}"

    def __add__(self, other):
        c = self.a + other.a
        d = self.b + other.b
        return ComplexNumber(c, d)

    def __mul__(self, other):
        c = self.a * other.a - self.b * other.b
        d = self.a * other.b + self.b * other.a

        return ComplexNumber(c,d)


e1 = ComplexNumber(2, 5)
e2 = ComplexNumber(3, 4)
print(e1 + e2)
print(e1*e2)
