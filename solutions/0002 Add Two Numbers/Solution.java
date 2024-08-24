class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // converting to numbers before summation then back to linked list will not work for large numbers
        int sum = 0;
        int carry = 0;
        ListNode head = null;
        ListNode curr = null;

        while (l1 != null || l2 != null) {
            if (l1 == null) {
                l1 = new ListNode(0);
            }

            if (l2 == null) {
                l2 = new ListNode(0);
            }

            sum = carry + l1.val + l2.val;
            int digit = sum % 10;
            carry = sum / 10;
            ListNode newNode = new ListNode(digit);

            if (head == null) {
                head = newNode;
                curr = newNode;
            } else {
                curr.next = newNode;
                curr = curr.next;
            }

            l1 = l1.next;
            l2 = l2.next;
        }

        if (carry > 0) {
            curr.next = new ListNode(carry);
        }
        return head;
    }
}