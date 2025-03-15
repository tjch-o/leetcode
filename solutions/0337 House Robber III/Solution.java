class Solution {
    public int rob(TreeNode root) {
        int[] pathSums = dfs(root);
        return Math.max(pathSums[0], pathSums[1]);
    }

    public int[] dfs(TreeNode node) {
        if (node == null) {
            return new int[]{0, 0};
        }

        int[] left = dfs(node.left);
        int[] right = dfs(node.right);

        int maxIncluded = left[0] + node.val + right[0];
        int maxExcluded = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
        return new int[]{maxExcluded, maxIncluded};
    }
}