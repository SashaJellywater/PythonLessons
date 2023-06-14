# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

list_1 = [int (i) for i in input(f'Введите оценки: ').split()]
print(list_1)
def vasa(points):
    min = points[0]
    max1 = points[0]
    for i in range (1, len(points)):
        if min > points[i]:
            min = points[i]
        elif max1<points[i]:
            max1= points[i]
    for i in range(len(points)):
        if points[i]== max1:
            points[i]= min
    return points
print(vasa(list_1))
