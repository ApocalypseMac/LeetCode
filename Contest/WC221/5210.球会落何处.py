class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        places = [_ for _ in range(n)]
        for i in range(m):
            for j in range(n):
                p = places[j]
                if p != -1:
                    if grid[i][p] == 1:
                        if p < n - 1 and grid[i][p + 1] == 1:
                            places[j] += 1
                        else:
                            places[j] = -1
                    else:
                        if p > 0 and grid[i][p - 1] == -1:
                            places[j] -= 1
                        else:
                            places[j] = -1
        return places
                        