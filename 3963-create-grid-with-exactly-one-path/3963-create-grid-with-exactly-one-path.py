class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#'] * n for _ in range(m)]

        # Make the first row free
        for j in range(n):
            grid[0][j] = '.'

        # Make the last column free
        for i in range(m):
            grid[i][n - 1] = '.'

        return [''.join(row) for row in grid]