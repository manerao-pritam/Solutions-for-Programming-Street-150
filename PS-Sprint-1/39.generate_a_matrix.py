def get_grid(size):
    grid = [[0] * size for _ in range(size)]

    count = 1
    for r in range(size):
        for c in range(size):
            grid[r][c] = count
            count += 1

    # # printing
    # for row in grid:
    #     print(row)

    return grid


if __name__ == "__main__":
    print(*get_grid(3))