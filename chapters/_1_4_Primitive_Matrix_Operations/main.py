# TODO Input Help Class
# Learn Strassen algorithm
# Hoare triple ex.: {P}A{Q}
from random import randrange
from numpy import*

def is_square_matrix(A):
    return len(A) == len(A[0])


def is_rect_matrix(A):
    return len(A) != len(A[0])

# TODO for bigger matrices ( define bigger ) use a different approach


def is_identity_matrix(A):
    if not is_square_matrix(A):
        return False
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i == j and A[i][j] != 1 or i != j and A[i][j] != 0:
                return False  # does not met the condition of identity matrix
    return True  # does met


def is_zero_matrix(A):
    if not is_square_matrix(A):
        return False
    for i in range(len(A)):
        for j in range(len(A[0])):
            if not A[i][j] == 0:
                return False
    return True  # does met


def is_upper_triangular_matrix(A):
    if not is_square_matrix(A):
        return False
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i > j and A[i][j] != 0:
                return False  # does not met the condition of upper triangular matrix
    return True  # does met


def is_lower_triangular_matrix(A):
    if not is_square_matrix(A):
        return False
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i < j and A[i][j] != 0:
                return False  # does not met the condition of lower triangular matrix
    return True  # does met

# Taking into account the notion of transposed matrix,
#  the symmetry condition may be written in the form of the equality A = Aᵗ


def is_symmetric_matrix(A):
    if not is_square_matrix(A):
        return False
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] != A[j][i]:
                return False  # does not met the condition of symmetric triangular matrix
    return True  # does met


def is_antisymmetric_matrix(A):
    if not is_square_matrix(A):
        return False
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] != A[j][i] * -1:

                return False  # does not met the condition of antisymmetric triangular matrix
    return True  # does met


def is_binary_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            if not (A[i][j] == 0 or A[i][j] == 1):
                return False  # does not met the condition of binary matrix
    return True  # does met


def is_valid_prod(A, B):
    return len(A[0]) == len(B)


def are_equal_matrices(A, B):
    if not len(A) == len(B) or not len(A[0]) == len(B[0]):
        return False
    for i in range(len(A)):
        for j in range(len(A[0])):
            if not A[i][j] == B[i][j]:
                return False  # does not met the condition of matrix equality
    return True  # does met


def are_commuting_matrices(A, B):
    if not is_square_matrix(A):
        return False  # Matrix to be commuting has to be a square matrix
    if not is_square_matrix(B):
        return False  # Matrix to be commuting has to be a square matrix
    if not len(A) == len(B):
        return False  # Matrices muss have same order

    AB = get_matrix_prod(A, B)
    BA = get_matrix_prod(B, A)

    if not are_equal_matrices(AB, BA):
        return False  # Matrices AB and BA Multiplication muss equal

    return True  # does match


def are_same_dim(A, B):
    return len(A) == len(B) and \
        len(A[0]) == len(B[0])


def get_transpose(A):
    # we get a zero matrix where B rows = A columns and B columns = A rows
    B = get_zero_matrix(len(A[0]), len(A))
    for i in range(len(A)):
        for j in range(len(A[0])):
            B[j][i] = A[i][j]  # we give to B columns the values of A rows
    return B


def get_matrix_main_diagonal(A):
    if is_square_matrix(A):
        B = []
        for i in range(len(A)):
            B.append(A[i][i])
        return B
    else:
        print('Matrix has to be a square Matrix')


def get_matrix_second_diagonal(A):
    if is_square_matrix(A):
        B = []
        for i in range(len(A)):
            B.append(A[i][len(A) - (i + 1)])
        return B
    else:
        print('Matrix has to be a square Matrix')

# if A and B are commuting, -commutator = Zero Matrix


def get_commutator_matrix(A, B):
    AB = get_matrix_prod(A, B)
    BA = get_matrix_prod(B, A)

    C = get_matrix_diff(AB, BA)
    return C


