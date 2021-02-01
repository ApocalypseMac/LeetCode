from functools import lru_cache
class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        @lru_cache(None)
        def comb(n, v):
            res = 1
            v1 = v
            while v1:
                res *= n
                n += 1
                res //= (v - v1 + 1)
                v1 -= 1
            # print(k, v, res)
            return res % mod
        
        @lru_cache(None)
        def fact(k):
            fac = {}
            k1 = k
            for i in range(2, min(k + 1, 101)): 
                # if one number < 10 ^ 4 have prime factor larger than 100, it must be prime
                if i > k1:
                    break
                while k1 % i == 0:
                    k1 //= i
                    if i not in fac:
                        fac[i] = 0
                    fac[i] += 1
            if k1 > 1: 
                fac[k1] = 1
            # print(fac)
            return list(fac.values())
        
        res = []
        mod = 10 ** 9 + 7
        for n, k in queries:
            if k == 1 or n == 1:
                res.append(1)
                continue
            v = fact(k)
            r = 1
            for vi in v:
                r *= comb(n, vi)
                r %= mod
            res.append(r)
        return res