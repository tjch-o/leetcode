public class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        } else if (p == null || q == null) {
            return false;
        } else {
            return isSameTree(p.left, q.left) && p.val == q.val && isSameTree(p.right, q.right);
        }
    }
}