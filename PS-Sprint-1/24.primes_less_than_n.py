from math import isqrt

"""
T.C.: O(n log(log n))
"""
def get_primes_less_than_n(n):
    primes = [1] * (n + 1)
    primes[:2] = [0, 0]         # 0 and 1 are NOT primes

    for p in range(2, isqrt(n) + 1):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = 0

    return [num for num in range(n + 1) if primes[num]]


if __name__ == "__main__":
    print(get_primes_less_than_n(20))