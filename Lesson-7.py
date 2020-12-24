# Задача 1
class Matrix:
    def __init__(self, a):
        self.b = '\n'.join(['\t'.join([str(j) for j in i]) for i in a])
        List = []
        for i in a:
            List.append([j for j in i])
        self.a = List

    def __str__(self):
        self.c = str(self.b)
        return self.c

    def __add__(self, other):
        NumStr = len(self.a)
        NumCol = len(other.a[0])
        for i in range(NumStr):
            for j in range(NumCol):
                self.a[i][j] = self.a[i][j] + other.a[i][j]
            Result = self.a
        return Matrix(Result)

m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1 + m2)



#Задача 2
from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, size, growth):
        self.size = size
        self.growth = growth

    @property
    def itogo(self):
        return f'Всего потребуется ткани: {(self.size/6.5 + 0.5) + (2 * self.growth + 0.3): .2f} метров'

class Palto(Clothes):

    def itogo_palto(self):
        return f'На пальто потребуется: {self.size/6.5 + 0.5: .2f} метров ткани'

class Costum(Clothes):

    def itogo_costum(self):
        return f'На костюм потребуется: {2 * self.growth + 0.3: .2f} метра ткани'

palto = Palto(int(input("Какой размер пальто: ")), int(input("Какой рост пальто: ")))
costum = Costum(int(input("Какой размер костюма : ")), int(input("Какой рост костюма: ")))


print(palto.itogo_palto())
print(costum.itogo_costum())
print(palto.itogo)


# Задача 3.
class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return f'При сложении клеток: {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        if sub >= 0:
            return f'При вычитании клеток: {sub}'
        else:
            print('Нельзя вычитать больше клеток, чем было')

    def __mul__(self, other):
        return f'При умножении клеток: {self.quantity * other.quantity}'

    def __truediv__(self, other):
        return f'При делении клеток: {self.quantity // other.quantity}'

    def make_order(self, cell_row):
        a = ''
        for i in range(int(self.quantity / cell_row)):
            a = a + '*' * cell_row + '/n'
        a = a + '*' * (self.quantity % cell_row)
        return a

cell1 = Cell(int(input("Введите количество клеток: ")))
cell2 = Cell(int(input("Введите количество других клеток: ")))

print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1.make_order(5))
