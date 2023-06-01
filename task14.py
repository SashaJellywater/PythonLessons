# Задача 14:
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
number = int(input("Введите целое положительное число: "))
while number < 0:
    number = int(input("Некорректный ввод. Введите целое положительное число: "))
qwerty = 2
if number == 0:
    print(1)
elif number == 1:
    print(qwerty)
else:
    print(1)
    while qwerty <= number:
        print(qwerty)
        qwerty *= 2
