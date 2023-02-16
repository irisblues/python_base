'''
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

'''
import numbers
from abc import ABC, abstractmethod

class NumCheck(Exception):
    def __init__(self, warn):
        self.warn = warn

class Warehouse:
    availability = {}

    def __str__(self):
        return f"В наличии на складе {Warehouse.availability}"

    @classmethod
    def get_item(cls, item, quantity):
        try:
            if isinstance(quantity, int) == False or quantity < 0:
                raise NumCheck('количество должно быть целым положительным числом, запрос отклонен')
        except NumCheck as nc:
            print(nc)
        else:
            last_quant = Warehouse.availability.get(item)
            if last_quant != None:
                quantity += last_quant
            return Warehouse.availability.update({item: quantity})

    @classmethod
    def give_item(cls, item, quantity, department):
        try:
            if isinstance(quantity, int) == False or quantity < 0:
                raise NumCheck('количество должно быть целым положительным числом, запрос отклонен')
        except NumCheck as nc:
            print(nc)
        else:
            last_quant = Warehouse.availability.get(item)
            if last_quant == None:
                print(f"{item} отсутствует на складе недостаточно, запрос отклонен.")
            elif last_quant < quantity or last_quant == None:
                print(f"Наличия на складе недостаточно, запрос на перемещение в {department} отклонен. B наличии {last_quant} шт. {item} ")
            else:
                print(f"Передано в {department} {item} - {quantity} шт ")
                quantity = last_quant - quantity
                Warehouse.availability.update({item: quantity})
                return Warehouse.availability


class Stationery(ABC):
    def __init__(self, name, manufacturer, price):
        self.name = name
        self.manufacturer = manufacturer
        try:
            if isinstance(price, numbers.Number) == False or price < 0:
                raise NumCheck(f"цена должна быть целым положительным числом. Цена {self.name} не записана")
        except NumCheck as nc:
            print(nc)
            self._price = None
        else:
            self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        try:
            if isinstance(value, numbers.Number) == False or value < 0:
                raise NumCheck(f"цена должна быть целым положительным числом. Цена {self.name} не записана")
        except NumCheck as nc:
            print(nc)
        else:
            self._price = value

    @abstractmethod
    def store_name(self):
        return f"{self.name} ({self.manufacturer}) - {self.price}"

class Printers(Stationery):
    def __init__(self, name, manufacturer, price, type_ink):
        super().__init__(name, manufacturer, price)
        self.type_ink = type_ink

    @property
    def store_name(self):
        return f"{self.name} ({self.manufacturer}) - {self.price}"

class Scanners(Stationery):
    def __init__(self, name, manufacturer, price, charge_port):
        super().__init__(name, manufacturer, price)
        self.charge_port = charge_port

    @property
    def store_name(self):
        return f"{self.name} ({self.manufacturer}) - {self.price}"

class Xerox(Stationery):
    def __init__(self, name, manufacturer, price, color):
        super().__init__(name, manufacturer, price)
        self.color = color

    @property
    def store_name(self):
        return f"{self.name} ({self.manufacturer}) - {self.price}"

#создаем экземпляры, проверяем валидность price- сделала через try-exept, чтобы не было аварийного завершения
x_1 = Xerox('c-500', 'HP', -22000, 'color')
x_2 = Xerox('a-450', 'Pantum', 15000, 'b/w')
p_1 = Printers('d-003-las', 'HP', 8000, 'laser')
s_1 = Scanners('FG-05', 'Epson', 6800, 'usb')
#проверяем валидность price в клиентском коде
x_1.price = '22000'
x_1.price = 22000

#проверяем метод добавления экземпляров на склад
print(Warehouse())
Warehouse.get_item(x_1.store_name, 7)
print(Warehouse())
Warehouse.get_item(s_1.store_name, 10)
print(Warehouse())
#проверяем валидность количества экземпляров при добавлении на склад
Warehouse.get_item(p_1.store_name, -15)
print(Warehouse())

#проверяем метод передачи экземпляров со склада в другие отделы
Warehouse.give_item(s_1.store_name, 5, 'отдел Бухгалтерия')
print(Warehouse())
Warehouse.give_item(x_1.store_name, 8, 'отдел Логистики')
print(Warehouse())

# проверяем работу абстрактного класса
class Phone(Stationery):
    pass

ph = Phone()