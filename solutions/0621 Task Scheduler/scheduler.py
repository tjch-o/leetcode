from collections import Counter
import heapq


def least_interval(tasks, n):
    counts = Counter(tasks)
    heap = []
    heapq.heapify(heap)

    for task, count in counts.items():
        heapq.heappush(heap, -count)

    cooldown = []
    time = 0

    while heap or cooldown:
        time += 1

        if heap:
            freq = -heapq.heappop(heap) - 1
            if freq > 0:
                cooldown.append((freq, time + n))

        if cooldown and cooldown[0][1] == time:
            next_task = cooldown.pop(0)
            heapq.heappush(heap, -next_task[0])
    return time
