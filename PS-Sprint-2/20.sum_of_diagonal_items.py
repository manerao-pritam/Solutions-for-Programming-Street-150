"""
LC 1572: Matrix Diagonal Sum
"""
def get_cross_diagonal_sum(mat):
    total = 0
    rows = len(mat)

    for r in range(rows):
        total += mat[r][r]

        if r != (rows - 1 - r):
            total += mat[r][rows - 1 - r]

    return total


def get_diagonal_sum(mat):
    result = 0

    for i in range(len(mat)):
        result += mat[i][i]

    return result


if __name__ == "__main__":
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(get_diagonal_sum(grid))

    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(get_cross_diagonal_sum(grid))