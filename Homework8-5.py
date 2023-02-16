'''
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).

'''
class Warehouse:
    availability = {}

    def __str__(self):
        return f"В наличии на складе {Warehouse.availability}"

    @classmethod
    def get_item(cls, item, quantity):
        last_quant = Warehouse.availability.get(item)
        if last_quant != None:
            quantity += last_quant
        return Warehouse.availability.update({item: quantity})

    @classmethod
    def give_item(cls, item, quantity, department):
        last_quant = Warehouse.availability.get(item)
        if last_quant < quantity:
            print(f"Наличия на складе недостаточно, запрос отклонен. B наличии {last_quant} шт. {item} ")

        else:
            print(f"Передано в {department} {item} - {quantity} шт ")
            quantity = last_quant - quantity
            Warehouse.availability.update({item: quantity})
            return Warehouse.availability

class Stationery:
    def __init__(self, name, manufacturer, price):
        self.name = name
        self.manufacturer = manufacturer
        self.price = price

class Printers(Stationery):
    def __init__(self, name, manufacturer, price, type_ink):
        super().__init__(name, manufacturer, price)
        self.type_ink = type_ink

    def __str__(self):
        return f"{self.name} ({self.manufacturer}) - {self.price}"

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

x_1 = Xerox('c-500', 'HP', 22000, 'color')
x_2 = Xerox('a-450', 'Pantum', 15000, 'b/w')
p_1 = Printers('d-003-las', 'HP', 8000, 'laser')
s_1 = Scanners('FG-05', 'Epson', 6800, 'usb')

print(Warehouse())
Warehouse.get_item(x_2.store_name, 7)
print(Warehouse())
Warehouse.get_item(s_1.store_name, 10)
print(Warehouse())
Warehouse.get_item(p_1.store_name, 15)
print(Warehouse())
Warehouse.give_item(s_1.store_name, 5, 'отдел Бухгалтерия')
print(Warehouse())
Warehouse.give_item(x_2.store_name, 8, 'отдел Логистики')
print(Warehouse())

