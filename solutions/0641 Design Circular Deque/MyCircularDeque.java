class MyCircularDeque {
    private int[] data;
    private int count;
    private int capacity;
    private int front;
    private int rear;

    public MyCircularDeque(int k) {
        data = new int[k];
        count = 0;
        capacity = k;
        front = 0;
        rear = 0;
    }
    
    public boolean insertFront(int value) {
        if (isFull()) return false;

        front = (front - 1 + capacity) % capacity;
        data[front] = value;
        count += 1;
        return true;
    }
    
    public boolean insertLast(int value) {
        if (isFull()) return false;

        data[rear] = value;
        rear = (rear + 1) % capacity;
        count += 1;
        return true;
    }
    
    public boolean deleteFront() {
        if (isEmpty()) return false;

        front = (front + 1) % capacity;
        count -= 1;
        return true;
    }
    
    public boolean deleteLast() {
        if (isEmpty()) return false;

        rear = (rear - 1 + capacity) % capacity;
        count -= 1;
        return true;
    }
    
    public int getFront() {
        if (isEmpty()) return -1;
        return data[front];
    }
    
    public int getRear() {
        if (isEmpty()) return -1;
        return data[(rear - 1 + capacity) % capacity];
    }
    
    public boolean isEmpty() {
        return count == 0;
    }
    
    public boolean isFull() {
        return count == capacity;
    }
}