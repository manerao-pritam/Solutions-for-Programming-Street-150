from math import isqrt


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def get_largest_prime_factor(num):
    if num <= 1:
        return None  # No prime factors for numbers <= 1

    # Check from the largest possible factor downwards
    for i in range(isqrt(num), 1, -1):
        if num % i == 0:  # Found a factor
            if is_prime(num // i):  # Check the larger factor first
                return num // i

            if is_prime(i):  # Check the smaller factor
                return i

    # no factors found, the number itself is prime
    return num


if __name__ == "__main__":
    print(get_largest_prime_factor(28))  # Output: 7
    print(get_largest_prime_factor(29))  # Output: 29 (29 is prime)
    print(get_largest_prime_factor(1))   # Output: None (no prime factors)
    print(get_largest_prime_factor(2))   # Output: 2 (2 is prime)
    print(get_largest_prime_factor(13195))  # Output: 29