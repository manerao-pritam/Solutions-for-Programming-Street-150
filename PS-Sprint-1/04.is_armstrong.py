def is_armstrong(num):
    result, org = 0, num

    while num:
        digit = num % 10
        result += pow(digit, 3)
        num //= 10

    return result == org


if __name__ == "__main__":
    print(is_armstrong(153))
    print(is_armstrong(150))