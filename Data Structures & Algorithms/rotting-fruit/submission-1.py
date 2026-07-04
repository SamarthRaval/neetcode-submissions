class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        deque = collections.deque()
        minutes = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    deque.append((i,j))

        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        count = 0
        while deque:
            
            for i in range(len(deque)):
                rotten = deque.popleft()
                for direction in directions:
                    new_row = direction[0] + rotten[0]
                    new_col = direction[1] + rotten[1]

                    if 0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col] == 1:
                        count += 1
                        grid[new_row][new_col] = 2
                        deque.append((new_row,new_col))

            if deque:
                minutes += 1

        # print(count)
        # print(minutes)

        return minutes if count == fresh else -1