def pairs_equal_to_sum(nums, target):
    # Sort the input array first (if needed)
    nums.sort()  # If nums is already sorted, this can be omitted
    pairs = []
    l, r = 0, len(nums) - 1

    while l < r:
        curr = nums[l] + nums[r]

        if curr == target:
            pairs.append((nums[l], nums[r]))
            l += 1
            r -= 1  # Move both pointers to avoid considering the same pair
        elif curr < target:
            l += 1
        else:
            r -= 1

    return pairs


if __name__ == "__main__":
    print(pairs_equal_to_sum([1, 2, 3, 4, 5], 5))  # Expected output: [(1, 4), (2, 3)]
