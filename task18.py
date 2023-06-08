# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

# n = int(input('Введите количество элементов в массиве: '))
# # list_array = [int(i) for i in range(1, n+1)]
# list_array = [int (i) for i in input().split()]
# print(list_array)
# number = int(input('Введите искомое число: '))
# temp = 0
# max = 0
# for i in range (n):
#      if list_array[i] < number:
#           max = list_array[i]
#           if max> temp:
#                temp = max
# print(temp)

n = int(input('Введите количество элементов в массиве: '))
list_array = [int (i) for i in input().split()]
print(list_array)
number = int(input('Введите искомое число: '))
temp = 0
max = 0
for i in range (len(list_array)):
     if list_array[i] < number:
          max = list_array[i]
          if max> temp:
               temp = max
     else:
          tem = list_array[i]
for i in range (len(list_array)):
     if list_array[i] > number:
          mini = list_array[i]
          if mini<tem:
               tem = mini
if (tem-number==number- temp):
     print(temp,tem )
if (tem-number > number- temp):
     print (temp)
if (tem-number < number- temp):
     print(tem)
