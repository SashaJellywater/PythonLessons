# Задача №27. 
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов или символами конца строки.Определите,
# сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore. The shells that she sells are sea shells I'm sure. 
# So if she sells sea shells on the sea shore, I'm sure that the shells are sea shore shells.
# Output: 19

text = input('Введите текст: ').lower().split()
print(text)
text = set(text)
# count = 0
# for i in text:
#     count+=1
# print(count)
print(len(text))

