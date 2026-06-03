class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])


        def dfs(r,c,i):
            if len(word) == i:
                return True
            if COL <= c or ROW <= r:
                return False
            if c < 0 or r < 0:
                return False
            if word[i] != board[r][c]:
                return False
            if board[r][c] == "#":
                return False
            board[r][c] = "#"
            res = (dfs(r+1,c,i+1) or
                   dfs(r-1,c,i+1) or
                   dfs(r,c+1,i+1) or
                   dfs(r,c-1,i+1))
            board[r][c] = word[i]
            return res
        for r in range(ROW):
            for c in range(COL):
                if dfs(r,c,0) == True:
                    return True
        return False