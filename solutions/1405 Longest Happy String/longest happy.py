import heapq


def is_same_three_consecutive(arr, c):
    return len(arr) >= 2 and arr[-1] == arr[-2] and arr[-1] == c


def longest_diverse_string(a, b, c):
    max_heap = [(-a, "a"), (-b, "b"), (-c, "c")]
    heap = [(count, c) for count, c in max_heap if count != 0]
    heapq.heapify(heap)

    res = []

    while heap:
        count, c = heapq.heappop(heap)

        if not is_same_three_consecutive(res, c):
            res.append(c)
            count += 1

            if count != 0:
                heapq.heappush(heap, (count, c))
        else:
            if not heap:
                break

            next_count, next_c = heapq.heappop(heap)
            res.append(next_c)
            next_count += 1

            if next_count != 0:
                heapq.heappush(heap, (next_count, next_c))

            heapq.heappush(heap, (count, c))
    return "".join(res)
