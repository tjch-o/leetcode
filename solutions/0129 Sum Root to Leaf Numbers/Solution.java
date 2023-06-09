class Solution {
    public int sumNumbers(TreeNode root) {
        return sumNumbersHelper(root, 0);
    }

    public int sumNumbersHelper(TreeNode root, int accumulate) {
        if (root == null) {
            return accumulate;
        } else if (root.left == null && root.right == null) {
            return accumulate + root.val;
        } else {
            int newAccumulate = (accumulate + root.val) * 10;
            
            if (root.left != null && root.right == null) {
                return sumNumbersHelper(root.left, newAccumulate);
            } else if (root.left == null && root.right != null) {
                return sumNumbersHelper(root.right, newAccumulate);
            } else {
                return sumNumbersHelper(root.left, newAccumulate) + 
                sumNumbersHelper(root.right, newAccumulate);
            }
        }
    }
}