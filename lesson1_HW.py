#1. Написать цикл для выведения на экран каждой буквы своего ФИО.
my_name = 'Бескина Мария Васильевна'
for el in my_name:
  print(el)

#2.Написать функцию для перевода доллара в евро c округлением до 2х знаков после запятой,
# если известно, что текущий курс составляет 1.17 долларов за один евро.
def dollar_euro_convert(dollar):
  return round(dollar/1.17, 2)


print(dollar_euro_convert(117))
