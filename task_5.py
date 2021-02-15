class Stationery:
    def __init__(self, title=None):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Отрисовка чернилами c помощью ручки {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисунок карандашом фирмы {self.title}')


class Handle(Stationery):
    def draw(self):
        print('Ручная отрисовка')


a = Stationery()
a.draw()
b = Pen('Parker')
b.draw()
c = Pencil('Graffiti')
c.draw()
d = Handle()
d.draw()
