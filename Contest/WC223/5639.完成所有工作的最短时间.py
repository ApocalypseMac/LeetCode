from functools import lru_cache
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        if n == k:
            return max(jobs)
        l = 2 ** n
        cost = [0] * (l)

        for i in range(l):
            for j in range(n):
                if i >> j & 1:
                    cost[i] += jobs[j]
        #print(cost)
        
        @lru_cache(None)
        def helper(state, idx):
            m = (l - 1) ^ state
            if idx == k - 1:
                return cost[m]
            res = helper(state, idx + 1)
            x = m
            while x:
                if cost[x] <= res: # cut branch
                    res = min(res, max(cost[x], helper(state|x, idx + 1)))
                x = (x - 1) & m
            return res
            
        
        
        return helper(0, 0)
#         # dp (TLE)
#         #print(cost)
#         dp = cost[:]
#         for i in range(1, k):
#             prev = dp[:]
#             dp = [float('INF')] * l
#             for mask in range(l):
#                 undone = mask ^ (l - 1)
#                 x = undone
#                 while x:
#                     dp[x|mask] = min(dp[x|mask], max(prev[mask], cost[x]))
#                     x = (x - 1) & undone
#         #print(dp)
                
        
#         return dp[-1]
                