def print_pattern(rows):
    result = []

    for r in range(1, rows + 1):
        spaces = " " * (rows - r)
        stars = "*" * (2 * r - 1)
        print(spaces + stars)


if __name__ == '__main__':
    print_pattern(3)