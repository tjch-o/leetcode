class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums.length == 0) {
            return null;
        }
        return sortedArrayToBSTHelper(nums, 0, nums.length - 1);
    }

    public TreeNode sortedArrayToBSTHelper(int[] nums, int start, int end) {
        if (start > end) {
            return null;
        }

        int middle = start + (end - start) / 2;
        TreeNode left = sortedArrayToBSTHelper(nums, start, middle - 1);
        TreeNode right = sortedArrayToBSTHelper(nums, middle + 1, end);
        TreeNode root = new TreeNode(nums[middle], left, right);
        return root;
    }
}