# Задача №3.
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32
print("Введите количество учеников в первом классе")
firstClass = int(input())
print("Введите количество учеников во втором классе")
secondClass = int(input())
print("Введите количество учеников в третьем классе")
therdClass = int(input())
classTables = int(
    firstClass / 2
    + firstClass % 2
    + secondClass / 2
    + secondClass % 2
    + therdClass / 2
    + therdClass % 2
)
print(f"Для трех новых классов потребуется {classTables} парты/парт")
# countStudents1 = int(input("Введите кол-во учеников в 1-ом кабинете: "))
# countStudents2 = int(input("Введите кол-во учеников в 2-ом кабинете: "))
# countStudents3 = int(input("Введите кол-во учеников в 3-ом кабинете: "))
# part = (countStudents1 // 2 + countStudents1 % 2) + (countStudents2 // 2 + countStudents2 % 2) + (countStudents3 // 2 + countStudents3 % 2)
# print(part)
