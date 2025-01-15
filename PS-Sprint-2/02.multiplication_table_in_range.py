def multiplication_table_in_range(start, end):
    for num in range(start, end + 1):
        for i in range(1, 11):
            print(f'{num} * {i} = {num * i}')
        print()


if __name__ == "__main__":
    multiplication_table_in_range(2, 4)