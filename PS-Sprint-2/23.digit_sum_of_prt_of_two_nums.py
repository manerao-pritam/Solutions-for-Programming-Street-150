def get_digit_sum_of_prt_of_two_nums(a, b):
    prod = a * b

    if not prod:
        return 0

    if prod < 0:
        prod *= -1

    result = 0
    while prod:
        prod, rem = divmod(prod, 10)
        result += rem

    return result


if __name__ == "__main__":
    print(get_digit_sum_of_prt_of_two_nums(12, 34))
    print(get_digit_sum_of_prt_of_two_nums(10, 0))
    print(get_digit_sum_of_prt_of_two_nums(-1, -2))
    print(get_digit_sum_of_prt_of_two_nums(3, -4))