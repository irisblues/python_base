'''	Задание 4

Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.


'''
transl = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре', 'Five' : 'Пять'}
rus_num = []

with open('text_4.txt', 'r', encoding = 'utf-8') as numbers:
    for i in numbers:
        i = i.split(' ', 1)
        rus_num.append(transl[i[0]] + ' ' + i[1])
with open('text_4_new.txt', 'w', encoding = 'utf-8') as numbers_2:
    numbers_2.writelines(rus_num)

with open('text_4_new.txt', 'r', encoding = 'utf-8') as numbers_2:
    for line in numbers_2:
        print(line)