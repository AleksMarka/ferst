# Задача 1
try:
    with open("my_file.txt", "w", encoding='UTF-8') as file:
        while True:
            s = input("- ")
            file.write(f"{s}")
            if s == "":
                break
except Exception as err:
    print(err)

# Задача 2
with open("text.txt", "a", encoding='UTF-8') as file:
    s = input("- ")
    file.write(f"{s}")
try:
    with open("text.txt", "r", encoding="UTF-8") as f:
        words_per_line = [len(line.split()) for line in f]
        print(f"Строк {len(words_per_line)}")
        print(f"Слов (по строчно): {words_per_line}")
except Exception as err:
    print(err)

#Задача 3
with open("company.txt", "a", encoding='UTF-8') as file:
    s = input("- ")
    file.write(f"{s}\n")

with open('company.txt', 'r', encoding='UTF-8') as file:
    salary = 0
    sum = 0
    sr = 0

    for line in file:
        content = line.split(',')
        try:
            salary = salary + int(content[1])
        except ValueError as err:
            print('Error', err)
        sum += 1
        if int(content[1]) < 20000:
            print(f'Менее 20 000 Р у следующих сотрудников: {content[0]}')

    sr = salary / sum
    print(f'В среднем доход сотрудников составляет: {sr} Р.')

#Задача 5
def create_ad_file(num_str):
    with open("5.txt", "w", encoding="UTF-8") as f:
        f.writelines(num_str)
create_ad_file("5 5 5 5 5 5 5 ")
def sum_file():
    with open("5.txt", "r", encoding="UTF-8") as f:
        ls = f.readlines()
        '''Если больше одной строки'''
        for l in ls:
            lt = l.split(" ")
            lt = [int(l) for l in lt]
            print("Sum ", sum(lt))
sum_file()

#Задача 6
def sum(str):
    s = 0
    try:
        for i in str.split():
            if i[:i.find("(")] != "":
                s += int(i[:i.find("(")])
        return s
    except ValueError as err:
        print('Error', err)
        return 0
try:
    with open("subjects.txt", "r", encoding="UTF-8") as f:
        subjects = {}
        for subj in f.readlines():
            rec = subj.split(":")
            subjects[rec[0]] = sum(rec[1])
        print(subjects)
except ValueError as err:
    print('Error', err)