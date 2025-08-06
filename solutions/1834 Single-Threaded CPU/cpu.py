import heapq


def get_order(tasks):
    n = len(tasks)
    indexed_tasks = [(tasks[i], i) for i in range(n)]
    indexed_tasks.sort(key=lambda x: x[0][0])

    heap = []
    heapq.heapify(heap)
    ptr = 0
    curr_time = 0
    res = []

    while len(res) < n:
        while ptr < n and indexed_tasks[ptr][0][0] <= curr_time:
            processing_time, index = indexed_tasks[ptr][0][1], indexed_tasks[ptr][1]
            heapq.heappush(heap, (processing_time, index))
            ptr += 1

        if heap:
            processing_t, idx = heapq.heappop(heap)
            curr_time += processing_t
            res.append(idx)
        else:
            curr_time = indexed_tasks[ptr][0][0]
    return res
