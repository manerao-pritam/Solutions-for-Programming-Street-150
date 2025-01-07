def is_palindrome(s):
    l, r = 0, len(s) - 1

    while l < r:
        # Skip non-alphanumeric characters
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        # Compare characters (case-insensitive)
        elif s[l].lower() != s[r].lower():
            return False
        else:
            # Move pointers inward if characters match
            l += 1
            r -= 1

    return True


if __name__ == "__main__":
    print(is_palindrome("ra  D A     R"))