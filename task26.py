# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

num = int(input('Введите число: '))
st = int(input('Введите степень: '))
def qwerty(n,m):
    if m==0:
        return (1)
    return n*qwerty(n,m-1)
print(qwerty(num,st))