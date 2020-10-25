from collections import deque
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        di = [1, 0, -1, 0]
        dj = [0, 1, 0, -1]
        def valid(d):
            visited = [[False] * n for _ in range(m)]
            visited[0][0] = True
            queue = deque([(0, 0)])
            while queue:
                i, j = queue.popleft()
                for k in range(4):
                    ni, nj = i + di[k], j + dj[k]
                    if 0 <= ni < m and 0 <= nj < n and visited[ni][nj] is False and abs(heights[ni][nj] - heights[i][j]) <= d:
                        visited[ni][nj] = True
                        queue.append((ni, nj))
            return visited[-1][-1]
        lo, hi = 0, 10 ** 6 + 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if valid(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
            