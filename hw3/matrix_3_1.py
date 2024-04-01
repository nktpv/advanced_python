import numpy as np


class Matrix:
    def __init__(self, data):
        self._data = data

    def _get_rows(self):
        return len(self._data)

    def _get_cols(self):
        return len(self._data[0])

    def _apply_operation(self, other, operation):
        if (
            self._get_rows() != other._get_rows()
            or self._get_cols() != other._get_cols()
        ):
            raise ValueError("Matrix dimensions must be the same")

        result = [
            [
                operation(self._data[i][j], other._data[i][j])
                for j in range(self._get_cols())
            ]
            for i in range(self._get_rows())
        ]
        return Matrix(result)

    def __add__(self, other):
        return self._apply_operation(other, lambda x, y: x + y)

    def __mul__(self, other):
        return self._apply_operation(other, lambda x, y: x * y)

    def __matmul__(self, other):
        if self._get_cols() != other._get_rows():
            raise ValueError(
                "Number of columns in the first matrix must be equal to the number of rows in the second matrix"
            )

        result = [
            [
                sum(self._data[i][k] * other._data[k][j] for k in range(self._get_cols()))
                for j in range(other._get_cols())
            ]
            for i in range(self._get_rows())
        ]
        return Matrix(result)


np.random.seed(0)
matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))

result_addition = matrix1 + matrix2
result_elementwise_mul = matrix1 * matrix2
result_matrix_mul = matrix1 @ matrix2

np.savetxt("artifacts/3_1/matrix+.txt", result_addition._data, fmt="%d")
np.savetxt("artifacts/3_1/matrix_mul.txt", result_elementwise_mul._data, fmt="%d")
np.savetxt("artifacts/3_1/matrix@.txt", result_matrix_mul._data, fmt="%d")
