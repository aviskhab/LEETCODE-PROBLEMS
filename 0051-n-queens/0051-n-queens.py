
class Solution:
    def solveNQueens(self, n: int):
        result = []

        board = [["."] * n for _ in range(n)]

        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col

        def backtrack(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):

                # Check if queen can be placed safely
                if (col in cols or
                    row - col in diag1 or
                    row + col in diag2):
                    continue

                # Place queen
                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Move to next row
                backtrack(row + 1)

                # Backtrack: remove queen
                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)

        return result
