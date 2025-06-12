class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_middle(head):
    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    if prev:
        prev.next = None
    return slow


def merge(l1, l2):
    # avoid the need to create the head specifically
    dummy = ListNode()
    curr = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    if not l1:
        curr.next = l2
    if not l2:
        curr.next = l1
    return dummy.next


def sort_list(head):
    if not head or not head.next:
        return head

    mid = get_middle(head)
    l1 = sort_list(head)
    l2 = sort_list(mid)
    result = merge(l1, l2)
    return result
