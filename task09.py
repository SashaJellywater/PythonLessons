# Задача №9.
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Input: 5
# Output: 120
n = int(input("Введите целое неотрицательное число: "))
while n < 0:
    n = int(input("Некорректный ввод. Введите целое неотрицательное число: "))
count = 0
nFact = 1
while count < n:
    count = count + 1
    nFact *= count
print(f' {n}! =  {nFact}')
