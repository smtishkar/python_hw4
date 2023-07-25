# Напишите функцию для транспонирования матрицы. Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

import numpy as np


# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3],[4,5,6]]


def matrix_transposition(matrix : list) -> list:
    new_matrix =  [ [0]* len(matrix) for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range (len(matrix[0])):
            new_matrix[j][i]= matrix [i][j]
    return new_matrix

def print_matrix (matrix: list):
    for i in range(len(matrix)):
        for j in range (len(matrix[0])):
            print (matrix[i][j], end=' ')
        print()


print("Исходная матрица:")
print_matrix(matrix)
print("-"*30)
print("Результат транспонирования матрицы:")
print_matrix(matrix_transposition(matrix))
# print(np.matrix(matrix_transposition(matrix)))        # Если хотим использовать numpy