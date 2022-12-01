import gauss_jordan.jordan_gauss as gauss_jordan


def get_unit_matrix(n: int) -> list:
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(matrix)):
        matrix[i][i] = 1
    return matrix


def get_expanded_matrix(matrix: list) -> list:
    result_matrix = matrix.copy()
    identity_matrix = get_unit_matrix(len(matrix))
    for i in range(len(matrix)):
        result_matrix = gauss_jordan.get_expanded_matrix(matrix, identity_matrix[i])
    return result_matrix


def get_inverse_matrix(matrix: list) -> list:
    expanded_matrix = get_expanded_matrix(matrix)
    expanded_matrix = gauss_jordan.forward_stroke(expanded_matrix)
    expanded_matrix = gauss_jordan.backward_stroke(expanded_matrix)
    inverse_matrix = []
    print(expanded_matrix)
    for i in range(len(matrix)):
        inverse_matrix.append(expanded_matrix[i][len(matrix):])

    return inverse_matrix


def get_roots(a_matrix: list, b_matrix: list) -> list:
    a_matrix = get_inverse_matrix(a_matrix)
    roots = []
    for row in a_matrix:
        temp = 0
        for j in range(len(a_matrix[0])):
            temp += b_matrix[j] * row[j]
        roots.append(temp)
    return roots
