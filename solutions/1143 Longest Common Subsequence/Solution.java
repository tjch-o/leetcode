public class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        if (text1.equals(text2)) {
            return text1.length();
        } else {
            int m = text1.length();
            int n = text2.length();
            int[][] table = new int[m + 1][n + 1];

            for (int i = 1; i <= m; i += 1) {
                for (int j = 1; j <= n; j += 1) {
                    char c1 = text1.charAt(i - 1);
                    char c2 = text2.charAt(j - 1);
                    if (c1 == c2) {
                        // only when both characters match then can increase LCS 
                        table[i][j] = table[i - 1][j - 1] + 1;
                    } else {
                        table[i][j] = Math.max(table[i - 1][j], table[i][j - 1]);
                    }
                }
            }

            return table[m][n];
        }
    }
}