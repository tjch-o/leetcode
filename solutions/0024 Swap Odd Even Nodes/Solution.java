class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head == null) {
            return head;
        } else if (head.next == null) {
            return head;
        }

        ListNode rest = swapPairs(head.next.next);
        ListNode newHead = head.next;
        head.next = rest;
        newHead.next = head;
        return newHead;
    }
}