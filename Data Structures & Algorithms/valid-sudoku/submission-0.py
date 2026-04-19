class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        square = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                else:
                    cur=board[i][j]
                    if (cur in rows[i] or cur in cols[j] or cur in square[(i//3,j//3)]):
                        return False
                rows[i].add(cur)
                cols[j].add(cur)
                square[(i//3,j//3)].add(cur)
        return True