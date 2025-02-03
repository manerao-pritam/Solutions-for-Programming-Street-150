def get_longest_seq(nums):
    longest = curr_len = 0

    for num in nums:
        curr_len += num     # add 1 or 0

        if not num:
            longest = max(longest, curr_len)
            curr_len = 0

    return max(longest, curr_len)


if __name__ == "__main__":
    print(get_longest_seq([1, 1, 0, 1, 1, 1]))
    print(get_longest_seq([0, 0, 0, 0, 0]))
    print(get_longest_seq([1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]))