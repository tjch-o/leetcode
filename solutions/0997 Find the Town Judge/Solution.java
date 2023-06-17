import java.util.ArrayList;

class Solution {
    public int findJudge(int n, int[][] trust) {
        ArrayList<ArrayList<Integer>> adjacencyList = new ArrayList<>();

        for (int i = 0; i < n; i += 1) {
            adjacencyList.add(new ArrayList<Integer>());
        }

        int numEdges = trust.length;
        for (int i = 0; i < numEdges; i += 1) {
            int[] currentEdge = trust[i];
            int from = currentEdge[0];
            int to = currentEdge[1];
            // people are labeled from 1 to n
            adjacencyList.get(from - 1).add(to);
        }

        int countEmptyNbrLists = 0;
        int judge = -1;
        for (int i = 0; i < n; i += 1) {
            ArrayList<Integer> currNbrList = adjacencyList.get(i);
            if (currNbrList.isEmpty()) {
                judge = i + 1;
                countEmptyNbrLists += 1;
            }
        }

        int countTrust = 0;
        for (int j = 0; j < n; j += 1) {
            ArrayList<Integer> currNbrList = adjacencyList.get(j);
            if (currNbrList.contains(judge)) {
                countTrust += 1;
            }
        }
        
        return countEmptyNbrLists == 1 && countTrust == n - 1 ? judge: -1;
    }
}