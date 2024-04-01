import numpy as np


class HashMixin:
    def __hash__(self):
        """
        Простейшая хэш-функция для матрицы.
        Вычисляется как сумма всех элементов матрицы по модулю 2^10.
        """
        return hash(np.sum(self._data) % (2**10))
    
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
    
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for row in self._data:
                f.write(' '.join(map(str, row)) + '\n')

    def __str__(self):
        return np.array2string(self._data)


class MatrixHash(Matrix, HashMixin):
    def __init__(self, data):
        self._data = data


A = MatrixHash([[1, 2], [3, 4]])
B = MatrixHash([[4, 3], [2, 1]])
C = MatrixHash([[2, 3], [4, 5]])
D = B

A.save_to_file("artifacts/3_3/A.txt")
B.save_to_file("artifacts/3_3/B.txt")
C.save_to_file("artifacts/3_3/C.txt")
D.save_to_file("artifacts/3_3/D.txt")

AB = A @ B
CD = C @ D
AB.save_to_file("artifacts/3_3/AB.txt")
CD.save_to_file("artifacts/3_3/CD.txt")

with open("artifacts/3_3/hash.txt", "w") as f:
    f.write(
        f"Hash of A: {hash(A)}\nHash of C: {hash(C)}\nHash of AB: {hash(AB)}\nHash of CD: {hash(CD)}"
    )
