class Solution {
    public boolean isPerfectSquare(int num) {
        if (num == 0 || num == 1) {
            return true;
        }

        long low = 1;
        long high = num;
        while (low <= high) {
            long middle = low + (high - low) / 2;
            long square = middle * middle;
            if (square == num) {
                return true;
            } else if (square > num) {
                high = middle - 1;
            } else {
                low = middle + 1;
            }
        }

        return false;
    }
}