class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        degree = [0] * n
        rep = {}
        q = len(queries)
        for u, v in edges:
            if u > v:
                u, v = v, u
            degree[u-1] += 1
            degree[v-1] += 1
            enc = u * 30000 + v
            if enc not in rep:
                rep[enc] = 0
            rep[enc] += 1
        res = [0] * q
        degree1 = sorted(degree)
        # print(degree)
        for i in range(q):
            cap = queries[i]
            lo = n - 1
            for k in range(n - 1):
                while lo >= 0 and degree1[k] + degree1[lo] > cap:
                    lo -= 1
                res[i] += n - 1 - max(lo, k)
        # print(res)
        for enc, val in rep.items():
            u, v = enc // 30000, enc % 30000
            deg = degree[u-1] + degree[v-1]
            # print(u, v, deg, deg - val)
            for i in range(q):
                if deg > queries[i] and deg - val <= queries[i]:
                    res[i] -= 1
        return res
                
        