def generate_pattern(size):
    matrix = []

    for r in range(size):
        row = []
        for c in range(r + 1):
            row.append("*")

        matrix.append(row)

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(*row)
    print()


if __name__ == '__main__':
    print_matrix(generate_pattern(1))
    print_matrix(generate_pattern(2))
    print_matrix(generate_pattern(4))