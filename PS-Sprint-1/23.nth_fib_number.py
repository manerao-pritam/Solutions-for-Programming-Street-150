def get_nth_fib_number(n):
    if 0 <= n <= 1:
        return n

    first, second = 0, 1
    for _ in range(2, n + 1):
        first, second = second, first + second

    return second


if __name__ == "__main__":
    print(get_nth_fib_number(5))
    print(get_nth_fib_number(20))
    print(get_nth_fib_number(200))
    print(get_nth_fib_number(300))
