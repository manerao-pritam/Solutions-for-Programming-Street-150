"""
O(1)
"""
def find_a_missing_number_in_arr(nums):
    # The range should be from 1 to len(nums) + 1
    n = len(nums) + 1  # The actual range size
    expected_sum = n * (n + 1) // 2  # Sum of numbers from 1 to n
    actual_sum = sum(nums)

    return [expected_sum - actual_sum]


if __name__ == "__main__":
    print(find_a_missing_number_in_arr([1, 2, 4, 5]))