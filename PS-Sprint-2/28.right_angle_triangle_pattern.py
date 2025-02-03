def generate_pattern(height):
    for r in range(1, height + 1):
        for n in range(1, r + 1):
            print(n, end=" ")
        print()



if __name__ == "__main__":
    generate_pattern(4)
    generate_pattern(7)
    generate_pattern(10)
