import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists):
    nodes = []
    res = None
    curr = None
    index = 0

    for l in lists:
        curr = l

        while curr:
            nodes.append((curr.val, index, curr))
            curr = curr.next
            index += 1

    heapq.heapify(nodes)

    while nodes:
        _, _, node = heapq.heappop(nodes)

        if not curr:
            res = node
            curr = res
        else:
            curr.next = node
            curr = curr.next
    return res
