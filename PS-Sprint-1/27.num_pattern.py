def print_num_pattern1(rows):
    count = 1
    for r in range(rows):
        for c in range(r + 1):
            print(count, end=" ")
            count += 1
        print()


def print_num_pattern(rows):
    count = 1
    for r in range(1, rows + 1):
        print(" ".join(map(str, range(count, count + r))))
        count += r



if __name__ == "__main__":
    print_num_pattern(3)
