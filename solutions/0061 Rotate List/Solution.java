class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null) {
            return head;
        }

        ListNode curr = head;
        int n = getLengthOfList(head);
        k = k % n;

        for (int i = 0; i < k; i += 1) {
            curr = rotateOnce(curr);
        }
        return curr;
    }

    public ListNode rotateOnce(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode tail = head;

        while (tail.next != null) {
            tail = tail.next;
        }

        ListNode secondLastNode = head;

        while (secondLastNode.next.next != null) {
            secondLastNode = secondLastNode.next;
        }

        secondLastNode.next = null;
        tail.next = head;
        return tail;
    }

    public int getLengthOfList(ListNode head) {
        if (head == null) {
            return 0;
        }
        return 1 + getLengthOfList(head.next);
    }
}