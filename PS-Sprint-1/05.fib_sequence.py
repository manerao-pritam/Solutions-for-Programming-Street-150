def fib_sequence_upto_n(num):
    result = [0, 1]

    for i in range(2, num):
        # result += [result[-1] + result[-2]]
        next_num = sum(result[-2:])

        if next_num >= num:
            break

        result += [next_num]

    return result

if __name__ == "__main__":
    print(fib_sequence_upto_n(10))
