from math import isqrt


def get_sum_of_n_primes(n):
    def is_prime(num):
        if num <= 1:
            return False

        if num == 2:
            return True

        if num % 2 == 0:
            return False

        for i in range(3, isqrt(num) + 1, 2):
            if num % i == 0:
                return False

        return True

    primes_count, num = 0, 2
    result = 0

    while primes_count < n:
        if is_prime(num):
            primes_count += 1
            result += num
        num += 1

    return result


if __name__ == "__main__":
    print(get_sum_of_n_primes(1000))
