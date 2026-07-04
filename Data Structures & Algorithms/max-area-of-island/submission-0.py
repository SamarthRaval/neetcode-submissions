class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        visited = set()

        def dfs(i,j, area):
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]==0 or (i,j) in visited:
                return area
            
            visited.add((i,j))
            area += 1

            area = dfs(i+1, j, area)
            area = dfs(i, j+1, area)
            area = dfs(i-1, j, area)
            area = dfs(i, j-1, area)

            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area = max(dfs(i,j,0), max_area)

        return max_area
        