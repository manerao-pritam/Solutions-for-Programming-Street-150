def get_single_digit_sum(num):
    while num >= 10:
        total = 0

        while num:
            num, digit = divmod(num, 10)
            total += digit

        num = total

    return num


if __name__ == "__main__":
    print(get_single_digit_sum(9875))
