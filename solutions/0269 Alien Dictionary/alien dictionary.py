from collections import defaultdict, deque


def alien_order(words):
    adj_list = defaultdict(set)
    n = len(words)
    in_degrees = {}

    for word in words:
        for c in word:
            in_degrees[c] = 0

    for i in range(n - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))

        if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
            return ""

        for j in range(min_len):
            c1, c2 = w1[j], w2[j]

            if c1 != c2:
                if c2 not in adj_list[c1]:
                    adj_list[c1].add(c2)
                    in_degrees[c2] += 1
                break

    q = []
    for c in in_degrees:
        if in_degrees[c] == 0:
            q.append(c)

    queue = deque(q)
    order = []

    while queue:
        curr = queue.popleft()
        order.append(curr)

        for neighbour in adj_list[curr]:
            in_degrees[neighbour] -= 1
            if in_degrees[neighbour] == 0:
                queue.append(neighbour)

    if len(order) == len(in_degrees):
        return "".join(order)
    return ""
