public class Solution {
    public int kthSmallest(TreeNode root, int k) {
        int left = countNode(root.left);

        if (k == left + 1) {
            return root.val;
        } else if (k > left + 1) {
            return kthSmallest(root.right, k - left - 1);
        } else {
            return kthSmallest(root.left, k);
        }
    }

    public int countNode(TreeNode root) {
        if (root == null) {
            return 0;
        } else {
            return 1 + countNode(root.left) + countNode(root.right);
        }
    }
}
