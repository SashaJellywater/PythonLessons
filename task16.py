# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
 
n = int(input('Введите количество элементов в массиве: '))
list_array = [int(i) for i in input().split()]
print(list_array)
number = int(input('Введите искомое число: '))
count = 0
for i in range (len(list_array)-1):
    if list_array[i] == number:
        count+=1
print (f"Число {number} встречается {count} раз/раза.")
