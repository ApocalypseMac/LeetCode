class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls, lp = len(s), len(p)
        dp = [[False] * (lp + 1) for _ in range(ls + 1)] # dp[i][j] denotes whether p[:j] matches s[:i] 
        dp[0][0] = True
        def match(i, j):
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]
        
        for i in range(ls + 1):
            for j in range(1, lp + 1):
                if p[j - 1] == '*':
                    dp[i][j] |= dp[i][j - 2] # if * denotes zero char
                    if match(i, j - 1):
                        dp[i][j] |= dp[i - 1][j] # s[i - 1] matched and * could be reused
                elif match(i, j):
                    dp[i][j] |= dp[i - 1][j - 1] # one match one
        return dp[-1][-1]