import heapq


def get_order(tasks):
    indexed_tasks = list(enumerate(tasks))
    indexed_tasks.sort(key=lambda x: x[1][0])

    curr_time = 0
    i = 0
    heap = []
    res = []

    while len(res) < len(tasks):
        while i < len(tasks) and indexed_tasks[i][1][0] <= curr_time:
            heapq.heappush(heap, (indexed_tasks[i][1][1], indexed_tasks[i][0]))
            i += 1

        if heap:
            pt, idx = heapq.heappop(heap)
            curr_time += pt
            res.append(idx)
        else:
            curr_time = indexed_tasks[i][1][0]
    return res
