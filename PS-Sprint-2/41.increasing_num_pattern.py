def generate_patter(rows):
    result = []
    for r in range(rows):
        count = 1
        row = []
        for c in range(r + 1):
            row.append(count)
            count += 1
        result.append(row)

    return result


def print_pattern(pattern):
    for row in pattern:
        print(*row)


if __name__ == '__main__':
    print_pattern(generate_patter(3))
    print_pattern(generate_patter(0))
    print_pattern(generate_patter(10))