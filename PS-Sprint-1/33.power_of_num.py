def power(base, exp):
    # return base ** exp
    # return pow(base, exp)

    for i in range(1, exp - 1):
        base *= base

    return base

if __name__ == "__main__":
    print(power(2, 3))