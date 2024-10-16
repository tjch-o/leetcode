public class Solution {
    /**
     * @param root: The root of the BST.
     * @param p: The node.
     * @return: Successor of p.
     */
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        if (root == null) {
            return root;
        }

        TreeNode successor = null;

        while (root != null) {
            if (p.val < root.val) {
                successor = root;
                root = root.left;
            } else {
                root = root.right;
            }
        }
        return successor;
    }
}