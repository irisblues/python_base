'''	Задание 3

Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.

'''

with open('text_3.txt') as my_file:
    salary = []
    less_20 = []
    sum_sal = 0
    list_empl = my_file.readlines()
    for i in list_empl:
        i = i.split()
        salary.append(i[1])
        sal = float(i[1])
        if sal < 20000:
            less_20.append(i[0])
    for el in salary:
        sum_sal += float(el)
    mean_sal = round((sum_sal / len(salary)), 2)

print(f"Cредний оклад: {mean_sal}, сотрудники с окладом меньше 20000:{less_20}")
