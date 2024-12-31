def get_index(c):
    return ord(c) - 97


def check_inclusion(substr, s):
    n1, n2 = len(substr), len(s)

    if n1 > n2:
        return False

    substr_count = [0 for _ in range(26)]
    window_count = [0 for _ in range(26)]

    for c in substr:
        substr_count[get_index(c)] += 1

    for i in range(n2):
        window_count[get_index(s[i])] += 1

        if i >= n1:
            window_count[get_index(s[i - n1])] -= 1

        if window_count == substr_count:
            return True
    return False
