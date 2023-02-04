'''	Задание 6

Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие лекционных,
практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —

Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


'''
subjects = []
hours = []
tot_hours = []
subject_time = {}
with open('text_6.txt') as classes:
    list_classes = classes.readlines()
    for el in list_classes:
        el1 = el.split(' ', 1)
        subjects.append(el1[0])
        hours.append(el1[1])
    for el in hours:
        sum = 0
        el = el.replace('(', ' ')
        el = el.split(' ')
        for i in el:
            if el.index(i) % 2 == 0:
                sum += int(i)
        tot_hours.append(sum)
    for el in subjects:
        new_dict = {el: tot_hours[subjects.index(el)]}
        subject_time.update(new_dict)
print(subject_time)
