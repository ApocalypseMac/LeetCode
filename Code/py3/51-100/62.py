class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # C(m + n - 2, m - 1)
        result = 1
        for i in range(n - 1):
            result *= m + n - 2 - i
            result //= 1 + i
        return result