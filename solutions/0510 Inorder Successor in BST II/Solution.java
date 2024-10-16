public class Solution {
    /**
     * @param node: random node in binary search tree
     * @return: the inorder successor of current node
     */
    public ParentTreeNode inorderSuccessor(ParentTreeNode node) {
        if (node == null) {
            return node;
        }

        ParentTreeNode successor;

        if (node.right != null) {
            successor = node.right;

            while (successor.left != null) {
                successor = successor.left;
            }
            return successor;
        }

        while (node.parent != null && node == node.parent.right) {
            node = node.parent;
        }
        return node.parent;
    }
}