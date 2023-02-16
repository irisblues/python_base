'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
 В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год
 и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
 месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


'''
class DataClass:
    def __init__(self, date_str):
        self.date_str = date_str

    @property
    def date_str(self):
        return self.date_str

    @classmethod
    def div_date(cls, date_str):
        list_date = date_str.split('-')
        dd = int(list_date[0])
        mm = int(list_date[1])
        yyyy = int(list_date[2])
        return dd, mm, yyyy, f"тип данных {dd} - {type(dd)}, тип данных {mm} - {type(mm)}, тип данных {yyyy} - {type(yyyy)}"

    @staticmethod
    def val_date(date_str):
        list_date = date_str.split('-')
        dd = int(list_date[0])
        mm = int(list_date[1])
        yyyy = int(list_date[2])
        if 1 <= dd <= 31:
            if 1 <= mm <= 12:
                if 1950 <= yyyy <= 2022:
                    return f"Корректная дата"
                else:
                    return f"Некорректное значение года"
            else:
                return f"Некорректное значение месяца"
        else:
            return f"Некорректное значение дня"


print(DataClass.div_date('17-11-1983'))
print(DataClass.val_date('45-11-1983'))