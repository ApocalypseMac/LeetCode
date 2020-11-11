class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        res = [0] * (n + 1)
        res[1] = 1
        for i in range(2, n + 1):
            if i & 1:
                res[i] = res[i//2] + res[i//2+1]
            else:
                res[i] = res[i//2]
        return max(res)