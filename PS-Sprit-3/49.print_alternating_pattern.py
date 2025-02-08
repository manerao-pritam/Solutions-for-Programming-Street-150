def generate_pattern(size):
    result = []

    for i in range(size):
        if i & 1 == 0:
            row = ['1'] * size
        else:
            row = ['2'] * size

        result.append(row)

    return result


def print_pattern(pattern):
    for row in pattern:
        print(*row)


if __name__ == '__main__':
    size = int(input("Enter the size of the pattern: "))
    print_pattern(generate_pattern(size))