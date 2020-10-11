class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        edges = [[False] * n for _ in range(n)]
        numedge = [0] * n
        for x, y in roads:
            numedge[x] += 1
            numedge[y] += 1
            edges[x][y] = True
            edges[y][x] = True
        res = 0
        for x in range(n):
            for y in range(x + 1, n):
                rks = numedge[x] + numedge[y]
                if edges[x][y]:
                    rks -= 1
                res = max(res, rks)
        return res
                
        