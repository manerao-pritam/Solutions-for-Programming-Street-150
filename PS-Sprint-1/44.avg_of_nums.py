def get_avg(nums):
    # return sum(nums) // len(nums)

    total, count = 0, 0
    for num in nums:
        count += 1
        total += num

    return total // count


if __name__ == "__main__":
    print(get_avg([1, 2, 3, 4, 5]))