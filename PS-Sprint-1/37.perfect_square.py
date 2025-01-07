from math import isqrt


def is_perfect_square(n):
    tmp = isqrt(n)
    return tmp * tmp == n



if __name__ == "__main__":
    print(is_perfect_square(16))
    print(is_perfect_square(15))