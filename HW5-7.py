'''	Задание 7

Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.

name = ' '.join([data_list[1], data_list[0]])
name = data_list[1] + ' ' + data_list[0]
'''
import json
name_list = []
profit_list = []
total_profit_plus = 0
firm_profit = {}
with open('text_7.txt') as firms:
    for line in firms:
        data_list = line.split()
        name = ' '.join([data_list[1], data_list[0]])
        name_list.append(name)
        profit = float(data_list[2]) - float(data_list[3])
        profit_list.append(profit)
    profit_plus = [el for el in profit_list if el >= 0]
    for el in profit_plus:
        total_profit_plus += el
    average = round(total_profit_plus/len(profit_plus), 2)
    av_output = {'average_profit': average}
    for el in name_list:
        firm_info = {el: profit_list[name_list.index(el)]}
        firm_profit.update(firm_info)
    profit_output = [firm_profit, av_output]
    print(f"Названия фирм {name_list}")
    print(f"Профит фирм {profit_list}")
    print(f"общий профит {total_profit_plus}")
    print(f"Профит не убыточных {profit_plus}")
    print(f"Список словарей {profit_output}")
with open('profit_out.json', 'w', encoding='utf-8') as profit_j:
    json.dump(profit_output, profit_j)
# проверка:
json_str = json.dumps(profit_output)
print(json_str)
# видимо, проблема с кодировкой, но я не понимаю, как её решить(((

