'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.

'''
class Warehouse:
    pass

class Stationery:
    def __init__(self, name, manufacturer, price):
        self.name = name
        self.manufacturer = manufacturer
        self.price = price

class Printers(Stationery):
    def __init__(self, name, manufacturer, price, type_ink):
        super().__init__(name, manufacturer, price)
        self.type_ink = type_ink

class Scanner(Stationery):
    def __init__(self, name, manufacturer, price, resolution):
        super().__init__(name, manufacturer, price)
        self.resolution = resolution

class Xerox(Stationery):
    def __init__(self, name, manufacturer, price, color):
        super().__init__(name, manufacturer, price)
        self.color = color

a = Printers('c-500', 'hp', 22000, 'laser')
print(a.name)