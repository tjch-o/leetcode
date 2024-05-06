import java.util.ArrayList;
import java.util.ArrayDeque;
import java.util.List;

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        ArrayDeque<TreeNode> queue = new ArrayDeque<>();

        if (root == null) {
            return result;
        }

        queue.add(root);

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            ArrayList<Integer> currentLevel = new ArrayList<>();

            for (int i = 0; i < levelSize; i += 1) {
                TreeNode curr = queue.pop();

                if (curr.left != null) {
                    queue.add(curr.left);
                } 

                if (curr.right != null) {
                    queue.add(curr.right);
                }

                currentLevel.add(curr.val);
            }

            result.add(currentLevel);
        }

        return result;
    }
}
