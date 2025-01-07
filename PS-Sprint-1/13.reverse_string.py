def reverse_string(s):
    # return s[::-1]

    result = list(s)
    l, r = 0, len(s) - 1
    while l < r:
        result[l], result[r] = result[r], result[l]
        l += 1
        r -= 1

    return "".join(result)


if __name__ == "__main__":
    print(reverse_string("programming"))