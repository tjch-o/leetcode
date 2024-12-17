def partition_labels(s):
    n = len(s)
    last_index = {}

    for i in range(n):
        last_index[s[i]] = i

    res = []
    curr = 0
    end = 0

    for i in range(n):
        c = s[i]
        end = max(end, last_index[c])
        curr += 1

        if i == end:
            res.append(curr)
            curr = 0
            end = 0
    return res
