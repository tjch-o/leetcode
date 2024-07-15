import java.util.ArrayList;

class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        ArrayList<Integer> path = new ArrayList<>();
        rightView(root, path, 0);
        return path;
    }

    public void rightView(TreeNode root, List<Integer> path, int currDepth) {
        if (root == null) {
            return;
        }

        if (currDepth == path.size()) {
            path.add(root.val);
        }
        
        rightView(root.right, path, currDepth + 1);
        rightView(root.left, path, currDepth + 1);
    }
}   