"""
One Liner using Map
"""
def get_longest_word_len(string):
    return max(map(len, string.split()), default=0)


"""
Loop
"""
def get_longest_word_len(string):
    strings = string.split()
    longest = 0

    for word in strings:
        longest = max(longest, len(word))

    return longest


if __name__ == '__main__':
    print(get_longest_word_len("Find the longest word"))
    print(get_longest_word_len(""))
    print(get_longest_word_len("ddddd dddsdsds aaaaaaaaaaaa    "))