from math import isqrt


def sum_of_prime_factors(num):
    def get_prime_factors(n):
        prime_factors = []

        # Divide by 2 until n is even
        while n % 2 == 0:
            prime_factors.append(2)
            n //= 2

        # Divide by odd factors from 3 to sqrt(n) and step by 2
        for i in range(3, isqrt(n) + 1, 2):
            while n % i == 0:
                prime_factors.append(i)
                n //= i

        # If n > 2, it must be a prime number
        if n > 2:
            prime_factors.append(n)

        return prime_factors

    return sum(get_prime_factors(num))


if __name__ == "__main__":
    print(sum_of_prime_factors(12))