def get_second_largest(nums):
    if not nums or len(nums) < 2:
        return None

    first = second = float('-inf')
    for num in nums:
        if num > first:
            second, first = first, num
        elif second < num < first:
            second = num

    return second if second != float('-inf') else None



if __name__ == "__main__":
    print(get_second_largest([10, 20, 4, 45, 99]))
    print(get_second_largest([]))                       # Empty list
    print(get_second_largest([10]))                     # Single element
    print(get_second_largest([5, 5]))                   # Two identical elements
    print(get_second_largest([10, 20]))                 # Two distinct elements
    print(get_second_largest([7, 7, 7, 7]))             # All elements the same
    print(get_second_largest([-10, -5, 0, 10, 20]))     # Negative and positive numbers
    print(get_second_largest([20, 20, 15, 10, 20]))     # Duplicate max values
    print(get_second_largest([-1, -2, -3, -4, -5]))     # All negative numbers
    print(get_second_largest([10, 20, -5]))             # Second largest is negative
    print(get_second_largest([3, 3, 3, 3, 3]))          # Only one number repeated