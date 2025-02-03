"""
Kadane's algo
"""
def get_largest_sum(nums):
    curr_sum, max_sum = 0, float('-inf')

    for num in nums:
        curr_sum = max(curr_sum + num, num)
        max_sum = max(max_sum, curr_sum)

    return max_sum


if __name__ == "__main__":
    print(get_largest_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))     # 6
    print(get_largest_sum([5, 4, -1, 7, 8]))                    # 23
    print(get_largest_sum([1]))                                 # 1