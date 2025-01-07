def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a

def get_lcm(a, b):
    return abs(a * b) // get_gcd(a, b)


if __name__ == "__main__":
    print(get_lcm(12, 15))
    print(get_lcm(36, 60))