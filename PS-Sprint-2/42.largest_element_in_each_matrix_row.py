def get_row_max(matrix):
    return [max(row) for row in matrix]


if __name__ == '__main__':
    print(get_row_max([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(get_row_max([[1], [1]]))
    print(get_row_max([[1, 3, 4, 2, 6], [2, 3, 3, 3, 3]]))