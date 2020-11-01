import math
from functools import lru_cache
class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        nh, nv = destination[1], destination[0]
        @lru_cache(None)
        def comb(m, n):
            if n < m:
                return 0
            return math.factorial(n) // (math.factorial(m) * math.factorial(n - m))
        
        @lru_cache(None)
        def helper(nh, nv, k): 
            #print(nh, nv, k)
            if k == 0:
                return 'H' * nh + 'V' * nv
            elif nh == 0:
                return 'V' * nv
            elif nv == 0:
                return 'H' * nh
            i = 0
            res = ""
            while comb(nv, nv + i) <= k:
                i += 1
            res += 'H' * (nh - i) + 'V'
            #print(res, i)
            res += helper(i, nv - 1, k - comb(nv, nv + i - 1))
            return res
        return helper(nh, nv, k - 1)