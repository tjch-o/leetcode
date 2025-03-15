import java.util.Stack;

class StockSpanner {
    private Stack<int[]> stockHistory;

    public StockSpanner() {
        stockHistory = new Stack<>();
    }
    
    public int next(int price) {
        int span = 1;

        while (!stockHistory.isEmpty() && stockHistory.peek()[0] <= price) {
            span += stockHistory.peek()[1];
            stockHistory.pop();
        }

        stockHistory.push(new int[]{price, span});
        return span;
    }
}