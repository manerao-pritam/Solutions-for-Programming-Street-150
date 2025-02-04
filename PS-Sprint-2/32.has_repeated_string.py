def has_repeated_substr(s):
    if not s or len(s) == 1:
        return False

    # 1. Double the String: s + s
    # 2. Drop the first and last chars: [1: -1]
    # 3. Check if s exist in the resultant string
    return s in (s + s)[1: -1]


if __name__ == "__main__":
    print(has_repeated_substr("abab"))
    print(has_repeated_substr("babcbabc"))
    print(has_repeated_substr(""))
    print(has_repeated_substr("a"))
    print(has_repeated_substr("abcdeg"))