from collections import defaultdict, Counter
class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        edges = defaultdict(set)
        cnt = Counter()
        for u, v in pairs:
            edges[u].add(v)
            edges[v].add(u)
            cnt[u] += 1
            cnt[v] += 1
        n = len(cnt)
        c = sorted(cnt.keys(), key = lambda x: -cnt[x])
        if cnt[c[0]] != n - 1: # root
            return 0
        res = 1
        for u, v in pairs:
            if cnt[u] == cnt[v]:
                res = 2
        pa = {}
        vis = {c[0]}
        for v in c:
            pa[v] = c[0]
        for u in c[1:]:
            for v in edges[u]:
                # print(u, v)
                if v not in vis: # v must in subtree of u
                    if pa[v] != pa[u]:
                        return 0
                    pa[v] = u
            vis.add(u)
        return res