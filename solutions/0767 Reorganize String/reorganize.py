from collections import Counter
from math import ceil
import heapq


def reorganize_string(s):
    counts = Counter(s)

    if max(counts.values()) > ceil(len(s) / 2):
        return ""

    heap = [(-counts[c], c) for c in counts]
    heapq.heapify(heap)

    prev_count, prev_c = 0, ""
    res = []

    while heap:
        count, c = heapq.heappop(heap)
        res.append(c)

        if prev_count < 0:
            heapq.heappush(heap, (prev_count, prev_c))

        prev_count, prev_c = count + 1, c
    return "".join(res)
