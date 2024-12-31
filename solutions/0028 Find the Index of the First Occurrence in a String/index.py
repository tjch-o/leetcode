def first_occurrence(s, substr):
    n, l = len(s), len(substr)

    for i in range(n - l + 1):
        if s[i : i + l] == substr:
            return i
    return -1
