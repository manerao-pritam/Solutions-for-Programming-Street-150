from collections import defaultdict

def get_word_count(s, word):
    word_freq = defaultdict(int)

    for w in s.strip().split():
        word_freq[w] += 1

    return word_freq[word]


if __name__ == "__main__":
    print(get_word_count("hello world hello", "hello"))
    print(get_word_count("hello world hello", "tmp"))
