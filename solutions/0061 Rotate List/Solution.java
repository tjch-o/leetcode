class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null || k == 0) {
            return head;
        }
        
        int lengthOfList = lengthOfLinkedList(head);
        k = k % lengthOfList;

        for (int i = 0; i < k; i += 1) {
            head = rotateRightOnce(head);
        }

        return head;
    }

    public ListNode rotateRightOnce(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        } else {
            ListNode tail = head.next; 
            while (tail.next != null) {
                tail = tail.next;
            }

            // make the list circular
            tail.next = head;

            ListNode newHead = head.next;
            ListNode newTail = head;
            while (newHead.next != head) {
                // the newTail pointer is always one node behind the newHead
                newHead = newHead.next;
                newTail = newTail.next;
            }
            newTail.next = null;

            return newHead;
        }
    }

    public int lengthOfLinkedList(ListNode head) {
        if (head == null) {
            return 0;
        }
        return 1 + lengthOfLinkedList(head.next);
    }
}