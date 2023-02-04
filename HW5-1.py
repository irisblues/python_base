'''Задание 1

Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.

'''

f_1 = open('text_1.txt', 'w', encoding = 'utf-8')
new_line = input('Введите текст>>> ')
while new_line:
    f_1.write(new_line)
    f_1.write("\n")
    new_line = input('Введите текст>>>')
    if not new_line:
        break
f_1.close()

# проверка:
f_1 = open('text_1.txt', 'r', encoding = 'utf-8')
content = f_1.read()
print(content)
f_1.close()

