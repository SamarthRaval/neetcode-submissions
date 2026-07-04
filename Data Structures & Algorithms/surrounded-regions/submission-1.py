class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(r, c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return

            board[r][c] = "NS"
            
            for direction in directions:
                new_row = r + direction[0]
                new_col = c + direction[1]

                if 0<=new_row<rows and 0<=new_col<cols and board[new_row][new_col] == "O":
                    dfs(new_row, new_col)

        for i in range(rows):
            for j in range(cols):
                if (i==0 or i==rows-1 or j==0 or j==cols-1) and board[i][j] == "O":
                    dfs(i,j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "NS":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"