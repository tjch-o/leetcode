class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null && list2 == null) {
            return null;
        } else if (list1 == null && list2 != null) {
            return list2;
        } else if (list2 == null && list1 != null) {
            return list1;
        } else {
            if (list1.val > list2.val) {
                ListNode nextNode = mergeTwoLists(list1, list2.next);
                list2.next = nextNode;
                return list2;
            } else {
                ListNode nextNode = mergeTwoLists(list1.next, list2);
                list1.next = nextNode;
                return list1;
            }
        }
    }
}