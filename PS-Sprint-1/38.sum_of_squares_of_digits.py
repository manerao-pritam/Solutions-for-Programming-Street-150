def get_sum_of_squares_of_digits(num):
    # return sum(int(n) ** 2 for n in str(num))

    total = 0
    while num:
        num, digit = divmod(num, 10)
        total += pow(digit, 2)

    return total

if __name__ == "__main__":
    print(get_sum_of_squares_of_digits(123))