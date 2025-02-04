def get_matrix(size):
    mat = [[0 for _ in range(size)] for _ in range(size)]

    for r in range(size):
        for c in range(r + 1):
            mat[r][c] = 1

    return mat

"""
One-liner
"""
def get_matrix1(size):
    return [[1 if c <= r else 0 for c in range(size)] for r in range(size)]


def print_matrix(mat):
    for row in mat:
        print(*row)
    print()


if __name__ == "__main__":
    print_matrix(get_matrix(0))
    print_matrix(get_matrix(1))
    print_matrix(get_matrix(4))
    print_matrix(get_matrix(6))