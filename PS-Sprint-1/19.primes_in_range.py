from math import isqrt


"""
Sieve algo -- prevents recomputing the same nums
"""
def get_primes_in_range(start, end):
    # primes = [1] * (end + 1)
    # primes[:2] = [0, 0]
    # 1 and 2 are NOT Primes
    primes = [0 if i < 2 else 1 for i in range(end + 1)]

    for p in range(2, isqrt(end) + 1):
        if primes[p]:
            for i in range(p * p, end + 1, p):
                primes[i] = 0

    return [num for num in range(start, end + 1) if primes[num]]


def get_primes_in_range1(start, end):
    def is_prime(num):
        if num < 2:
            return False

        if 2 <= num <= 3:
            return True

        if 0 in (num % 2, num % 3):
            return False

        for i in range(5, isqrt(num) + 1):
            if num % i == 0 or num % (i + 2) == 0:
                return False

        return True

    return [num for num in range(start, end + 1) if is_prime(num)]


if __name__ == "__main__":
    print(get_primes_in_range(10, 30))
    print(get_primes_in_range(1, 27))