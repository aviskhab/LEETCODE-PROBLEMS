class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Initialize sets and collect empty cells
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    empty.append((r, c))
                else:
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + c // 3].add(num)

        def backtrack(pos):
            if pos == len(empty):
                return True

            # Choose the empty cell with the fewest candidates
            best = pos
            min_count = 10

            for i in range(pos, len(empty)):
                r, c = empty[i]
                b = (r // 3) * 3 + c // 3
                count = sum(
                    str(n) not in rows[r]
                    and str(n) not in cols[c]
                    and str(n) not in boxes[b]
                    for n in range(1, 10)
                )

                if count < min_count:
                    min_count = count
                    best = i

                if count == 0:
                    return False

                if count == 1:
                    break

            empty[pos], empty[best] = empty[best], empty[pos]

            r, c = empty[pos]
            b = (r // 3) * 3 + c // 3

            for n in range(1, 10):
                num = str(n)

                if (num not in rows[r]
                    and num not in cols[c]
                    and num not in boxes[b]):

                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[b].add(num)

                    if backtrack(pos + 1):
                        return True

                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[b].remove(num)

            empty[pos], empty[best] = empty[best], empty[pos]
            return False

        backtrack(0)