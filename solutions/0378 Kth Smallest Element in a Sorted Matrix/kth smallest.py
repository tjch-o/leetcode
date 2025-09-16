import heapq


def kth_smallest(matrix, k):
    n = len(matrix)
    heap = []
    heapq.heapify(heap)

    for i in range(n):
        heapq.heappush(heap, (matrix[i][0], i, 0))

    for _ in range(k):
        curr, row, col = heapq.heappop(heap)

        if col < n - 1:
            heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
    return curr
