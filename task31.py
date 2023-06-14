# Задача №31. Решение в группах
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

def Fib(n):
    if n==0 or n==1:
        return 1
    return Fib(n-1)+Fib(n-2)
# list_1 = []
m = int(input('Введите какое число Фибоначчи нужно найти: '))
# for i in range(m+1):
#     list_1.append(Fib(i))
# print(list_1[m]) 
print(Fib(m))
