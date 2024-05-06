class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode output = null;
        
        for (int i = 0; i < lists.length; i += 1) {
            output = mergeTwoLists(output, lists[i]);
        }

        return output;
    }

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) {
            return l2;
        } else if (l2 == null) {
            return l1;
        } else {
            if (l1.val <= l2.val) {
               ListNode merged = mergeTwoLists(l1.next, l2);
               l1.next = merged;
               return l1;
            } else {
                ListNode merged = mergeTwoLists(l1, l2.next);
                l2.next = merged;
                return l2;
            }
        }
    }
}