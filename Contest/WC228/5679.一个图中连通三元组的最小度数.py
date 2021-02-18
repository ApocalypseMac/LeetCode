class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        edges1 = [[False] * (n + 1) for _ in range(n + 1)]
        edges2 = [[] for _ in range(n + 1)]
        degree = [0] * (n + 1)
        for u, v in edges:
            edges1[u][v] = True
            if v > u:
                edges2[u].append(v)
            else:
                edges2[v].append(u)
            edges1[v][u] = True
            degree[u] += 1
            degree[v] += 1
        for _ in range(1, n + 1):
            edges2[_].sort()
        res = 1000000
        for u in range(1, n + 1):
            for v in edges2[u]:
                for w in edges2[v]:
                    if u != w and edges1[u][w]:
                        res = min(res, degree[u] + degree[v] + degree[w] - 6)
        if res == 1000000:
            return -1