class Solution {
    public int numIslands(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int count = 0;

        for (int i = 0; i < m; i += 1) {
            for (int j = 0; j < n; j += 1) {
                if (grid[i][j] == '1') {
                    count += 1;
                    DFS(i, j, grid, m, n);
                }
            }
        }

        return count;
    }

    public void DFS(int row, int col, char[][] grid, int m, int n) {
        if (row < 0 || row > (m - 1) || col < 0 || col > (n - 1) || grid[row][col] == '0') {
            return ;
        }

        // mark this as visited to prevent double counting
        grid[row][col] = '0';

        DFS(row - 1, col, grid, m, n);
        DFS(row + 1, col, grid, m, n);
        DFS(row, col - 1, grid, m, n);
        DFS(row, col + 1, grid, m, n);
    }
}