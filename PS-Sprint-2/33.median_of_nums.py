def get_median(nums):
    sorted_nums = sorted(nums)      # not modifying the input
    mid = len(sorted_nums) // 2

    if len(sorted_nums) & 1:
        return sorted_nums[mid]

    return sum(sorted_nums[mid: mid + 2]) / 2


if __name__ == "__main__":
    print(get_median([3, 1, 4, 1, 1, 5]))