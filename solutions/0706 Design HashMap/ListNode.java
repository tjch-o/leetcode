public class ListNode {
    public int key;
    public Integer val;
    public ListNode next;

    public ListNode(int key) {
        this.key = key;
        this.val = null;
        this.next = null;
    }

    public ListNode(int key, int val) {
        this.key = key;
        this.val = val;
        this.next = null;
    }
}
