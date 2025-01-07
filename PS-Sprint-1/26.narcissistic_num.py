# Explanation: 153 is a narcissistic number because 1^3 + 5^3 + 3^3 = 153.

def is_narcissistic(num):
    result, org = 0, num,
    digit_count = len(str(num))

    while num:
        digit = num % 10
        result += pow(digit, digit_count)
        num //= 10

    return result == org



if __name__ == "__main__":
    print(is_narcissistic(153))
    print(is_narcissistic(135))