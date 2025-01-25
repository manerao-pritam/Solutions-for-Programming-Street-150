def spiral_pattern_matrix(size):
    grid = [[0 for _ in range(size)] for _ in range(size)]

    counter = 1
    rows = cols = size
    r, c, direction = 0, -1, 1

    while rows and cols:
        for _ in range(cols):
            c += direction
            grid[r][c] = counter
            counter += 1
        rows -= 1

        for _ in range(rows):
            r += direction
            grid[r][c] = counter
            counter += 1
        cols -= 1

        direction *= -1

    return grid


def print_matrix(mat):
    for row in mat:
        print(*row)


if __name__ == "__main__":
    print_matrix(spiral_pattern_matrix(3))
    print_matrix(spiral_pattern_matrix(5))