class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        visited = set()

        def dfs(i, j):
            if i<0 or i>=rows or j<0 or j>=cols or (i,j) in visited or grid[i][j]=="0":
                return
            
            visited.add((i,j))

            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)

            return
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i,j)
                    islands += 1

        return islands