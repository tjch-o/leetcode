class Solution {
    public double myPow(double x, int n) {
        if (n == 0) {
            return 1;
        } else if (x == 1) {
            return 1;
        } else if (n == 1) {
            return x;
        } else if (n == Integer.MIN_VALUE) {
            // prevents integer overflow when we negative sign of n
            x = 1 / x;
            return myPow(x, - n - 1) * x;
        } else if (n < 0) {
            x = 1 / x;
            n = -n;
            return myPow(x, n);
        } else if (n % 2 == 0) {
            return myPow(x * x, n / 2);
        } else {
            return myPow(x * x, (n - 1) / 2) * x;
        }
    }
}