import java.util.ArrayList;

public class Solution {
    ArrayList<ListNode> seen = new ArrayList();

    public ListNode detectCycle(ListNode head) {
        if (head == null) {
            return null;
        } else if (seen.contains(head)) {
            return head;
        } else {
            seen.add(head);
            return detectCycle(head.next);
        }
    }
}