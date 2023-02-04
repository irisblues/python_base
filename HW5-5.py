'''	Задание 5

Cоздать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
'''

sum_num = 0
str_list = input('введите числа через пробелы>>> ').split()
str_2 = '\n'.join(str_list)
with open('text_5.txt', 'w', encoding = 'utf-8') as numbers:
    numbers.writelines(str_2)
with open('text_5.txt', 'r', encoding = 'utf-8') as numbers:
    num = numbers.readlines()
    for i in num:
        sum_num += int(i)
    print(f"Сумма введенныхчисел {sum_num}")

'''
Пытаюсь сократить код через w+ и он перестает работать(( Что я делаю не так?
sum_num = 0
str_list = input('введите числа через пробелы>>> ').split()
str_2 = '\n'.join(str_list)
with open('text_5.txt', 'w+', encoding = 'utf-8') as numbers:
    numbers.writelines(str_2)
    num = numbers.readlines()
    for i in num:
        sum_num += int(i)
    print(f"Сумма введенныхчисел {sum_num}")

'''