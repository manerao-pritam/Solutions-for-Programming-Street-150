def get_digit_count(num):
    # return len(str(num))

    count = 0
    while num:
        count += 1
        num //= 10

    return count



if __name__ == "__main__":
    print(get_digit_count(12345))