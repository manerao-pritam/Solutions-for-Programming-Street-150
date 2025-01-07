def get_gcd(m, n):
    while n != 0:
        m, n = n, m % n

    return m


if __name__ == "__main__":
    print(get_gcd(12, 15))
    print(get_gcd(36, 60))