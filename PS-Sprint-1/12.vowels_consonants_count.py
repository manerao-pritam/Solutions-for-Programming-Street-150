def vowels_consonants_count(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vow_counter, consonants_counter = 0, 0

    for ch in s:
        if not ch.isalpha():
            continue

        if ch.lower() in vowels:
            vow_counter += 1
        else:
            consonants_counter += 1

    return vow_counter, consonants_counter


if __name__ == "__main__":
    print(vowels_consonants_count("hEllo wor l  d    "))    # (3, 7)
    print(vowels_consonants_count("Hello, World! 123"))     # (3, 7)
    print(vowels_consonants_count(""))                      # (0, 0)
    print(vowels_consonants_count("AEIOUaeiou"))            # (10, 0)
    print(vowels_consonants_count("12345"))                 # (0, 0)
    print(vowels_consonants_count("Python"))                # (1, 5)
