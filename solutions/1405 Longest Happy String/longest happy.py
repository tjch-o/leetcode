import heapq


def consecutive_letters(arr, c):
    return len(arr) >= 2 and arr[-1] == c and arr[-2] == c


def longest_diverse_string(a, b, c):
    res = []
    counts = [(-a, "a"), (-b, "b"), (-c, "c")]
    heap = list(filter(lambda x: x[0] != 0, counts))
    heapq.heapify(heap)

    while heap:
        count, curr_c = heapq.heappop(heap)

        if not consecutive_letters(res, curr_c):
            res.append(curr_c)
            if count + 1 < 0:
                heapq.heappush(heap, (count + 1, curr_c))
        else:
            if heap:
                next_count, next_c = heapq.heappop(heap)

                if next_count < 0:
                    res.append(next_c)
                    if next_count + 1 < 0:
                        heapq.heappush(heap, (next_count + 1, next_c))

                heapq.heappush(heap, (count, curr_c))
    return "".join(res)
