import numpy as np

class MatrixOperations:
    def __add__(self, other):
        return self.__class__(self._data + other._data)

    def __sub__(self, other):
        return self.__class__(self._data - other._data)

    def __mul__(self, other):
        return self.__class__(self._data * other._data)
    
    def __matmul__(self, other):
        return self.__class__(self._data @ other._data)

    def __truediv__(self, other):
        return self.__class__(self._data / other._data)

class MatrixIO:
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for row in self._data:
                f.write(' '.join(map(str, row)) + '\n')

    def __str__(self):
        return np.array2string(self._data)


class EnhancedMatrix(MatrixOperations, MatrixIO):
    def __init__(self, data):
        self._data = np.asarray(data)

    @property
    def matrix(self):
        return self._data

    @matrix.setter
    def matrix(self, value):
        self._data = np.array(value)

np.random.seed(0)
matrix1 = EnhancedMatrix(np.random.randint(0, 10, (10, 10)))
matrix2 = EnhancedMatrix(np.random.randint(0, 10, (10, 10)))

(matrix1 + matrix2).save_to_file("artifacts/3_2/matrix+.txt")
(matrix1 * matrix2).save_to_file("artifacts/3_2/matrix_mul.txt")
(matrix1 @ matrix2).save_to_file("artifacts/3_2/matrix@.txt")