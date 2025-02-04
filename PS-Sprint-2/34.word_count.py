"""
One-liner
"""
def get_count(s):
    return len(s.split())


"""
more pythonic version
"""
def get_count1(s):
    count, in_word = 0, False

    for ch in s:
        # if we encounter a non-space char, and we're not yet in a word,
        # its start of the word
        if ch != " " and not in_word:
            count += 1
            in_word = True

        # if we hit a space, we're no longer inside a word
        elif ch == " ":
            in_word = False

    return count

"""
simple loop
"""
def get_count2(s):
    i, count = 0, 0
    while i < len(s):
        while i < len(s) and s[i] == " ":
            i += 1

        # reached the string end
        if i == len(s): break

        while i < len(s) and s[i] != " ":
            i += 1

        count += 1

    return count


if __name__ == "__main__":
    print(get_count("Hello world"))                     # 2
    print(get_count(""))                                # 0
    print(get_count("HelloWorld"))                      # 1
    print(get_count("H    ell  o Wo   rld      "))      # 5
