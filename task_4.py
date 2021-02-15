class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Машина: {self.name}, цвет {self.color}, полицеская? Ответ: {self.is_police}')

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, direction):
        print(f"Машина {self.name} повернула {'налево' if direction == 0 else 'направо'}")

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.name} равна {self.speed}")


class SportCar(Car):
    pass


class TownCar(Car):
    def show_speed(self):
        print(f'Автомобиль {self.name}. {"Вы превышаете скорость!" if self.speed > 60 else f"Скорость: {self.speed}"}')


class WorkCar(Car):
    def show_speed(self):
        print(f'Автомобиль {self.name}. {"Вы превышаете скорость!" if self.speed > 40 else f"Скорость: {self.speed}"}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


t = TownCar(70, 'white', 'Ford')
t.go()
t.show_speed()
t.turn(0)
t.stop()

p = PoliceCar(80, 'black', 'Pontiac')
p.go()
p.show_speed()
p.turn(1)
p.stop()

s = SportCar(160, 'red', 'lamba')
s.go()
s.show_speed()
s.turn(1)
s.turn(2)
s.stop()

w = WorkCar(60, 'blue', 'Reno')
w.go()
w.show_speed()
w.turn(1)
w.turn(2)
w.stop()
