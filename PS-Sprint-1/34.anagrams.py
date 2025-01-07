from collections import defaultdict


def are_anagrams(s1, s2):
    if not s1 and not s2:
        return True

    if not s1 or not s2 or len(s1) != len(s2):
        return False

    char_to_freq = defaultdict(int)

    for c1, c2 in zip(s1, s2):
        if c1.isdigit():
            char_to_freq[c1] += 1
        elif c2.isdigit():
            char_to_freq[c2] -= 1
        elif c1.isalpha():
            char_to_freq[c1.lower()] += 1
        elif c2.isalpha():
            char_to_freq[c2.lower()] -= 1

    # Check if any frequency is non-zero
    return any(value != 0 for value in char_to_freq.values())


    # for value in char_to_freq.values():
    #     if not value:
    #         return False
    #
    # return True


if __name__ == "__main__":
    print(are_anagrams("silent", "listen"))         # True
    print(are_anagrams("sil e n t   ", "listen"))   # False
    print(are_anagrams("triangle", "integral"))     # True
    print(are_anagrams("hello123", "321hello"))     # True
    print(are_anagrams("abc123", "abc321"))         # True
    print(are_anagrams("abc", "abcd"))              # False
    print(are_anagrams("abc", "abcc"))              # False

