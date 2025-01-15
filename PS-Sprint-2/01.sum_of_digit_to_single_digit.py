def sum_of_digits_to_single_digit(num):
    while num >= 10:
        total = 0
        while num:
            num, digit = divmod(num, 10)
            total += digit

        num = total

    return num


if __name__ == "__main__":
    print(sum_of_digits_to_single_digit(123))
    print(sum_of_digits_to_single_digit(1234))
    print(sum_of_digits_to_single_digit(12345))