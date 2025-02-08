def generate_pattern(rows):
    result = []

    for r in range(rows):
        row = []
        for c in range(rows):
            if r in (0, rows - 1):
                row.append("*")
            elif c in (0, rows - 1):
                row.append("*")
            else:
                row.append(" ")
        result.append(row)
    return result


def print_pattern(pattern):
    for row in pattern:
        print(*row)


if __name__ == '__main__':
    print_pattern(generate_pattern(1))
    print_pattern(generate_pattern(3))
    print_pattern(generate_pattern(5))
