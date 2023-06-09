class Solution {
    public int[] searchRange(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;

        /* we don't use start < end because we may miss the last occurrence of the target element 
        we are looking for a range here which is different from the normal binary search algorithm 
        that looks for an element */
        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (nums[mid] == target) {
                int first = mid;
                int last = mid;

                while (first >= 0 && nums[first] == target) {
                    first -= 1;
                }

                while (last < nums.length && nums[last] == target) {
                    last += 1;
                }

                /* we cannot return { first, last } because we increment last and decrease first 
                until the element at the indexes are no longer the same as the target; which means 
                we are now one position left and right from the range*/ 
                return new int[] { first + 1, last - 1 };
            } else if (nums[mid] > target) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }

        return new int[] { -1, -1 };
    }
}