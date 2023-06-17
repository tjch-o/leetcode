class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return null;
        } else if (head.next == null) {
            return head;
        } else {
            ListNode reverse = reverseList(head.next);
            head.next.next = head;
            head.next = null;
            return reverse;
        }
    }
}