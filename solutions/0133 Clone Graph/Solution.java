import java.util.HashMap;

class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) {
            return null;
        }
        
        // key is the current node value is the cloned node
        HashMap<Node, Node> visited = new HashMap<>();
        return cloneNode(node, visited);
    }

    public Node cloneNode(Node node, HashMap<Node, Node> visited) {
        if (visited.containsKey(node)) {
            return visited.get(node);
        } else if (node.neighbors.size() == 0) {
            return new Node(node.val);
        } else {
            Node clonedNode = new Node(node.val);
            visited.put(node, clonedNode);

            for (int i = 0; i < node.neighbors.size(); i += 1) {
                Node currentNode = cloneNode(node.neighbors.get(i), visited);
                clonedNode.neighbors.add(currentNode);
            }

            return clonedNode;
        }
    }
}