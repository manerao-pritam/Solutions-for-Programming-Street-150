def sum_of_series(num):
    total = 0

    for i in range(1, num + 1):
        total += (1 / i)

    return total


if __name__ == "__main__":
    print(sum_of_series(4))