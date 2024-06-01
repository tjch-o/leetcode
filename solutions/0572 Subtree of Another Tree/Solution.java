class Solution {
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null && subRoot == null) {
            return true;
        } else if (root == null) {
            return false;
        } else if (isSameTree(root, subRoot)) {
            return true;
        } else {
            return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
        }
    }

    public boolean isSameTree(TreeNode x, TreeNode y) {
        if (x == null && y == null) {
            return true;
        } else if (x == null | y == null) {
            return false;
        } else {
            return isSameTree(x.left, y.left) && x.val == y.val && isSameTree(x.right, y.right);
        }
    }
}
