"""
idea is simple -> keep on finding the gcd of two nums:
    gcd(a, b, c) = gcd(gcd(a, b), c) and so on
"""

def get_gcd_of_list(nums):
    def get_gcd(m, n):
        while n != 0:
            m, n = n, m % n

        return m

    result = nums[0]
    for num in nums[1:]:
        result = get_gcd(result, num)

    return result


if __name__ == "__main__":
    print(get_gcd_of_list([24, 36, 48]))
    print(get_gcd_of_list([12, 24, 36]))
    print(get_gcd_of_list([24, 36, 50, 48]))