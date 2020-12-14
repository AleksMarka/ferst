from sys import argv
a = argv
b = argv
c = argv

def zp(a, b, c):
    return a * b + c

print(f"Ваша зарплата {zp(int(a), int(b), int(c))}")