import java.util.ArrayList;

class MyHashMap {
    private ArrayList<ListNode> arr;

    public MyHashMap() {
        this.arr = new ArrayList<>();

        for (double i = 0; i < Math.pow(10, 4); i += 1) {
            arr.add(new ListNode(0));
        }
    }
    
    public void put(int key, int value) {
        int idx = key % (arr.size());
        ListNode curr = arr.get(idx);

        while (curr.next != null) {
            if (curr.next.key == key) {
                curr.next.val = value;
                return;
            }
            curr = curr.next;
        }
        curr.next = new ListNode(key, value);
    }
    
    public int get(int key) {
        int idx = key % (arr.size());
        ListNode curr = arr.get(idx);

        while (curr.next != null) {
            if (curr.next.key == key) {
                return curr.next.val;
            }
            curr = curr.next;
        }
        return -1;
    }
    
    public void remove(int key) {
        int idx = key % (arr.size());
        ListNode curr = arr.get(idx);

        while (curr.next != null) {
            if (curr.next.key == key) {
                curr.next = curr.next.next;
                break;
            }
            curr = curr.next;
        }
        return;
    }
}