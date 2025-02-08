from collections import defaultdict, Counter


"""
using counter
"""
def get_char_freq(string):
    return Counter(string).items()


def get_char_freq(string):
    char_freq = defaultdict(int)
    for ch in string:
        char_freq[ch] += 1

    return char_freq.items()


if __name__ == '__main__':
    print(get_char_freq("hello"))
    print(get_char_freq(""))
    print(get_char_freq("ll"))