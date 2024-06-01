class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) {
            return true;
        }

        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode reversedSecondHalf = reverseList(slow);
        
        while (head != null && reversedSecondHalf != null) {
            if (head.val != reversedSecondHalf.val) {
                return false;
            }

            head = head.next;
            reversedSecondHalf = reversedSecondHalf.next;
        }
        return true;
    }

    public ListNode reverseList(ListNode head) {
        if (head == null | head.next == null) {
            return head;
        }

        ListNode prev = null;
        ListNode curr = head;
        ListNode next = null;

        while (curr != null) {
            next = curr.next;
            curr.next = prev;

            prev = curr;
            curr = next;
        }
        return prev;
    }
}
