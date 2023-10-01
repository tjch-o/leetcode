class Solution {
    public int lengthOfLIS(int[] nums) {
        if (nums.length == 0 || nums.length == 1) {
            return nums.length;
        } else {
            int max = 0;
            int n = nums.length;
            int[] table = new int[n];
            table[0] = 1;

            for (int i = 0; i < n; i += 1) {
                int prevMax = 0;
                for (int j = 0; j < i; j += 1) {
                    // possible to increase LIS at i using subsequence ending at j when nums[i] > nums[j]
                    if (nums[i] > nums[j]) {
                        prevMax = Math.max(prevMax, table[j]);
                    }
                    // prevMax is the max LIS of the subsequences before i then we +1 
                    table[i] = prevMax + 1;
                    max = Math.max(max, table[i]);
                }
            }

            return max;
        }
    }
}