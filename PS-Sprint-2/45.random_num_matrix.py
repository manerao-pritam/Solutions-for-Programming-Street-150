from random import randint

def generate_matrix(rows, cols):
    matrix = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(randint(1, 9))
        matrix.append(row)

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(*row)
    print()


if __name__ == '__main__':
    print_matrix(generate_matrix(rows = 2, cols = 3))
    print_matrix(generate_matrix(rows = 3, cols = 3))
    print_matrix(generate_matrix(rows = 1, cols = 1))