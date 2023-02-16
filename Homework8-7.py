'''
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.

'''
class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.y = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма комплексных чисел равна')
        return f'y = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение комплексных чисел равно')
        return f'y = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'комплексное число y = {self.a} + {self.b} * i'


y_1 = ComplexNumber(1, -2)
y_2 = ComplexNumber(3, 4)
print(y_1)
print(y_1 + y_2)
print(y_1 * y_2)


