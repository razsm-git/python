class Stationery:
    title = 'name'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Отрисовка чернилами')


class Pencil(Stationery):
    def draw(self):
        print('Рисунок карандашом')


class Handle(Stationery):
    def draw(self):
        print('Ручная отрисовка')


a = Stationery()
a.draw()
b = Pen()
b.draw()
c = Pencil()
c.draw()
d = Handle()
d.draw()
