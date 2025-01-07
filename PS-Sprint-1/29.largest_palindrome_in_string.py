def get_largest_palindrome_in_string(s):
    max_len, start = 1, 0

    for i in range(len(s)):
        # odd
        l, r = i, i
        while l >= 0 and r < len(s) and s[l].lower() == s[r].lower():
            curr_len = r - l + 1
            if curr_len > max_len:
                max_len = curr_len
                start = l
            l -= 1
            r += 1

        # even
        l, r = i, i +1
        while l >= 0 and r < len(s) and s[l].lower() == s[r].lower():
            curr_len = r - l + 1
            if curr_len > max_len:
                max_len = curr_len
                start = l
            l -= 1
            r += 1

    return s[start: start + max_len]


if __name__ == "__main__":
    print(get_largest_palindrome_in_string("babad"))