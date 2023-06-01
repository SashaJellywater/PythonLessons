# Задача №11.
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6
A = int(input("Введите целое неотрицательное число: "))
count = 2
if A == 0:
    print(1)
if  A == 1:
    print("2 or 3")
else:
    fib1 = 0
    fib2 = 1
    while A > fib2:
        temp = fib2
        fib2 = fib1 + fib2
        fib1 = temp
        count += 1
    if A == fib2:
        print(count)
    else:
        print(-1)

# A = int(input("Введите целое неотрицательное число: "))
# count = 2
# if A == 1:
#     print("2 or 3")
# else:
#     fib1 = 0
#     fib2 = 1
#     while A > fib2:
#         temp = fib2
#         fib2 = fib1 + fib2
#         fib1 = temp
#         count += 1
#         if fib2 > A:
#             count = 0
#     if count != 0:
#         print(count)
#     else:
#         print(-1)

