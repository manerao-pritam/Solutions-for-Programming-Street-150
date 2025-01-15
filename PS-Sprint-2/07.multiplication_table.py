"""
more pythonic way
"""
def multiplication_table(num):
    grid = []

    for r in range(1, num + 1):
        row = [r * c for c in range(1, num + 1)]  # Generate the row i.e. curr row num * col from 1 -> n
        grid += [row]

    return grid


def multiplication_table1(num):
    grid = [[0] * num for _ in range(num)]

    # fill rows
    count = 1
    for r in range(num):
        grid[r][0] = count
        count += 1

    # fill cols
    count = 1
    for c in range(num):
        grid[0][c] = count
        count += 1

    # fill remaining cells
    for r in range(1, num):
        for c in range(1, num):
            grid[r][c] = grid[0][c] * grid[r][0]

    return grid

if __name__ == "__main__":
    print(multiplication_table(3))
