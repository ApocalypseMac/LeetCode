class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10 ** 9 + 7
        res = 0
        def digit(i):
            res = 0
            while i:
                i >>= 1
                res += 1
            return res
        for i in range(1, n + 1):
            d = digit(i)
            res <<= d
            res += i
            res %= mod
        return res
        
        