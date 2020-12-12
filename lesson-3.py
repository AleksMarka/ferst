#Задача 1

# def fun():
#     try :
#         arg_1 = float(input("Пожалуйста, введите число от 1 до 100 "))
#         arg_2 = float(input("Пожалуйста, введите число от 1 до 100 "))
#     except ValueError:
#         return None
#         print(err)
#     except ZeroDivisionError as err:
#         print(err)
#         return None
#     result = arg_1 / arg_2
#     return result
# print(fun())
#
# 2 Задача
# def user_info(name, surname, yo, city, mail, phone):
#     return phone, name, surname, yo, city, mail
# user = {
#     "name": "Aleksei",
#     "surname": "Markov",
#     "yo" : 38,
#     "city" : "Moscow",
#     "mail" : "as@as.ru",
#     "phone" : "+777777777"
# }
# print (user_info(**user))

# 3 Задача - не работает. Не знаю почему, кажется все правильно.
a = 2
b = 3
c = 7
def my_func(a, b, c):
    z = (a, b, c)
    y = z.remove(min(a, b, c))
    return a + b + c - y
a = 2
b = 3
c = 7
print(my_func(int(a), int(b), int(c)))

# 4 Задача
# def my_func(a, b):
#     return b**a
# def my_func_two(a, b):
#     c = 1
#     for i in range(a):
#         c *= b
#     return c
#
# a = int(input("Введите целое, положительное число "))
# b = int(input("Введите целое, отрицательное число "))
# print(my_func(a, b))
# print(my_func_two(a, b))

# Задача 5
# def my_func(*args):
#     a = 0
#     for b in args:
#         try:
#             a += int(b)
#         except ValueError:
#             continue
#     return a
# row = ''
# while True:
#     row = "%s %s" % (row, input(f"Введите числа через пробел. Нажмите - z чтоб завершить цикл: "))
#     print(f"Сумма: {my_func(*row.split())}")
#     if row.find("z") >= 0:
#         break

#Задача 6
# def int_func(text):
#     return str(text).capitalize()
# big = input("Введите текст: ")
# cap = list()
# for i in big.split():
#     cap.append(int_func(i))
# print(' '.join(cap))