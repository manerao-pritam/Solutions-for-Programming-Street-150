from collections import deque
from math import isqrt


def get_divisors(a, b):
    def helper(num):
        divisors, large_divisors = [], deque()

        for i in range(1, isqrt(num) + 1):
            if num % i == 0:
                divisors.append(i)

                if i != num // i:
                    large_divisors.appendleft(num // i)

        return divisors + list(large_divisors)


    if not a or not b:
        return []

    return helper(a * b)


if __name__ == "__main__":
    print(get_divisors(6, 10))