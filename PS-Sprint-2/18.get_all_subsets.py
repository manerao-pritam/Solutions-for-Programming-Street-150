"""Pick/Skip approach"""

"""
BFS
"""
from collections import deque

def subsets(nums):
    deq = deque([[]])

    for num in nums:
        level_size = len(deq)

        for _ in range(level_size):
            subset = deq.popleft()

            # create two subsets: picking and skipping num
            deq.append(subset)          # skip num
            deq.append(subset + [num])  # pick num

    return list(deq)


"""
Backtracking
"""
def subsets(nums):
    def helper(idx, subset):
        if idx == len(nums):
            result.append(list(subset))
            return

        # skip
        helper(idx + 1, subset)

        # pick
        subset.append(nums[idx])
        helper(idx + 1, subset)

        # backtrack
        subset.pop()

    result = []
    helper(0, [])
    return result



if __name__ == "__main__":
    print(subsets([1, 2, 3]))
    print(subsets([1]))