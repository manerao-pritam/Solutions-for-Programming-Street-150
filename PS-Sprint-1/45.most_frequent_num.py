from collections import Counter


def get_most_frequent_num(nums):
    # Use Counter to count frequencies of elements
    freq = Counter(nums)

    # Find the element with the highest frequency
    return max(freq, key=freq.get)


"""
This only works if most freq num appears more than half of the times in the list
"""
""""
def get_most_frequent_num(nums):
    if not nums:
        return None

    if len(nums) == 1:
        return nums[0]

    candidate, freq = nums[0], 1

    for num in nums[1:]:
        if candidate == num:
            freq += 1
        else:
            freq -= 1

            if not freq:
                candidate = num
                freq = 1

    return candidate
"""


if __name__ == "__main__":
    print(get_most_frequent_num([1, 2, 2, 3, 3, 4, 4, 4]))