def get_median(nums):
    tmp = sorted(nums)
    start, end = 0, len(tmp) - 1
    mid = start + (end - start) // 2

    if len(tmp) & 1:
        return tmp[mid]  # Return the middle element for odd length

    # Return the average of the two middle elements for even length
    return (tmp[mid] + tmp[mid + 1]) / 2  # Use float division

if __name__ == "__main__":
    print(get_median([3, 1, 2, 4, 5]))  # Output: 3
    print(get_median([3, 1, 2, 4, 7, 5]))  # Output: 3.5
