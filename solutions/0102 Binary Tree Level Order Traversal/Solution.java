import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();

        if (root == null) {
            return result;
        }

        List<TreeNode> queue = new ArrayList<>();
        queue.add(root);

        // essentially doing a BFS
        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            List<Integer> currentLevel = new ArrayList<>();
            List<TreeNode> nextFrontier = new ArrayList<>();

            for (int i = 0; i < levelSize; i += 1) {
                TreeNode currentNode = queue.remove(0);
                currentLevel.add(currentNode.val);
                
                if (currentNode.left != null) {
                    nextFrontier.add(currentNode.left);
                }

                if (currentNode.right != null) {
                    nextFrontier.add(currentNode.right);
                }
            }

            result.add(currentLevel);
            queue.addAll(nextFrontier);
        }

        return result;
    }
}