'''Задание 2

Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.

'''

f_2 = open('text_2.txt', encoding = 'utf-8')
content = f_2.readlines()
str_num = len(content)
print(f"Количество строк в данном файле равно {str_num}")
for el in content:
    num = content.index(el) + 1
    words = el.split()
    word_num = len(words)
    print(f"Количество слов в строке {num} равно {word_num}")
f_2.close()

# Почему-то когда пытаюсь дописать encoding = 'utf-8' программа выдает ошибку в строке с readlines и пишет
#...UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd1 in position 0: invalid continuation byte
# В чем проблема? Надо поменять кодировку в текстовом файле?