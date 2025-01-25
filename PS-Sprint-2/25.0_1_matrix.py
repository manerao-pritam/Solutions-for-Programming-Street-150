def get_0_1_matrix1(size):
    grid = [[0 for _ in range(size)] for _ in range(size)]
    value = 1

    for r in range(size):
        for c in range(size):
            value = int(not value)
            grid[r][c] = value

    return grid


"""
The (r + c) % 2 expression ensures the checkerboard pattern:
- When the sum of the row and column indices is even, it assigns 0.
- When the sum is odd, it assigns 1.
"""
def get_0_1_matrix(size):
    return [[(r + c) % 2 for c in range(size)] for r in range(size)]


def print_grid(grid):
    for row in grid:
        print(*row)



if __name__ == "__main__":
    grid = get_0_1_matrix(3)
    print_grid(grid)

    grid = get_0_1_matrix(5)
    print_grid(grid)