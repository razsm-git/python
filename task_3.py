class Cell:
    def __init__(self, count):
        self.count = count

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.count // rows)]) + '\n' + '*' * (self.count % rows)

    def __str__(self):
        return f'{self.count}'

    def __add__(self, other):
        return f"Сумма ячеек: {Cell(self.count + other.count)}"

    def __sub__(self, other):
        if (self.count - other.count) > 0:
            return f"Разность ячеек: {Cell(self.count - other.count)}"
        else:
            return f'В первой клетке меньше ячеек, чем во второй. Вычитание невозможно'

    def __mul__(self, other):
        return f"Умножение ячеек: {Cell(self.count * other.count)}"

    def __floordiv__(self, other):
        return f"Разность ячеек: {Cell(self.count // other.count)}"


cell1 = Cell(12)
cell2 = Cell(25)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 // cell2)
print(cell1.make_order(11))
