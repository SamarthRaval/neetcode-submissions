class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        deque = collections.deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    deque.append((i,j))

        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while deque:
            count += 1
            for _ in range(len(deque)):
                treasure = deque.popleft()
                for direction in directions:
                    new_row = treasure[0] + direction[0]
                    new_col = treasure[1] + direction[1]

                    if 0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col] == 2147483647:
                        grid[new_row][new_col] = count
                        deque.append((new_row, new_col))
