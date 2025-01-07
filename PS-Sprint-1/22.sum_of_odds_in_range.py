"""
Sum of arithmetic sequence
T.C. O(1)
"""
def get_sum_of_odds_in_range(start, end):
    # if start is even, add 1 to it and make it odd
    start += (start % 2 == 0)

    # if end is even, remove 1 to it and make it odd
    end -= (end % 2 == 0)

    # even terms in the range
    n = (end - start) // 2 + 1

    # Sum of arithmetic sequence: n/2 * (first_term + last_term)
    return n * (start + end) // 2


"""
Using simple loop
T.C. O(end-start)
"""
def get_sum_of_odds_in_range1(start, end):
    total = 0

    # if start is odd, add 1 to even and make it even
    start += (start % 2 == 0)

    # if end is odd, remove 1 to even and make it even
    end -= (end % 2 == 0)

    while start <= end:
        if start % 2:
            total += start
        start += 2

    return total




if __name__ == "__main__":
    print(get_sum_of_odds_in_range(1, 10))