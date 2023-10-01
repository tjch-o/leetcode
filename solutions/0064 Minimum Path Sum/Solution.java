class Solution {
    public int minPathSum(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] pathSum = new int[m][n];
        pathSum[0][0] = grid[0][0];

        for (int i = 1; i < m; i += 1) {
            pathSum[i][0] = pathSum[i - 1][0] + grid[i][0];
        }

        for (int j = 1; j < n; j += 1) {
            pathSum[0][j] = pathSum[0][j - 1] + grid[0][j];
        }

        for (int i = 1; i < m; i += 1) {
            for (int j = 1; j < n; j += 1) {
                if (i >= 0 && j >= 0) {
                    pathSum[i][j] = grid[i][j] + Math.min(pathSum[i - 1][j], pathSum[i][j - 1]);
                }
            }
        }

        return pathSum[m - 1][n - 1];
    }
}