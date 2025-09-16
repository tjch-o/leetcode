class MyCircularQueue {
    private int[] data;
    private int count;
    private int capacity;
    private int front;
    private int rear;

    public MyCircularQueue(int k) {
        this.data = new int[k];
        this.capacity = k;
        this.count = 0;
        this.front = 0;
        this.rear = 0;
    }
    
    public boolean enQueue(int value) {
        if (isFull()) {
            return false;
        }

        count += 1;
        data[rear] = value;
        rear = (rear + 1) % capacity;
        return true;
    }
    
    public boolean deQueue() {
        if (isEmpty()) {
            return false;
        }

        count -= 1;
        front = (front + 1) % capacity;
        return true;
    }
    
    public int Front() {
        if (isEmpty()) {
            return -1;
        }
        return data[front];
    }
    
    public int Rear() {
        if (isEmpty()) {
            return -1;
        }
        return data[(rear - 1 + capacity) % capacity];
    }
    
    public boolean isEmpty() {
        return count == 0;
    }
    
    public boolean isFull() {
        return count == capacity;
    }
}