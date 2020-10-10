class Solution:
    def keyboard(self, k: int, n: int) -> int:
        mod = 10 ** 9 + 7
        @lru_cache(None)
        def helper(a, b, c, d, e): # number of remaining freq
            count = 26 * k - (a + 2 * b + 3 * c + 4 * d + 5 * e) # remaining count
            if count > n: 
                return 0
            elif count == n: 
                return 1
            res = 0
            if a:
                res += a * helper(a - 1, b, c, d, e) % mod
            if b:
                res += b * helper(a + 1, b - 1, c, d, e) % mod
            if c:
                res += c * helper(a, b + 1, c - 1, d, e) % mod
            if d:
                res += d * helper(a, b, c + 1, d - 1, e) % mod
            if e:
                res += e * helper(a, b, c, d + 1, e - 1) % mod
            return res % mod
        
        freq = [0] * 5
        freq[k-1] = 26
        return helper(*tuple(freq))