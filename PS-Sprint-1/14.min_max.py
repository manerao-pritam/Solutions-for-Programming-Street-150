def get_min_max(nums):
    if not nums:
        return 0, 0

    if len(nums) < 2:
        return nums[0], nums[0]

    smallest, largest = nums[0], nums[0]
    for n in nums:
        smallest = min(smallest, n)
        largest = max(largest, n)

    return smallest, largest


if __name__ == "__main__":
    print(get_min_max([4, 7, 1, 8, 5]))