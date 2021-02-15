class Road:
    def __init__(self, length, width, m_per_square, n):
        self._length = length
        self._width = width
        self.m_per_square = m_per_square
        self.n = n

    def calc(self):
        result = int((self._width * self._length * self.m_per_square * self.n) / 1000)
        print(
            f"При толщине слоя {self.n}см, на дорогу шириной {self._width}м и длиной {self._length}м потратят {result}т "
            f"асфальта.")


a = Road(5000, 20, 25, 5)
a.calc()
