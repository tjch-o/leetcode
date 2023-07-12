class Solution {
    public ListNode removeElements(ListNode head, int val) {
        if (head == null) {
            return null;
        } else if (head.val == val) {
            return removeElements(head.next, val);
        } else {
            ListNode remainingElements = removeElements(head.next, val);
            head.next = remainingElements;
            return head;
        }
    }
}