class Solution {
    public void reorderList(ListNode head) {
        if (head.next == null) {
            return;
        }

        ListNode rest = reverseList(head.next);
        head.next = rest;
    }

    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return null;
        } else if (head.next == null) {
            return head;
        } else {
            ListNode reversed = reverseList(head.next);
            head.next.next = head;
            head.next = null;
            return reversed;
        }
    }
}