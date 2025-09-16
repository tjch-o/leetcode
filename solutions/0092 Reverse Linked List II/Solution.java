class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (right == 1) {
            return head;
        }

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;

        for (int i = 1; i < left; i += 1) {
            prev = prev.next;
        }

        ListNode start = prev.next;
        ListNode end = start;

        for (int i = left; i < right; i += 1) {
            end = end.next;
        }

        ListNode headAfterReverse = end.next;
        ListNode reversed = reverseList(start, end);
        start.next = headAfterReverse;
        prev.next = reversed;
        return dummy.next;
    }

    public ListNode reverseList(ListNode start, ListNode end) {
        if (start == end) {
            return start;
        }

        ListNode reversed = reverseList(start.next, end);
        start.next.next = start;
        start.next = null;
        return reversed;
    }
}