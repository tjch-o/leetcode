import java.util.Collections;
import java.util.PriorityQueue;

class MedianFinder {
    // min heap to store values above the median, max heap to store values below the median
    PriorityQueue<Integer> minHeap;
    PriorityQueue<Integer> maxHeap;

    public MedianFinder() {
        minHeap = new PriorityQueue<>();
        maxHeap = new PriorityQueue<>(Collections.reverseOrder());
    }
    
    public void addNum(int num) {
        // need to ensure 0 <= maxHeap.size() - minHeap.size() <= 1 after addition
        if (maxHeap.size() == minHeap.size()) {
            if (minHeap.peek() != null && num > minHeap.peek()) {
                // balance both heaps by shifting lowest priority of the minHeap to the maxHeap
                maxHeap.offer(minHeap.poll());
                minHeap.offer(num);
            } else {
                maxHeap.offer(num);
            }
        } else {
            if (num < maxHeap.peek()) {
                // balance both heaps by shifting highest priority of the maxHeap to the minHeap
                minHeap.offer(maxHeap.poll());
                maxHeap.offer(num);
            } else {
                minHeap.offer(num);
            }
        }
    }
    
    public double findMedian() {
        int totalSize = minHeap.size() + maxHeap.size();
        if (totalSize % 2 == 0) {
            double sum = minHeap.peek() + maxHeap.peek();
            return sum / 2;
        } else {
            return maxHeap.peek();
        }
    }
}
