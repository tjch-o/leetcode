class Solution {
    public boolean isPerfectSquare(int num) {
        int start = 1;
        int end = (int) Math.sqrt(num) + 1;

        while (start <= end) {
            int mid = (start + end) / 2;
            int currSquare = mid * mid;

            if (currSquare == num) {
                return true;
            } else if (currSquare > num) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return false;
    }
}