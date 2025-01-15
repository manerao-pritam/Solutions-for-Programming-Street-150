"""
Manacher's Algorithm (Modified for Palindromic Substrings):
T.C: O(n)
S.C: O(n)

Steps:
    1. Preprocess the string to handle both odd- and even-length palindromes. For example, transform "aba" into "#a#b#a#".
    2. Use a center-expansion approach with a helper array (P) to store the radius of the palindrome at each center.
    3. Use the symmetry property of palindromes to avoid redundant calculations.
    4. Sum up the lengths of all palindromes using the values in P.
"""
def get_palindromic_substring_count(s):
    # Preprocess the string to handle even and odd length palindromes
    t = "#" + "#".join(s) + "#"
    n = len(t)
    P = [0] * n
    center = right = 0

    for i in range(n):
        # Mirror of current position i with respect to center
        mirror = 2 * center - i
        if i < right:
            P[i] = min(right - i, P[mirror])

        # Expand around center
        a, b = i + P[i] + 1, i - P[i] - 1
        while a < n and b >= 0 and t[a] == t[b]:
            P[i] += 1
            a += 1
            b -= 1

        # Update center and right boundary if we've expanded beyond the current boundary
        if i + P[i] > right:
            center, right = i, i + P[i]

    # Sum up the contributions of each palindrome (ignoring the '#' characters)
    return sum((length + 1) // 2 for length in P)



"""
T.C: O(n * n)
this can also be used to get a list of all the palindromes, just collect each palindrome in the while loop
"""
def get_palindromic_substring_count1(s):
    def get_palindrome_count(l, r):
        nonlocal count
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1

        return count

    count = 0
    for i in range(len(s)):
        get_palindrome_count(i, i)         # odd length palindromes
        get_palindrome_count(i, i + 1)     # even length palindromes

    return count


"""
Brute force
T.C.: O(n * n * n)
"""
def get_palindromic_substring_count2(s):
    def is_palindrome(l, r):
        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True

    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            count += is_palindrome(i, j)

    return count

if __name__ == "__main__":
    print(get_palindromic_substring_count("aaa"))       # output: 6 => a, a, a, aa, aa, aaa
    print(get_palindromic_substring_count("madam"))     # output: 7 => m, a, d, a, m, ada, madam
    print(get_palindromic_substring_count(""))          # output: 0
    print(get_palindromic_substring_count("m"))         # output: 1 => m
    print(get_palindromic_substring_count("ad"))        # output: 2 => a, d