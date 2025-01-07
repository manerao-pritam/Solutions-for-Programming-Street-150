"""
T.C. O(n * log n)
S.C. O(1)       -- in-place
"""
# def sort_arr_in_place(nums):
def sort_arr(nums):
    def merge(left, mid, right):
        l, r = left, mid + 1

        while l <= mid and r <= right:
            if nums[l] <= nums[r]:
                l += 1
            else:
                # # Place nums[r] in its correct position by rotating the subarray
                # temp = nums[r]
                # for k in range(r, l, -1):  # Shift elements one-by-one
                #     nums[k] = nums[k - 1]
                # nums[l] = temp

                ## OR

                # Rotate nums[right] to the left of nums[left]
                tmp = nums[r]
                nums[l + 1: r + 1] = nums[l: r]
                nums[l] = tmp

                # Update pointers
                l += 1
                mid += 1
                r += 1


    def merge_sort(l, r):
        if l >= r:
            return

        mid = l + (r - l) // 2

        merge_sort(l, mid)
        merge_sort(mid + 1, r)
        merge(l, mid, r)


    if len(nums) <= 1:
        return

    merge_sort(0, len(nums) - 1)
    return nums



"""
T.C. O(n * log n)
S.C. O(n)       -- creating a new list
"""
def sort_arr1(nums):
    def merge(left, right):
        l, r = 0, 0
        result = []

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                result += [left[l]]
                l += 1
            else:
                result += [right[r]]
                r += 1

        result += left[l:]
        result += right[r:]

        return result


    def merge_sort(sub_list):
        if len(sub_list) <= 1:
            return sub_list

        mid = len(sub_list) // 2

        left = merge_sort(sub_list[:mid])
        right = merge_sort(sub_list[mid:])

        return merge(left, right)

    if len(nums) < 2:
        return nums

    return merge_sort(nums)



if __name__ == "__main__":
    nums = [3, 1, 4, 1, 5, 9]
    print(sort_arr(nums))
    nums = [4, 7, 1, 8, 5]
    print(sort_arr(nums))