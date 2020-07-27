class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp
        if s == "":
            return ""
        n = len(s)
        start, maxlen = 0, 1
        dp = [[False] * n for _ in range(n)]
        #print(dp)
        for j in range(n): # calculation sequence: j then i
            for i in range(j + 1):
                if s[i] == s[j]:
                    if j - i < 2:
                        dp[i][j] = True
                        if j - i + 1 > maxlen:
                            start, maxlen = i, j - i + 1
                    elif i + 1 < n and dp[i + 1][j - 1]: # need dp[i + 1][j - 1]
                        dp[i][j] = True
                        if j - i + 1 > maxlen:
                            start, maxlen = i, j - i + 1
        return s[start: start + maxlen]