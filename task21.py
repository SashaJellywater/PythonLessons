# Задача №21.
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

bingo = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
 {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {"VIII":"S007"} ]
values = set()
for i in bingo:
    values.add(list(i.values())[0]) 
print(values)

# bingo = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#  {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {"VIII":"S007"} ]
# values = set()
# for i in bingo:
#     for key in i:
#         values.add(i[key])
# print(values)