def get_zero_matrix(rows, columns):
    return [[0 for j in range(columns)]
            for i in range(rows)]


def get_matrix_sum(A, B):
    if are_same_dim(A, B):
        C = get_zero_matrix(len(A), len(A[0]))
        for i in range(len(A)):
            for j in range(len(A[0])):
                C[i][j] = A[i][j] + B[i][j]
        return C
    else:
        print('Can not performe addition on different matrix dimensions!')


def get_matrix_diff(A, B):
    if are_same_dim(A, B):
        C = get_zero_matrix(len(A), len(A[0]))
        for i in range(len(A)):
            for j in range(len(A[0])):
                C[i][j] = A[i][j] - B[i][j]
        return C
    else:
        print('Can not performe substraction on different matrix dimensions!')

# Matrix Multiplication is non-commutative


def get_matrix_prod(A, B):

    if is_valid_prod(A, B):  # A Column Size and B Row Size has to be equal
        C = get_zero_matrix(len(A), len(B[0]))
        for i in range(len(A)):  # rows A
            for j in range(len(B[0])):  # columns B
                sum = 0
                for k in range(len(B)):  # rows B
                    sum += A[i][k] * B[k][j]
                C[i][j] = sum
        return C
    else:
        print('Can not performe multiplication on different matrix row-column dimensions!')


def get_matrix_transpose(A):
    C = get_zero_matrix(A)
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[j][i] = A[i][j]
    return C

# Jacobi identity
# [[P,Q],R] + [[Q,R],P] + [[R,P],Q] = O

# trace of identity matrix n x n is equal to n
def get_matrix_trace(A):
    diagonal = get_matrix_main_diagonal(A)
    sum = 0
    for i in range(len(diagonal)):
        sum += diagonal[i]
    return sum

def get_identity_matrix(n):
    A = get_zero_matrix(n, n)
    for i in range(n):
        for j in range(n):
            temp = 0
            if i == j:
                temp = 1
            A[i][j] = temp
    return A

def get_random_matrix(max_m, max_n, max_value):
    m = randrange(max_m)
    n = randrange(max_n)
    A = get_zero_matrix(m, n)
    for i in range(m):
        for j in range(n):
            A[i][j] = randrange(max_value)
    return A

# TODO Constrain row input to maximal m size


def read_matrix_from_console():
    print('Enter Matrix Row Size:', end='')
    n = int(input())  # Number of Rows
    print('Enter Matrix Column Size:', end='')
    m = int(input())  # Number of Columns
    A = []

    for i in range(n):
        print('Enter numbers for row ', i, '(maximal ', m, ' ):', end='')
        row = input().split()  # Splits each input to a list, default separator is withespace
        for j in range(m):
            row[j] = int(row[j])
        A.append(row)  # Appens row inputs to List
    return A

# TODO Prettier print the matrix, like ||100  20||
#                                      ||  2 200||


def print_matrix_to_console(A):
    for row in A:
        print('||', end='')
        for index, element in enumerate(row):
            if index == len(row) - 1:
                print(element, end='')
            else:
                print(element, end=' ')
        print('||')


# A = get_random_matrix(100, 100, 2)
# print_matrix_to_console(A)


# I = get_identity_matrix(5)
# print_matrix_to_console(I)

# it = get_matrix_trace(I)
# print(it)


# A = read_matrix_from_console()
# print_matrix_to_console(A)

# print("Is Binary Matrix: ", is_binary_matrix(A))

# print("Is Identity Matrix: ", is_identity_matrix(A))

# B = get_matrix_second_diagonal(A)
# print(B)
# print(is_rect_matrix(A), is_square_matrix(A))
# B = get_transpose(A)
# print_matrix_to_console(B)

# B = read_matrix_from_console()
# print_matrix_to_console(B)

# C = get_matrix_prod(A, B)
# print_matrix_to_console(C)
