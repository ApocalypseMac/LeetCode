class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        cnta, cntb = 0, 0
        for i in range(n):
            if s[i] == 'b':
                cntb += 1
            dp[i] += cntb
        for i in range(n-1, -1, -1):
            if s[i] == 'a':
                cnta += 1
            dp[i] += cnta
        #print(dp)
        return min(dp) - 1