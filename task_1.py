'''
Напишите функцию для транспонирования матрицы
'''

matrix = [[1, 3, 5], [8, 6, 2]]


def matrix_transposition(matrix):
    trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    return trans_matrix


print(matrix_transposition(matrix))
