class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return head;
        }

        ListNode curr = head;
        ListNode prev = null;
        ListNode next = null;

        while (curr != null) {
            next = curr.next;
            curr.next = prev;

            // prev and curr are moving in opposite directions
            prev = curr;
            curr = next;
        }

        head = prev;
        return head;
    }
}