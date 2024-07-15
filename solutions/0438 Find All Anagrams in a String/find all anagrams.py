def get_char_freq(s):
    char_freq = {}

    for c in s:
        char_freq[c] = char_freq.get(c, 0) + 1
    return char_freq


def find_anagrams(s, p):
    result = []
    target = get_char_freq(p)
    m, n = len(s), len(p)
    window_freq = {}

    for i in range(m):
        c = s[i]
        window_freq[c] = window_freq.get(c, 0) + 1

        if i >= n:
            prev_start = s[i - n]

            if prev_start in window_freq:
                window_freq[prev_start] -= 1

                if window_freq[prev_start] == 0:
                    del window_freq[prev_start]

        if window_freq == target:
            new_window_start = i - n + 1
            result.append(new_window_start)

    return result
