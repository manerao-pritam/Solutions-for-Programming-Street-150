def get_multiplication_table(num):
    for i in range(1, 11):
        print(f'{num} * {i} = {num * i}')


if __name__ == "__main__":
    get_multiplication_table(4)