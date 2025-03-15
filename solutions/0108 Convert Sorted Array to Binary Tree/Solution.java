class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        return sortArrayToBSTHelper(nums, 0, nums.length - 1);
    }

    public TreeNode sortArrayToBSTHelper(int[] nums, int start, int end) {
        if (start > end) {
            return null;
        }

        int mid = start + (end - start) / 2;
        TreeNode root = new TreeNode(nums[mid]);
        root.left = sortArrayToBSTHelper(nums, start, mid - 1);
        root.right = sortArrayToBSTHelper(nums, mid + 1, end);
        return root;
    }
}