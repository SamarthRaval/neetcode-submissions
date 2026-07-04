class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        deque = collections.deque()
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    deque.append((i,j))

        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        while deque:
            count += 1
            for i in range(len(deque)):
                land = deque.popleft()
                row = land[0]
                col = land[1]

                for direction in directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]

                    if 0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col]==2147483647:
                        grid[new_row][new_col] = count
                        deque.append((new_row, new_col))


        