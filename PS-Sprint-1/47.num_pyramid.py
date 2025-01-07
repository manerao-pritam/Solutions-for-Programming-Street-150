def num_pyramid(rows):
    for r in range(1, rows + 1):
        for c in range(1, r + 1):
            print(c, end=" ")
        print()


if __name__ == "__main__":
    print(num_pyramid(4))
