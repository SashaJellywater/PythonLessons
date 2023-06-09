# Задача №29. Общее обсуждение
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# Ваня:
n = int(input())
max_number = 1000      # ошибочно задано значение 1000 - какое число будет больше??? здесь ставим = n
while n != 0:
   n = int(input())
   if max_number > n:  # тут максимум постепенно будет становиться минимумом
     max_number = n
print(max_number)

# Петя:
n = int(input())
max_number = -1         # = n
while n < 0:       # неверно условие
   n = int(input())
   if max_number < n:
      n = max_number  # здесь любое значение n превратится в -1 и мы никогда не покинем цикл вайл
print(n)             # в выводе будет последнее введенное число, а не максимум
