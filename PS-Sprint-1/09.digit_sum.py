def digit_sum(num):
    result = 0

    while num:
        result += num % 10
        num //= 10

    return result


if __name__ == "__main__":
    print(digit_sum(1234))
    print(digit_sum(1000))
