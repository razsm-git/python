class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.num = complex(self.x, self.y)

    def __add__(self, other):
        return f'Результат сложения: {self.num + other.num}'

    def __mul__(self, other):
        return f'Результат умножения: {self.num * other.num}'


a = Complex(1, 2)
b = Complex(3, 4)
print(a + b)
print(a * b)
