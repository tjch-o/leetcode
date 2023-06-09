class Solution {
    public boolean isValidBST(TreeNode root) {
        return isValidBSTHelper(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    public boolean isValidBSTHelper(TreeNode root, long min, long max) {
        // validating BST is not just checking left and right node values
        if (root == null) {
            return true;
        } else if (root.val <= min) {
            return false;
        } else if (root.val >= max) {
            return false;
        } else {
            boolean validateLeftSubtree = isValidBSTHelper(root.left, min, root.val);
            boolean validateRightSubtree = isValidBSTHelper(root.right, root.val, max);
            return validateLeftSubtree && validateRightSubtree;
        }
    }
}