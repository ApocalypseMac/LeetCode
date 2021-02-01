class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        q = len(queries)
        n = len(candiesCount)
        ps = [0]
        p = 0
        for i in range(n):
            p += candiesCount[i]
            ps.append(p)
          
        res = []
        for t, d, c in queries:
            lb = d + 1
            ub = c * d + c
            llb, uub = ps[t] + 1, ps[t + 1]
            # print(lb, ub, llb, uub)
            if llb > ub or uub < lb:
                res.append(False)
            else:
                res.append(True)
        return res
        