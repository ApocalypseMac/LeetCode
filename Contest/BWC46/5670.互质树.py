class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        @lru_cache(None)
        def gcd(m, n):
            if m % n == 0:
                return n
            else:
                return gcd(n, m % n)
            
        cop = [[True] * 51 for _ in range(51)]
        for i in range(1, 51):
            for j in range(1, 51):
                if gcd(i, j) != 1:
                    cop[i][j] = False
                
        n = len(nums)
        edges1 = [[] for _ in range(n)]
        for u, v in edges:
            edges1[u].append(v)
            edges1[v].append(u)
        fa = [-1] * n
        vis = [False] * n
        dep = [0] * n
        vis[0] = True
        def dfs(u):
            # vis[u] = True
            for v in edges1[u]:
                if vis[v] is False:
                    vis[v] = True
                    fa[v] = u
                    dep[v] = dep[u] + 1
                    dfs(v)
    
        dfs(0)        
        # print(fa)
        # print(dep)
        res = [-1] * n
        ppa = [[-1] * 51 for _ in range(n)]
        def dfs2(u):
            pa = ppa[u][:]
            nu = nums[u]
            d = -1
            tmp = -1
            for i in range(1, 51):
                if cop[nu][i] is True and pa[i] != -1:
                    if dep[pa[i]] > d:
                        tmp = pa[i]
                        d = dep[pa[i]]
            res[u] = tmp
            pa[nu] = u
            for v in edges1[u]:
                if v != fa[u]:
                    ppa[v] = pa[:]
                    dfs2(v)
        dfs2(0)
        return res
            
                    
            
        