import math
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        def comb(n, m):
            return math.factorial(n) // (math.factorial(m) * math.factorial(n - m))
        @lru_cache(None)
        # n length, k segments
        def helper(n, k):
            if n < k:
                return 0
            if n == k: # each line length 1
                return 1
            if k == 1: # one line
                return n * (n + 1) // 2 
            res = 0
            # h(n, k) = \sum_i i * h(n - i, k - 1)
            # h(n-1, k) = \sum_i i * h(n - 1 - i, k - 1)
            # h(n-2, k) = \sum_i i * h(n - 2 - i, k - 1)
            # h(n, k) - h(n-1, k) = h(n-1, k) - h(n-2, k) + h(n-1, k-1)
            res = 2 * helper(n-1, k) - helper(n-2, k) + helper(n-1, k-1)
            res %= mod
            #print(n + 1, k, res)
            return res % mod
        return helper(n - 1, k)