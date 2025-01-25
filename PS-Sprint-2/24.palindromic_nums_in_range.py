def get_palindromic_nums_in_range(start, end):
    def is_palindrome(num):
        num = str(num)

        for i in range((len(num) // 2) + 1):
            if num[i] != num[~i]:
                return False

        return True

    """
    space: O(len(num) space for creating a reversed copy
    """
    # def is_palindrome(num):
    #     num = str(num)
    #     return num == num[::-1]

    return [num for num in range(start, end + 1) if is_palindrome(num)]



if __name__ == "__main__":
    print(get_palindromic_nums_in_range(1, 100))