"""
List comprehension
"""
def get_count(num, key):
    if not num: return 0
    return sum(1 for digit in str(abs(num)) if int(digit) > key)

"""
Loop
"""
def get_count(num, key):
    count = 0
    num = abs(num)      # handling negatives
    while num:
        num, rem = divmod(num, 10)
        count += (rem > key)

    return count


if __name__ == '__main__':
    print(get_count(54321, 3) == 2)
    print(get_count(-54321, 3) == 2)
    print(get_count(0, 3) == 0)