class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int m = image.length;
        int n = image[0].length;
        int srcColour = image[sr][sc];
        
        DFS(image, sr, sc, color, srcColour, m, n);
        return image;
    }

    public void DFS(int[][] image, int sr, int sc, int color, int srcColour, int m, int n) {
        if (sr < 0 || sc < 0 || sr >= m || sc >= n || srcColour == color || 
        image[sr][sc] != srcColour) {
            return;
        } 

        image[sr][sc] = color;
        DFS(image, sr - 1, sc, color, srcColour, m, n);
        DFS(image, sr + 1, sc, color, srcColour, m, n);
        DFS(image, sr, sc - 1, color, srcColour, m, n);
        DFS(image, sr, sc + 1, color, srcColour, m, n);
    }
}