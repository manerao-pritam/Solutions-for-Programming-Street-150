def get_digit_freq(num, digit):
    freq = 0

    while num:
        num, rem = divmod(num, 10)
        freq += (digit == rem)

    return freq


if __name__ == "__main__":
    print(get_digit_freq(1223333, 3))