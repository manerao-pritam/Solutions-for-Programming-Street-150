from math import isqrt


def is_prime(num):
    if num <= 2:
        return False

    for n in range(3, isqrt(num)):
        if num % n == 0:
            return False

    return True


if __name__ == "__main__":
    print(is_prime(11))
    print(is_prime(7))
    print(is_prime(1456))