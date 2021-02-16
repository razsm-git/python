m1 = [[1, 3], [4, 5]]
m2 = [[7, 8], [9, 10]]


class Matrix:
    def __init__(self, mat):
        self.mat = mat

    def __add__(self, other):
        m3 = []
        for i in range(len(self.mat)):
            m3.append([])
            for j in range(len(self.mat[0])):
                result = self.mat[i][j] + other.mat[i][j]
                m3[i].append(result)
        return '\n'.join(map(str, m3))

    def __str__(self):
        return f"Объект с параметрами {self.mat}"


a = Matrix(m1)
b = Matrix(m2)
print(a)
print(b)
print(f'Сумма двух матриц.\nНовая матрица:\n{a + b}')
