class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp
        ls = len(s)
        lp = len(p)
        dp = [[False] * (lp + 1) for _ in range(ls + 1)] # does p[:j] match s[:i]
        dp[0][0] = True
        for j in range(1, lp + 1): # initialize first row
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        for i in range(1, ls + 1):
            for j in range(1, lp + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[-1][-1]
        