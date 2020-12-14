# #Задача 1
from sys import argv
a = argv
b = argv
c = argv

def zp(a, b, c):
    return a * b + c

print(f"Ваша зарплата {zp(int(a), int(b), int(c))}")


# #Задача 2
# list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# res = [el for el in list[1::] if list[(list.index(el) - 1)] < el]
# print(res)

#Задача 3
# list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
# print(list)

#Задача 4
from itertools import groupby
# list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# # res = [el for el, _ in groupby(list)] """Попробовал такой вариант, пока не понял, что он группирует соседние числа. Пусть полежит как неправильный."""
# res = [el for el in list if list.count(el) == 1]
# print(res)

#Задача 5
# from functools import reduce
#
# def my_f(a, b):
#     return a * b
# list = [el for el in range(100, 1001) if el % 2 == 0]
# print(reduce(my_f, list))

#Задача 6
# from itertools import count
#
# a = 10
# b = 15
# def my_count(a, b):
#     for el in count(a):
#         if el > b:
#             break
#         else:
#             print(el)
# print(my_count(a, b))

# from itertools import cycle
# x = list(range(5))
# for i, j in enumerate(cycle(x)):
#     print(j, end=' ')
#     if i > 10:
#         print()
#         break
#
# #Задача 7
# "Вот так вроде просто"
# # import math
# # a = input("Введите число ")
# # print("Факториал = ", end="")
# # print(math.factorial(int(a)))
#
# "Тоже работает"
# a = 10
# fact = 1
# for i in range(1, a + 1):
#     fact = fact * i
#
# print("Факториал = ", end="")
# print(fact)