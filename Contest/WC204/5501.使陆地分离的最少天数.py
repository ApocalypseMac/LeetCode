from collections import deque
from copy import deepcopy
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        grid1 = copy.deepcopy(grid)
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        '''
        def neighbour(x, y): # 1 count
            res = 0
            for i in range(4):
                x1, y1 = x + dx[i], y + dy[i]
                if 0 <= x1 < m and 0 <= y1 < n:
                    res += grid[x1][y1]
            return res
        '''
        
        def bfs(grid, i, j):
            queue = deque([(i, j)])
            grid[i][j] = 0
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    x1, y1 = x + dx[i], y + dy[i]
                    if 0 <= x1 < m and 0 <= y1 < n and grid[x1][y1] == 1:
                        grid[x1][y1] = 0
                        queue.append((x1, y1))
            return
            
        
        def islandcount(grid):
            grid1 = copy.deepcopy(grid)
            count = 0
            for i in range(m):
                for j in range(n):
                    if grid1[i][j] == 1:
                        bfs(grid1, i, j)
                        count += 1
            return count
        
        if islandcount(grid) > 1:
            return 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    count = islandcount(grid)
                    if count > 1:
                        return 1
                    grid[i][j] = 1
        return 2
                    