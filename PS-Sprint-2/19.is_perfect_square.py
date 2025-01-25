from math import ceil, floor, sqrt

"""
Mathematical Approach
"""
def get_perfect_squares_in_range(start, end):
    lower = ceil(sqrt(start))   # smallest integer whose square is >= start
    upper = floor(sqrt(end))    # largest integer whose square is <= end

    # Generate the perfect squares in the range
    return [num * num for num in range(lower, upper + 1)]



if __name__ == "__main__":
    print(get_perfect_squares_in_range(0, 10))
    print(get_perfect_squares_in_range(5, 20))
    print(get_perfect_squares_in_range(20, 100))