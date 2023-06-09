class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        } else {
            return isSubtreesSymmetric(root.left, root.right);
        }
    }

    public boolean isSubtreesSymmetric(TreeNode leftSubtree, TreeNode rightSubtree) {
        if (leftSubtree == null && rightSubtree == null) {
            return true;
        } else if (leftSubtree != null && rightSubtree == null) {
            return false;
        } else if (leftSubtree == null && rightSubtree != null) {
            return false;
        } else {
            return leftSubtree.val == rightSubtree.val && 
            isSubtreesSymmetric(leftSubtree.left, rightSubtree.right) && 
            isSubtreesSymmetric(leftSubtree.right, rightSubtree.left);
        }
    }
}