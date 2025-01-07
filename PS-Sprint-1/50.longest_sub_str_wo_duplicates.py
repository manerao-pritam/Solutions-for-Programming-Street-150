from collections import defaultdict


def get_longest_sub_str(s):
    last_seen = defaultdict(int)
    start, max_len, window_start = 0, 0, 0

    for window_end, ch in enumerate(s):
        if ch in last_seen:
            window_start = max(window_start, last_seen[ch] + 1)

        last_seen[ch] = window_end

        curr_len = window_end - window_start + 1

        if curr_len > max_len:
            max_len = curr_len
            start = window_start

    return s[start: start + max_len]

if __name__ == "__main__":
    print(get_longest_sub_str("abcabcbb"))