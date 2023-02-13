'''2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''
from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def total_tissue(self):
        pass

class Coat(Clothes):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @property
    def total_tissue(self):
        return round(self.size/6.5 + 0.5, 2)

class Suit(Clothes):
    def __init__(self, name, height):
        self.name = name
        self.height = height

    @property
    def total_tissue(self):
        return round(2*self.height + 0.3, 2)

coat_001 = Coat('ref-001', 54)
print(f"Расход ткани на пальто {coat_001.name} размер {coat_001.size} - {coat_001.total_tissue} м")
suit_002 = Suit('ref-002', 1.8)
print(f"Расход ткани на костюм {suit_002.name} рост {suit_002.height} - {suit_002.total_tissue} м")

#создаем новый класс одежды, забыв создать там метод total_tissue
class Dress(Clothes):
    def __init__(self, name, size):
        self.name = name
        self.size = size

dress_003 = Dress('ref-003', 44)
print(dress_003.name)