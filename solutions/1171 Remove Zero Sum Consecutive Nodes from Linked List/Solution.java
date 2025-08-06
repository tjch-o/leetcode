import java.util.HashMap;

class Solution {
    public ListNode removeZeroSumSublists(ListNode head) {
        HashMap<Integer, ListNode> prefixSumMap = new HashMap<>();
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        int prefixSum = 0;
        prefixSumMap.put(prefixSum, dummy);
        ListNode curr = head;

        while (curr != null) {
            prefixSum += curr.val;

            if (prefixSumMap.containsKey(prefixSum)) {
                ListNode prev = prefixSumMap.get(prefixSum);
                removeNodes(prev, curr, prefixSumMap, prefixSum);
                prev.next = curr.next;
            } else{
                prefixSumMap.put(prefixSum, curr);
            }
            
            curr = curr.next;
        }

        return dummy.next;
    }

    public void removeNodes(ListNode start, ListNode end, HashMap<Integer, ListNode> prefixSumMap, int prefixSum) {
        ListNode curr = start.next;
        int currSum = prefixSum;

        while (curr != end) {
            currSum += curr.val;
            prefixSumMap.remove(currSum);
            curr = curr.next;
        }
    }
}
