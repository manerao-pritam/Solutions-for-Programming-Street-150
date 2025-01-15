from math import isqrt


def get_perfect_nums(limit):
    def is_perfect(num):
        divisor_sum = 1                 # 1 is always a divisor

        for i in range(2, isqrt(num) + 1):
            if num % i == 0:
                divisor_sum += i        # divisor found

                if i != num // i:       # Avoid adding the square root twice if perfect square
                    divisor_sum += (num // i)

            # early exit
            if divisor_sum > num:
                return False

        return divisor_sum == num

    result = []
    for n in range(2, limit + 1):
        if is_perfect(n):
            result += [n]

    return result


if __name__ == "__main__":
    print(get_perfect_nums(25))
    print(get_perfect_nums(28))
    print(get_perfect_nums(1000))