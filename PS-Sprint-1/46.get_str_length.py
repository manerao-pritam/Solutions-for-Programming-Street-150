def get_str_length(s):
    # return len(s)
    # return sum(1 for _ in s)

    count = 0
    for _ in s:
        count += 1

    return count


if __name__ == "__main__":
    print(get_str_length("hello"))