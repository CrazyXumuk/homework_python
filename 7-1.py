

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix


    def __str__(self):
        return '\n'.join('\t'.join([str(i) for i in j]) for j in self.matrix)


    def __add__(self, other):

        return Matrix([map(sum, zip(*t)) for t in zip(self.matrix, other.matrix)])



matrix_1 = Matrix([[31, 22, 0, 0], [37, 43, 0, 0], [51, 86, 0, 0]])

matrix_2 = Matrix([[3, 5, 32, 0], [2, 4, 6, 0], [-1, 64, -8, 0]])

matrix_3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1], [0, 0, 0, 0]])


print(matrix_1)
print()
print(matrix_2)
print()
print(matrix_3)
print()
print(f"matrix_1 + matrix_2 + matrix_3\n{matrix_1 + matrix_2 + matrix_3}")

