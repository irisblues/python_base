"""Задание 4.

4.	Реализуйте базовый класс Car.

●	у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
●	опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
●	добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
●	для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.


"""

class Car:
    def __init__(self, color, name, speed = 0, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn_right(self):
        print('Машина повернула направо')

    def turn_left(self):
        print('Машина повернула налево')

    def show_speed(self):
        print(f"Скорость движения {self.speed} км/ч")

#Проверка
c = Car('black', 'BMW', 100)
print(c.__dict__)
c.turn_left()
c.show_speed()

class TownCar(Car):
    def __init__(self, color, name, speed, is_police = False):
        super().__init__(color, name, speed, is_police)

    def show_speed(self):
        if int(self.speed) > 60:
            print(f"Превышение скорости! Ваша скорость {self.speed} км/ч")
        else:
            print(f"Скорость движения {self.speed} км/ч")


class SportCar(Car):
    def __init__(self, color, name, speed = 0, is_police = False):
        super().__init__(color, name, speed, is_police)


class WorkCar(Car):
    def __init__(self, color, name, speed, is_police = False):
        super().__init__(color, name, speed, is_police)

    def show_speed(self):
        if int(self.speed) > 40:
            print(f"Превышение скорости! Ваша скорость {self.speed} км/ч")
        else:
            print(f"Скорость движения {self.speed} км/ч")


class PoliceCar(Car):
    def __init__(self, color, name, speed = 0, is_police = True):
        super().__init__(color, name, speed, is_police)

#проверка
tc = TownCar('blue', 'Subaru', 110)
print(f"Характеристики TownCar: {tc.__dict__}")
tc.go()
tc.stop()
tc.turn_right()
tc.show_speed()
sc = SportCar('red', 'Ferrary', 200)
print(f"Характеристики SportCar: {sc.__dict__}")
sc.go()
sc.show_speed()
wc = WorkCar('grey', 'Белаз', 40)
print(f"Характеристики WorkCar: {wc.__dict__}")
wc.turn_right()
wc.show_speed()
pc = PoliceCar('white', 'Ford')
print(f"Характеристики PoliceCar: {pc.__dict__}")
pc.stop()
pc.show_speed()
