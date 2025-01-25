"""
The simplest idea is to use Fib sequence; pair for curr num is from zip(r2, r2[1:])
"""

def print_pascals_triangle(n):
    r1, r2 = [1], [1, 1]

    while n:
        print(*r1)      # * here is the same as printing each item in a list

        r1, r2 = r2, [1] + [sum(pair) for pair in zip(r2, r2[1:])] + [1]
        n -= 1



if __name__ == "__main__":
    print_pascals_triangle(5)
    print_pascals_triangle(4)