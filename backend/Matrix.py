class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices must have the same dimensions for addition.")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def __sub__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices must have the same dimensions for subtraction.")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append(self.matrix[i][j] - other.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other):
        if self.columns != other.rows:
            raise ValueError("The number of columns in the first matrix must match the number of rows in the second matrix for multiplication.")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.columns):
                element = 0
                for k in range(self.columns):
                    element += self.matrix[i][k] * other.matrix[k][j]
                row.append(element)
            result.append(row)
        return Matrix(result)

    def determinant(self):
        if self.rows != self.columns:
            raise ValueError("Matrix must be square for determinant.")
        if self.rows == 1:
            return self.matrix[0][0]
        elif self.rows == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        else:
            det = 0
            for i in range(self.columns):
                det += ((-1) ** i) * self.matrix[0][i] * self.submatrix(0, i).determinant()
            return det

    def submatrix(self, row, column):
        sub = []
        for i in range(self.rows):
            if i != row:
                subrow = []
                for j in range(self.columns):
                    if j != column:
                        subrow.append(self.matrix[i][j])
                sub.append(subrow)
        return Matrix(sub)

    def transpose(self):
        result = []
        for j in range(self.columns):
            row = []
            for i in range(self.rows):
                row.append(self.matrix[i][j])
            result.append(row)
        return Matrix(result)


matrix1 = Matrix([[1, 2], [3, 4]])
matrix2 = Matrix([[5, 6], [7, 8]])

sum_matrix = matrix1 + matrix2
print(sum_matrix)

diff_matrix = matrix1 - matrix2
print(diff_matrix)

product_matrix = matrix1 * matrix2
print(product_matrix)

determinant = matrix1.determinant()
print(determinant)
