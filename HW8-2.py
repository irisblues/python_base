'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.

'''
class ZeroDiv(Exception):
    def __init__(self, warn):
        self.warn = warn
div_x = int(input('Введите делимое>>> '))
div_y = int(input('Введите делитель>>> '))
try:
    if div_y == 0:
        raise ZeroDiv('перестаньте делить на ноль!!!')

except ZeroDiv as zero_div:
    print(zero_div)
else:
    result = (round(div_x / div_y, 2))
    print(f"При делении  {div_x} на {div_y} получится {result}")

