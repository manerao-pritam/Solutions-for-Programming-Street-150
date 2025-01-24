"""
LC 128: https://leetcode.com/problems/longest-consecutive-sequence/description/
"""
def get_longest_consecutive_seq_len(nums):
    nums_set = set(nums)
    longest = 0

    for num in nums_set:
        if num - 1 not in nums_set: # is this the start of the seq?
            curr = num
            curr_len = 1

            # Count up as long as the next consecutive number exists
            while curr + 1 in nums_set:
                curr_len += 1
                curr += 1

            longest = max(longest, curr_len)

    return longest



if __name__ == "__main__":
    print(get_longest_consecutive_seq_len([100, 4, 200, 1, 3, 2]))
    print(get_longest_consecutive_seq_len([0,3,7,2,5,8,4,6,0,1]))
