from random import randint


def generate_random_num_matrix(size):
    count, matrix = 1, []

    for r in range(size):
        row = []
        for c in range(size):
            row.append(count)
            count += 1

        matrix.append(row)

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(*row)
    print()


if __name__ == '__main__':
    print_matrix(generate_random_num_matrix(1))
    print_matrix(generate_random_num_matrix(2))
    print_matrix(generate_random_num_matrix(3))