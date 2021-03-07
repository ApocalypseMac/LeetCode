import heapq
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        edge = [[] for _ in range(n + 1)]
        for u, v, c in edges:
            edge[u].append((v, c))
            edge[v].append((u, c))
        # dijkstra
        dis = [-1] * (n + 1)
        pq = []
        heapq.heappush(pq, (0, n))
        while pq:
            c, u = heapq.heappop(pq)
            if dis[u] >= 0:
                continue
            dis[u] = c
            for v, cc in edge[u]:
                if dis[v] >= 0:
                    continue
                heapq.heappush(pq, (cc + c, v))
            # print(u, dis, pq)
        # print(dis)
        # dp = [-1] * (n + 1)
        # dp[n] = 1
        @lru_cache(None)
        def helper(u):
            if u == n:
                return 1
            res = 0
            for v, _ in edge[u]:
                if dis[u] > dis[v]:
                    res += helper(v)
                    res %= 10 ** 9 + 7
            return res
        
        return helper(1)
                    
                    
            
            