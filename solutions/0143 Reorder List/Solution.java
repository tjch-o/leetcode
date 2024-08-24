class Solution {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) {
            return;
        }

        ListNode mid = getMiddleOfList(head);
        ListNode reversed = reverseList(mid);
        mergeLists(head, reversed);
    }

    public ListNode getMiddleOfList(ListNode head) {
        ListNode slow = head;
        ListNode prev = null;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }

        if (prev != null) {
            prev.next = null;
        }
        return slow;
    }

    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode curr = head;
        ListNode prev = null;

        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;

            prev = curr;
            curr = next;
        }

        return prev;
    }

    public void mergeLists(ListNode l1, ListNode l2) {
        ListNode curr = new ListNode(0);

        while (l1 != null && l2 != null) {
            curr.next = l1;
            l1 = l1.next;
            curr = curr.next;

            curr.next = l2;
            l2 = l2.next;
            curr = curr.next;
        }

        if (l1 != null) {
            curr.next = l1;
        }

        if (l2 != null) {
            curr.next = l2;
        }
    }
}