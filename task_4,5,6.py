class Storage:
    list = [1, {'Имя товара': "", 'Кол-во': "", 'Сетевой': ""}]

    def __init__(self, n, count):
        self.n = n  # имя
        self.count = count  # кол-во

    def input(self):
        Storage.list[1]['Имя товара'] = self.n
        Storage.list[1]['Кол-во'] = self.count

    @staticmethod
    def show():
        for i in Storage.list:
            print(i)

    @staticmethod
    def move(name, count, where):
        Storage.list[1]['Имя товара'] = name
        Storage.list[1]['Кол-во'] = count
        Storage.list[1]['Местоположение:'] = where
        print(f'Перемещено в {where}')


class Org:
    def __init__(self, network):
        self.network = network

    def input(self):
        Storage.list[1]['Сетевой'] = self.network


class Printer(Org):
    def __init__(self, format_list):
        self.format_list = format_list

    def input(self):
        Storage.list[1]['Формат бумаги'] = self.format_list


class Scanner(Org):
    def __init__(self, dpi):
        self.dpi = dpi

    def input(self):
        Storage.list[1]['Разрешение dpi'] = self.dpi


class Xerox(Org):
    def __init__(self, speed):
        self.speed = speed

    def input(self):
        Storage.list[1]['Скорость копирования л/мин'] = self.speed


name = int(input('Меню.\nВыберите, что нужно добавить на склад:\n1.Принтер\n2.Сканер\n3.Xerox\n: '))
cou = int(input('Введите кол-во единиц: '))
net = int(input('Устройство сетевое?\n1.Да\n2.Нет\n: '))

if name == 1:
    f = int(input('Формат страниц:\n1.A4\n2.A3\n: '))
    if f == 1:
        f = 'A4'
    else:
        f = 'A3'
    if net == 1:
        net = True
    else:
        net = False
    var0 = Org(net)
    var0.input()
    var = Storage('Printer', cou)
    var2 = Printer(f)
    var.input()
    var2.input()
    var.show()
elif name == 2:
    d = int(input('Разрешение сканера:\n1.1024\n2.600\n: '))
    if d == 1:
        d = 1024
    else:
        d = 600
    if net == 1:
        net = True
    else:
        net = False
    var0 = Org(net)
    var0.input()
    var = Storage('Сканер', cou)
    var3 = Scanner(d)
    var.input()
    var3.input()
    var.show()
elif name == 3:
    x = int(input('Скорость копирования л/мин:\n1.50\n2.40\n: '))
    if x == 1:
        x = 50
    else:
        x = 40
    if net == 1:
        net = True
    else:
        net = False
    var0 = Org(net)
    var0.input()
    var = Storage('Xerox', cou)
    var4 = Xerox(x)
    var.input()
    var4.input()
    var.show()

var = Storage('Xerox', '2')
Storage.move('Xerox', '2', 'Office')
var.show()
