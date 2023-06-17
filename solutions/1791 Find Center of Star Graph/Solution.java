import java.util.ArrayList;

class Solution {
    public int findCenter(int[][] edges) {
        ArrayList<ArrayList<Integer>> adjacencyList = new ArrayList<>();

        // given that edges.length = n - 1
        for (int i = 0; i < edges.length + 1; i += 1) {
            adjacencyList.add(new ArrayList<Integer>());
        }

        for (int i = 0; i < edges.length; i += 1) {
            int[] edge = edges[i];
            int n1 = edge[0];
            int n2 = edge[1];
            adjacencyList.get(n1 - 1).add(n2);
            adjacencyList.get(n2 - 1).add(n1);
        }

        int centre = -1;
        for (int i = 0; i < adjacencyList.size(); i += 1) {
            ArrayList<Integer> current = adjacencyList.get(i);
            if (current.size() == edges.length) {
                centre = i + 1;
            }
        }

        return centre;
    }
}