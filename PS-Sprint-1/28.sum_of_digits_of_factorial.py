from math import factorial

"""
Using in-built factorial method
"""
def get_sum_of_digits_of_factorial1(n):
    def get_digit_sum(num):
        return sum(int(digit) for digit in str(num))

    return get_digit_sum(factorial(n))

def get_sum_of_digits_of_factorial(n):
    def get_digit_sum(num):
        return sum(int(digit) for digit in str(num))

    def get_factorial(n):
        fact = 1
        for num in range(1, n + 1):
            fact *= num
        return fact

    return get_digit_sum(get_factorial(n))


if __name__ == "__main__":
    print(get_sum_of_digits_of_factorial(4))