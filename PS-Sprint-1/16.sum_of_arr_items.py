def get_total(nums):
    # return sum(num for num in nums)

    total = 0

    for num in nums:
        total += num

    return total


if __name__ == "__main__":
    print(get_total([1, 2, 3, 4, 5]))
    print(get_total([1, 1, 3, 4, 5, 9]))
    print(get_total([1, 4, 5, 7, 8]))
