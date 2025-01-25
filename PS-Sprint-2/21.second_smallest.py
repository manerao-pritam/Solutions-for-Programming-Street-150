def get_second_smallest(nums):
    if len(nums) < 2:
        return None         # At least two nums are required

    first = second = float('inf')

    for num in nums:
        if num < first:
            second, first = first, num
        elif num < second and num != first:
            second = num

    if second == float('inf'):
        return None         # No second-largest element found

    return second



if __name__ == "__main__":
    print(get_second_smallest([1, 2, 3, 4, 5, 6]))          # 2
    print(get_second_smallest([1, 2, 3, 4, 5, 6][::-1]))    # 2
    print(get_second_smallest([12, 13, 1, 10, 34, 1]))      # 10
    print(get_second_smallest([12, 13, 2, 3, 34, 1]))       # 2
    print(get_second_smallest([1, 1, 1]))                   # None
    print(get_second_smallest([1]))                         # None
    print(get_second_smallest([]))                          # None