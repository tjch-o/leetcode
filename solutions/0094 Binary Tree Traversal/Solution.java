import java.util.ArrayList;
import java.util.List;

class Solution {
    ArrayList<Integer> output = new ArrayList<>();

    // update the array first don't return anything
    public void inorderTraversalHelper(TreeNode root) {
        if (root != null) {
            inorderTraversalHelper(root.left);
            output.add(root.val);
            inorderTraversalHelper(root.right);
        }
    }

    public List<Integer> inorderTraversal(TreeNode root) {
        inorderTraversalHelper(root);
        return output;
    }  
}