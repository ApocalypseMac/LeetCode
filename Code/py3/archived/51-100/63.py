from collections import deque
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # BFS
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1: # Start or finish is obstacle
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        obstacleGrid[0][0] = -1
        queue = deque([(0, 0)])
        while queue:
            i, j = queue.popleft()
            if i + 1 < m and obstacleGrid[i + 1][j] == 0:
                temp = obstacleGrid[i][j]
                if j and obstacleGrid[i + 1][j - 1] < 0:
                    temp += obstacleGrid[i + 1][j - 1]
                obstacleGrid[i + 1][j] = temp
                queue.append((i + 1, j))
            if j + 1 < n and obstacleGrid[i][j + 1] == 0:
                temp = obstacleGrid[i][j]
                if i and obstacleGrid[i - 1][j + 1] < 0:
                    temp += obstacleGrid[i - 1][j + 1]
                obstacleGrid[i][j + 1] = temp
                queue.append((i, j + 1))
        return -obstacleGrid[-1][-1]