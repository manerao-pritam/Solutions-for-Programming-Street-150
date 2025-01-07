def fib(n):
    if n in memo:
        return memo[n]

    # Recursively calculate fib(n) and store in memo to avoid redundant computation
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


if __name__ == "__main__":
    memo = {0: 0, 1: 1}
    print(fib(5))  # Output: 5
    print(*memo.values())