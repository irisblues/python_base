"""Задание 5.

Реализовать класс Stationery (канцелярская принадлежность).

●	определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
●	создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
●	в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
●	создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"{self.title}: Отрисовка тонкой синей линии")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"{self.title}: Отрисовка тонкой чёрной линии")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"{self.title}: Отрисовка жирной зеленой линии")


pn = Pen('Ручка канцелярская')
pn.draw()
pl = Pencil('Карандаш автоматический')
pl.draw()
hl = Handle('Маркер зеленый 1,0')
hl.draw()
s = Stationery('Письменная принадлежность')
s.draw()