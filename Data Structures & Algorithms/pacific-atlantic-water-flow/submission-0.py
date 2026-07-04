class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, sett):
            if r<0 or r>=rows or c<0 or c>=cols or (r,c) in sett:
                return

            sett.add((r,c))

            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            for direction in directions:
                new_row = direction[0] + r
                new_col = direction[1] + c

                if 0<=new_row<rows and 0<=new_col<cols and heights[new_row][new_col] >= heights[r][c]:
                    dfs(new_row, new_col, sett)

            return 

        for i in range(rows):
            dfs(i, 0, pacific)
            dfs(i, cols-1, atlantic)

        for j in range(cols):
            dfs(0, j, pacific)
            dfs(rows-1, j, atlantic)

        output = []
        for i in range(rows):
            for j in range(cols):
                if (i, j) in pacific and (i,j) in atlantic:
                    output.append([i,j])

        return output
