from pprint import pprint as print


"""
Without precomputing the seq
"""
def print_matrix_of_fib_1(num):
    grid = [[0 for _ in range(num)] for _ in range(num)]

    for r in range(num):
        for c in range(num):
            if (r, c) in ((0, 0), (0, 1)):
                grid[r][c] = 1
            elif c == 0:
                grid[r][c] = grid[r - 1][num - 1] + grid[r - 1][num - 2]
            elif c == 1:
                grid[r][c] = grid[r][c - 1] + grid[r - 1][num - 1]
            else:
                grid[r][c] = grid[r][c - 1] + grid[r][c - 2]

    return grid


"""
precomputing the seq
"""
def print_matrix_of_fib(num):
    fibs = [0] * (num * num)
    fibs[:2] = [1, 1]

    for i in range(2, len(fibs)):
        fibs[i] = fibs[i - 1] + fibs[i - 2]

    write_idx = 0

    grid = [[0 for _ in range(num)] for _ in range(num)]
    for r in range(num):
        for c in range(num):
            grid[r][c] = fibs[write_idx]
            write_idx += 1

    return grid



if __name__ == "__main__":
    print(print_matrix_of_fib(3))
    print(print_matrix_of_fib(2))
    print(print_matrix_of_fib(1))
    print(print_matrix_of_fib(5))