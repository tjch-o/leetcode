class Solution {
    public boolean isValidBST(TreeNode root) {
        return isValidBSTHelper(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    public boolean isValidBSTHelper(TreeNode root, long min, long max) {
        if (root == null) {
            return true;
        } else if (root.val <= min || root.val >= max) {
            return false;
        } 

        boolean isLeftSubtreeValid = isValidBSTHelper(root.left, min, root.val);
        boolean isRightSubtreeValid = isValidBSTHelper(root.right, root.val, max);
        return isLeftSubtreeValid && isRightSubtreeValid;
    }
}