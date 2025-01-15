def get_sum_of_first_n_odd_nums(n):
    # return sum(i for i in range(1, n + n + 1) if i % 2)

    # OR sum of first N = N * N
    return n * n


if __name__ == "__main__":
    print(get_sum_of_first_n_odd_nums(5))