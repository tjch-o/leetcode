import heapq


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


def min_meeting_rooms(intervals):
    n = len(intervals)
    intervals.sort(key=lambda x: x.start)
    heap = [(intervals[0].end)]
    heapq.heapify(heap)

    for i in range(1, n):
        if intervals[i].start >= heap[0]:
            heapq.heappop(heap)

        heapq.heappush(heap, intervals[i].end)
    return len(heap)
