class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode rightPtr = head;
        ListNode leftPtr = head;
        int count = n;

        while (count > 0 && rightPtr != null) {
            rightPtr = rightPtr.next;
            count -= 1;
        }

        if (rightPtr == null) {
            if (count == 0) {
                head = head.next;
                return head;
            } else {
                // n is greater than length of list
                return null;
            }
        }

        while (rightPtr.next != null) {
            rightPtr = rightPtr.next;
            leftPtr = leftPtr.next;
        }

        leftPtr.next = leftPtr.next.next;
        return head;
    }
}