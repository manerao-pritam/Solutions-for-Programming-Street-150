def get_triplets(nums):
    nums.sort()
    triplets = []

    for first, num in enumerate(nums[:-2]):  # Stop at the third-last element
        if first > 0 and num == nums[first - 1]:  # Skip duplicates
            continue

        second, third = first + 1, len(nums) - 1
        while second < third:
            triplet_sum = num + nums[second] + nums[third]

            if triplet_sum == 0:
                triplets.append([num, nums[second], nums[third]])
                second += 1
                third -= 1

                # Skip duplicate numbers for the second pointer
                while second < third and nums[second] == nums[second - 1]:
                    second += 1

                # Skip duplicate numbers for the third pointer
                while second < third and nums[third] == nums[third + 1]:
                    third -= 1

            elif triplet_sum > 0:
                third -= 1
            else:
                second += 1

    return triplets

if __name__ == '__main__':
    print(get_triplets([-1, 0, 1, 2, -1, -4]))  # Expected: [[-1, -1, 2], [-1, 0, 1]]
    print(get_triplets([0, 1, 1]))              # Expected: []
    print(get_triplets([0, 0, 0]))              # Expected: [[0, 0, 0]]
