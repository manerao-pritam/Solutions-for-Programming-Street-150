def get_armstrong_in_range(start, end):
    """
    Another approach -- precompute the powers of 1 to 9
    """
    def is_armstrong(num):
        digits = len(str(num))

        """
        precompute the powers of each number (1 to 9) to the power of (0-9)
        {1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]...}
        """
        powers = {d: [pow(i, d) for i in range(10)] for d in range(1, digits + 1)}
        return num == sum(powers[digits][int(digit)] for digit in str(num))

    def is_armstrong1(num):
        result, org = 0, num
        while num:
            digit = num % 10
            result += pow(digit, 3)
            num //= 10

        return result == org

    """
    - 1 is an armstrong num
    - there's no other single digit armstrong num therefore the above would fail so num >= 10 condition 
    """
    return [num for num in range(start, end + 1) if num == 1 or (num >= 10 and is_armstrong(num))]


if __name__ == "__main__":
    print(get_armstrong_in_range(1, 500))