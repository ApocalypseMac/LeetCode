class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
        #print(dp)
        for i in range(n - 2):
            if dp[0][i]:
                # print(i)
                for j in range(i + 1, n - 1):
                    if dp[i+1][j] and dp[j+1][n-1]:
                        return True
        return False