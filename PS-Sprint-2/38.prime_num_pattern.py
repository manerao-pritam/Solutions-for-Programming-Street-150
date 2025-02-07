from math import isqrt


def generate_prime_pattern(size):
    """
    Generate a pattern of primes where each row i contains the first i+1 primes.
    """
    def is_prime(num):
        if num < 2: return False
        if num in (2, 3): return True

        if 0 in (num % 2, num % 3):         # if divisible by 2 or 3
            return False

        i = 5                               # 5 is the next prime
        while i <= isqrt(num):
            if num % i == 0 or num % (i + 2) == 0:
                return False

            i += 6                          # 6 because anything before that would be divisible by 2, 3, or 5

        return True

    def get_primes(size):
        num = 2         # 2 is the first prime num
        while True:
            if is_prime(num):
                primes.append(num)

                if len(primes) == size:
                    break

            num += 1

    primes = []
    get_primes(size)

    # pattern
    result = []
    for i in range(size):
        row = []
        for j in range(i + 1):
            row.append(primes[j])

        result.append(row)

    return result


def print_pattern(pattern):
    for row in pattern:
        print(*row)


if __name__ == '__main__':
    print_pattern(generate_prime_pattern(3))
    print_pattern(generate_prime_pattern(10))