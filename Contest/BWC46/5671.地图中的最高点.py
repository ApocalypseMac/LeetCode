from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        res = [[-1] * n for _ in range(m)]
        queue = deque([])
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append((i, j, 0))
                    res[i][j] = 0
        while queue:
            i, j, h = queue.popleft()
            for k in range(4):
                ni, nj = i + dx[k], j + dy[k]
                # print(ni, nj)
                if 0 <= ni < m and 0 <= nj < n and res[ni][nj] == -1:
                    res[ni][nj] = h + 1
                    queue.append((ni, nj, h + 1))
        return res
                
                    
        