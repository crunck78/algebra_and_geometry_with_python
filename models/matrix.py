from select import select


class Matrix:
    """
    Matrix Like Object.
    A is 2d list of values
    """
    A = [[]]

    def __init__(self, m=0, n=0):
        self.A = self.get_zero_matrix(m, n)
    
    def __init__(self, m=0):
        self.m = m
        self.n = m

    def __init__(self, A):
        self.A = A
        self.m = len(A)
        self.n = len(A[0])

    def get_zero_matrix(rows, columns):
        return [[0 for j in range(columns)]
                for i in range(rows)]

    def print_matrix_to_console(self):
        """Prints a visual representation of Matrix A"""
        for row in self.A:
            print('||', end='')
            for index, element in enumerate(row):
                if index == len(row) - 1:
                    print(element, end='')
                else:
                    print(element, end=' ')
            print('||')
