import java.util.PriorityQueue;

class MedianFinder {
    private PriorityQueue<Integer> minHeap;
    private PriorityQueue<Integer> maxHeap;

    public MedianFinder() {
        minHeap = new PriorityQueue<>();
        maxHeap = new PriorityQueue<>((x, y) -> Integer.compare(y, x));
    }
    
    public void addNum(int num) {
        maxHeap.add(num);

        if (!minHeap.isEmpty() && maxHeap.peek() > minHeap.peek()) {
            minHeap.add(maxHeap.poll());
        }

        if (maxHeap.size() > minHeap.size()) {
            minHeap.add(maxHeap.poll());
        } else if (minHeap.size() - maxHeap.size() > 1) {
            maxHeap.add(minHeap.poll());
        }
    }
    
    public double findMedian() {
        int totalSize = minHeap.size() + maxHeap.size();
        if (totalSize % 2 == 0) {
            return (minHeap.peek() + maxHeap.peek()) / 2.0;
        }
        return minHeap.peek();
    }
}