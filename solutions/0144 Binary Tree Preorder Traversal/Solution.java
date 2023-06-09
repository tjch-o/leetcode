import java.util.ArrayList;

class Solution {
    ArrayList<Integer> output = new ArrayList<>();

    public List<Integer> preorderTraversal(TreeNode root) {
        if (root == null) {
            return output;
        } else {
            output.add(root.val);
            preorderTraversal(root.left);
            preorderTraversal(root.right);
            return output;
        }
    }
}