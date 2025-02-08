def generate_pattern(rows):
    result = []

    for r in range(1, rows + 1):
        spaces = " " * (rows - r)
        stars = "*" * (2 * r - 1)
        result.append(spaces + stars)

    for r in range(rows - 1, 0, -1):
        spaces = " " * (rows - r)
        stars = "*" * (2 * r - 1)
        result.append(spaces + stars)

    return result


def print_pattern(pattern):
    for row in pattern:
        print(*row)


if __name__ == '__main__':
    print_pattern(generate_pattern(3))