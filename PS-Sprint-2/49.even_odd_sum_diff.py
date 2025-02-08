def get_diff(nums):
    even = odd = 0
    for num in nums:
        if num & 1:
            odd += num
        else:
            even += num

    return abs(odd - even)


if __name__ == '__main__':
    print(get_diff([1, 2, 3, 4, 5, 6]))