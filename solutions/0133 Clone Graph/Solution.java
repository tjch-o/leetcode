import java.util.HashMap;

class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) {
            return null;
        }

        HashMap<Node, Node> visited = new HashMap<>();
        return cloneNode(node, visited);
    }

    public Node cloneNode(Node node, HashMap<Node, Node> visited) {
        if (visited.containsKey(node)) {
            return visited.get(node);
        }

        Node clonedNode = new Node(node.val);
        visited.put(node, clonedNode);

        if (node.neighbors.size() > 0) {
            for (int i = 0; i < node.neighbors.size(); i += 1) {
                Node clonedNeighbour = cloneNode(node.neighbors.get(i), visited);
                clonedNode.neighbors.add(clonedNeighbour);
            }
        }

        return clonedNode;
    }
}
