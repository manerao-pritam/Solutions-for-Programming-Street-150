def get_prime_sum_in_range(start, end):
    primes = [1] * (end + 1)
    primes[:2] = [0, 0]

    for p in range(2, end+ 1):
        if primes[p]:
            for i in range(p * p, end + 1, p):
                primes[i] = 0

    # print([num for num in range(start, end) if primes[num]])
    return sum(num for num in range(start, end) if primes[num])


if __name__ == "__main__":
    print(get_prime_sum_in_range(1, 10))
    print(get_prime_sum_in_range(2, 23))