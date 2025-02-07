def get_sum(num):
    return sum(n * n for n in range(2, num + 1, 2))


if __name__ == '__main__':
    print(get_sum(4))