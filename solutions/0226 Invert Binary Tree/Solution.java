class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return null;
        } else {
            TreeNode temp = new TreeNode();
            temp = root.left;
            root.left = root.right;
            root.right = temp;
            invertTree(root.left);
            invertTree(root.right);
            return root;
        }
    }
}