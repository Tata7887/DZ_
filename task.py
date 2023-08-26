'''
Создайте класс Матрица. Добавьте методы для: - вывода на печать,
сравнения,
сложения,
*умножения матриц
'''



class Matrix:

    def __init__(self, matr):
        self._matr = matr

    def get_matrix(self):
        return self._matr

    def __add__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            return f'Error: матрицы разных размеров'
        else:
            return Matrix([[self._matr[i][j] + other._matr[i][j] for j in range(len(self._matr[0]))] for i in range(len(self._matr))])

    def __mul__(self, other):
        if len(self._matr[0]) != len(other._matr):
            return f'Error: невозможно перемножить матрицы'
        else:
            mult_matr = [[sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*other._matr)] for i_row in self._matr]
            return Matrix(mult_matr)

    def __eq__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            return f'Error: матрицы разных размеров'
        else:
            for i in range(len(self._matr)):
                for j in range(len(self._matr[0])):
                    if self._matr[i][j] != other._matr[i][j]:
                        return False
            return True

    def __str__(self):
        s = ''
        for i in range(len(self._matr)):
            s += str(self._matr[i]) + '\n'
        return s

m_1 = [[5, 2, 1],
          [7, 4,  2],
          [5, 7, 9],
          [5, 5, 5]]

m_2 = [[1, 2, 1],
          [8, 5,  8],
          [2, 2,  2],
          [8, 8, 3]]

m_3 = [[9, 8, 7, 6],
          [5, 4, 3, 2],
          [1, 0, -1, -2]]


matr_1 = Matrix(m_1)
matr_2 = Matrix(m_2)
matr_3 = Matrix(m_3)


print ("Cложение матриц:")
matr_sum = matr_1 + matr_2
print(matr_sum)

print ("Умножение матриц:")
print(matr_1 * matr_3)


print ("Cравнение матриц:")
print(matr_1 == matr_1)
print(matr_3 == matr_2)

