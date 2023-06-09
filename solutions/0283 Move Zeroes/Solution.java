class Solution {
    public void moveZeroes(int[] nums) {
        int leftMostZero = 0;

        for (int i = 0; i < nums.length; i += 1) {
            if (nums[i] != 0) {
                if (i != leftMostZero) {
                    swap(nums, i, leftMostZero);
                }
                leftMostZero += 1;   
            }
        }
    }

    public void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}