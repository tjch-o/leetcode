class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }
        return isMirrored(root.left, root.right);
    }

    public boolean isMirrored(TreeNode left, TreeNode right) {
        if (left == null && right == null) {
            return true;
        } else if (left == null || right == null) {
            return false;
        } else {
            return isMirrored(left.left, right.right) && left.val == right.val && isMirrored(left.right, right.left);
        }
    }
}