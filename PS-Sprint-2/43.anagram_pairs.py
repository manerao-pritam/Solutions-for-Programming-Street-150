from collections import Counter, defaultdict

"""
For any chars
"""
def get_anagram_pair(strings):
    anagrams = defaultdict(list)

    for string in strings:
        key = frozenset(Counter(string).items())  # Unique char count representation
        anagrams[key].append(string)

    return [group for group in anagrams.values() if len(group) > 1]

"""
For just English letters
"""
def get_anagram_pair_(strings):
    anagrams = defaultdict(list)

    for string in strings:
        hash_table = [0] * 26       # 26 English chars
        for ch in string:
            # lower for case-insensitive
            hash_table[ord(ch.lower()) - ord('a')] += 1

        key = tuple(hash_table)
        anagrams[key].append(string)

    return [val for val in anagrams.values() if len(val) > 1]


if __name__ == '__main__':
    print(get_anagram_pair(["listen", "silent", "silEnt", "Slient", "hello", "world"]))
    print(get_anagram_pair(["wood", "woof", "blew", "lebw", "tmp", "dwoo"]))