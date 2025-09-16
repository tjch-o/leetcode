class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyHashSet:
    def __init__(self):
        self.set = [ListNode(0) for _ in range(10**4)]

    def add(self, key: int) -> None:
        idx = key % len(self.set)
        curr = self.set[idx]

        while curr.next:
            if curr.next.val == key:
                return
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        idx = key % len(self.set)
        curr = self.set[idx]

        while curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        idx = key % len(self.set)
        curr = self.set[idx]

        while curr.next:
            if curr.next.val == key:
                return True
            curr = curr.next
        return False
