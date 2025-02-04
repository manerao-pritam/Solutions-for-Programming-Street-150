def get_sum(n):
    if n <= 0:
        return 0

    first, second = 0, 1
    result = 1      # first + second

    for i in range(2, n + 1):
        first, second = second, first + second
        result += second

    return result

if __name__ == "__main__":
    print(get_sum(0))   # 0
    print(get_sum(5))   # 12
    print(get_sum(15))  # 1596