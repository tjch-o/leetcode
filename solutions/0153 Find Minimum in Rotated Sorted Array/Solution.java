class Solution {
    public int findMin(int[] nums) {
        int start = 0;
        int end = nums.length - 1;

        while (start < end) {
            int middle = start + (end - start) / 2;
            int current = nums[middle];

            if (current <= nums[end]) {
                // from middle to end is already sorted so min must be in left half
                end = middle;
            } else {
                // there is a change in direction so min must be in right half
                start = middle + 1;
            }
        }

        return nums[start];
    }
}