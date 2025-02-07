"""
Formula
"""
def get_sum(n):
    # /2 (in n + (n + 1) / 2) means the odds
    return n * (n + 1)


"""
Range
"""
def get_sum(n):
    # n evens = 2 * n + 1
    return sum(range(2, 2 * n + 1, 2));


"""
Loop
"""
def get_sum(n):
    count = result = 0
    i = 2
    while True:
        if count == n:
            break

        result += i
        count += 1
        i += 2

    return result


if __name__ == '__main__':
    print(get_sum(4) == 20)
    print(get_sum(10) == 110)
    print(get_sum(1) == 2)
    print(get_sum(12) == 156)
