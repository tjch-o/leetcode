class NumMatrix:
    def __init__(self, matrix):
        self.mat = matrix
        m, n = len(self.mat), len(self.mat[0])
        self.prefix_sums = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                overlap = self.prefix_sums[i][j]
                self.prefix_sums[i + 1][j + 1] = (
                    self.mat[i][j]
                    + self.prefix_sums[i][j + 1]
                    + self.prefix_sums[i + 1][j]
                    - overlap
                )

    def sum_region(self, r1, c1, r2, c2):
        above = self.prefix_sums[r1][c2 + 1]
        left = self.prefix_sums[r2 + 1][c1]
        return (
            self.prefix_sums[r2 + 1][c2 + 1] + self.prefix_sums[r1][c1] - above - left
        )
