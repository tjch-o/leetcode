import java.util.ArrayList;

public class Solution {

    ArrayList<ListNode> seen = new ArrayList<>();

    public boolean hasCycle(ListNode head) {
        if (head == null) {
            return false;
        } else if (seen.contains(head)) {
            return true;
        } else {
            seen.add(head);
            return hasCycle(head.next);
        }
    }
}