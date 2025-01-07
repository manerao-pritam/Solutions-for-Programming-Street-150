from collections import deque
from math import isqrt


def get_all_divisors(num):
    divisors, large_divisors = [], deque()

    for i in range(1, isqrt(num) + 1):
        if num % i == 0:
            divisors += [i]

            if i != num // i:
                large_divisors.appendleft(num // i)

    return divisors + list(large_divisors)


if __name__ == "__main__":
    print(get_all_divisors(12))