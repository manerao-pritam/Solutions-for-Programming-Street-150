from math import isqrt


def is_perfect_num(num):
    divisors = {1}

    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)

    return sum(divisors) == num



if __name__ == "__main__":
    print(is_perfect_num(28))
    print(is_perfect_num(36))