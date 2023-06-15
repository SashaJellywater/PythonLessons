# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. 

m = int(input('Введите количество элементов набора чисел: '))
array= [int (i) for i in input(f'Введите {m} чисел: ').split()]
count = 0
# for i in range(len(array)):
#     if i>0 and i<len(array)-1:
#         if array[i-1]<array[i] and array[i]> array[i+1]:
#             count+=1
for i in range(1, m-1):
    if array[i-1]<array[i]>array[i+1]:
        count+=1
print(count)
